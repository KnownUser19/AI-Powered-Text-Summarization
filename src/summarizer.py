from transformers import pipeline
import torch
import logging
from typing import List, Optional

class TextSummarizer:
    """Advanced text summarization using transformer models."""
    
    def __init__(self, model_name: str = "facebook/bart-large-cnn"):
        self.model_name = model_name
        self.device = 0 if torch.cuda.is_available() else -1
        self._load_model()
        
    def _load_model(self):
        """Load the summarization pipeline."""
        try:
            self.summarizer = pipeline(
                "summarization",
                model=self.model_name,
                device=self.device
            )
            print(f"✅ Model {self.model_name} loaded successfully")
        except Exception as e:
            print(f"❌ Error loading model: {e}")
            raise
    
    def summarize(self, text: str, max_length: int = 150, min_length: int = 30) -> str:
        """Summarize the given text."""
        if not text.strip():
            raise ValueError("Input text cannot be empty")
        
        # Handle long texts by chunking
        if len(text.split()) > 1000:
            return self._summarize_long_text(text, max_length, min_length)
        
        try:
            summary = self.summarizer(
                text,
                max_length=max_length,
                min_length=min_length,
                do_sample=False
            )
            return summary[0]['summary_text']
        except Exception as e:
            print(f"❌ Summarization error: {e}")
            raise
    
    def _summarize_long_text(self, text: str, max_length: int, min_length: int) -> str:
        """Handle long texts by chunking."""
        words = text.split()
        chunks = []
        
        # Split into chunks of ~500 words
        chunk_size = 500
        for i in range(0, len(words), chunk_size):
            chunk = ' '.join(words[i:i + chunk_size])
            chunks.append(chunk)
        
        summaries = []
        for chunk in chunks:
            try:
                summary = self.summarizer(
                    chunk,
                    max_length=100,
                    min_length=20,
                    do_sample=False
                )
                summaries.append(summary[0]['summary_text'])
            except Exception as e:
                print(f"⚠️ Warning: Error summarizing chunk: {e}")
                continue
        
        # Combine summaries
        combined = ' '.join(summaries)
        
        # Final summarization if combined summary is still long
        if len(combined.split()) > max_length:
            final_summary = self.summarizer(
                combined,
                max_length=max_length,
                min_length=min_length,
                do_sample=False
            )
            return final_summary[0]['summary_text']
        
        return combined
