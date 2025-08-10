import streamlit as st
import sys
import os

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from summarizer import TextSummarizer

# Page config
st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .summary-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin: 1rem 0;
    }
    .stats-box {
        background-color: #e8f4f8;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown('<h1 class="main-header">🤖 AI Text Summarizer</h1>', unsafe_allow_html=True)
    st.markdown("**Transform lengthy text into concise, meaningful summaries using advanced AI**")
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Settings")
        
        model_choice = st.selectbox(
            "Choose AI Model",
            [
                "facebook/bart-large-cnn",
                "google/pegasus-cnn_dailymail", 
                "t5-base"
            ],
            help="Select the AI model for summarization"
        )
        
        max_length = st.slider("Maximum Summary Length", 50, 500, 150)
        min_length = st.slider("Minimum Summary Length", 10, 100, 30)
        
        st.markdown("---")
        st.markdown("### 💡 Tips")
        st.info("""
        • Best results with 100+ words
        • Use clear, well-structured text
        • Longer texts = better summaries
        • Try different models for variety
        """)

    # Main content
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.subheader("📝 Input Text")
        
        # Text input
        input_text = st.text_area(
            "Enter your text here:",
            height=300,
            placeholder="Paste your article, document, or any text you want to summarize...",
            help="Enter at least 50 words for best results"
        )
        
        # Sample text button
        if st.button("📄 Load Sample Text"):
            sample_text = """
            Artificial Intelligence (AI) has revolutionized numerous industries and continues to shape our future. 
            From healthcare to transportation, AI applications are becoming increasingly sophisticated and widespread. 
            Machine learning algorithms can now diagnose diseases with remarkable accuracy, often surpassing human specialists. 
            In transportation, autonomous vehicles are being tested on roads worldwide, promising safer and more efficient travel. 
            Natural language processing has enabled AI assistants to understand and respond to human queries with increasing nuance. 
            Computer vision technology allows machines to interpret visual information, leading to advances in robotics and surveillance. 
            However, the rapid advancement of AI also raises important ethical questions about job displacement, privacy, and algorithmic bias. 
            As we continue to integrate AI into society, it's crucial to develop frameworks that ensure these technologies benefit humanity while minimizing potential risks. 
            The future of AI holds immense promise, but it requires careful consideration and responsible development practices.
            """
            st.session_state.sample_text = sample_text
            st.rerun()
        
        if 'sample_text' in st.session_state:
            input_text = st.session_state.sample_text
        
        # Summarize button
        if st.button("🚀 Generate Summary", type="primary", use_container_width=True):
            if input_text and len(input_text.split()) >= 10:
                with st.spinner("🤖 AI is analyzing your text..."):
                    try:
                        # Initialize summarizer
                        summarizer = TextSummarizer(model_name=model_choice)
                        
                        # Generate summary
                        summary = summarizer.summarize(
                            input_text,
                            max_length=max_length,
                            min_length=min_length
                        )
                        
                        # Display results
                        st.success("✅ Summary generated successfully!")
                        
                        # Summary display
                        st.markdown("### 📋 Summary")
                        st.markdown(f'<div class="summary-box">{summary}</div>', unsafe_allow_html=True)
                        
                        # Statistics
                        original_words = len(input_text.split())
                        summary_words = len(summary.split())
                        compression_ratio = (summary_words / original_words) * 100
                        
                        st.markdown("### 📊 Statistics")
                        col_stat1, col_stat2, col_stat3 = st.columns(3)
                        
                        with col_stat1:
                            st.metric("Original Words", original_words)
                        with col_stat2:
                            st.metric("Summary Words", summary_words)
                        with col_stat3:
                            st.metric("Compression", f"{compression_ratio:.1f}%")
                        
                        # Download option
                        st.download_button(
                            "📥 Download Summary",
                            summary,
                            file_name="summary.txt",
                            mime="text/plain",
                            use_container_width=True
                        )
                        
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")
                        st.info("💡 Try using a different model or check your text input.")
            else:
                st.warning("⚠️ Please enter at least 10 words for summarization.")
    
    with col2:
        st.subheader("🎯 Model Info")
        
        model_descriptions = {
            "facebook/bart-large-cnn": {
                "description": "Excellent for news articles and general text",
                "strength": "High quality summaries",
                "speed": "⭐⭐⭐"
            },
            "google/pegasus-cnn_dailymail": {
                "description": "Specialized for news content",
                "strength": "Great for articles",
                "speed": "⭐⭐"
            },
            "t5-base": {
                "description": "Versatile general-purpose model",
                "strength": "Balanced performance",
                "speed": "⭐⭐⭐⭐"
            }
        }
        
        if model_choice in model_descriptions:
            info = model_descriptions[model_choice]
            st.markdown(f"""
            <div class="stats-box">
            <strong>Current Model:</strong> {model_choice.split('/')[-1]}<br>
            <strong>Best for:</strong> {info['description']}<br>
            <strong>Strength:</strong> {info['strength']}<br>
            <strong>Speed:</strong> {info['speed']}
            </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
