import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from summarizer import TextSummarizer

def main():
    # Sample text for testing
    sample_text = """
    Climate change represents one of the most pressing challenges of our time. 
    Rising global temperatures are causing widespread environmental disruption, 
    including melting ice caps, rising sea levels, and extreme weather events. 
    The primary driver of climate change is the increased concentration of greenhouse gases 
    in the atmosphere, particularly carbon dioxide from burning fossil fuels. 
    Scientific consensus confirms that human activities are the dominant cause of recent climate change. 
    Addressing this crisis requires immediate and coordinated global action, including 
    transitioning to renewable energy sources, improving energy efficiency, 
    and implementing policies to reduce carbon emissions. 
    The consequences of inaction could be catastrophic for future generations.
    """
    
    print("🤖 AI Text Summarizer - Example Usage\n")
    print("Original Text:")
    print("-" * 50)
    print(sample_text)
    print(f"\nOriginal word count: {len(sample_text.split())} words\n")
    
    # Initialize summarizer
    print("Loading AI model...")
    summarizer = TextSummarizer()
    
    # Generate summary
    print("Generating summary...")
    summary = summarizer.summarize(sample_text, max_length=100, min_length=30)
    
    print("\nSummary:")
    print("-" * 50)
    print(summary)
    print(f"\nSummary word count: {len(summary.split())} words")
    
    # Calculate compression ratio
    compression = (len(summary.split()) / len(sample_text.split())) * 100
    print(f"Compression ratio: {compression:.1f}%")

if __name__ == "__main__":
    main()
