"""
Intelligent Text Summarization Suite

A sophisticated AI-powered text summarization package that leverages 
state-of-the-art transformer models for document summarization.

Author: Your Name
Version: 1.0.0
"""

__version__ = "1.0.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

# Import main classes for easy access
from .summarizer import TextSummarizer
from .pdf_processor import PDFProcessor
from .utils import validate_text, clean_text, chunk_text, format_summary

# Define what gets imported with "from src import *"
__all__ = [
    "TextSummarizer",
    "PDFProcessor", 
    "validate_text",
    "clean_text",
    "chunk_text",
    "format_summary"
]

# Package metadata
SUPPORTED_MODELS = [
    "facebook/bart-large-cnn",
    "google/pegasus-cnn_dailymail",
    "t5-base",
    "google/flan-t5-base"
]

# Configuration defaults
DEFAULT_CONFIG = {
    "model_name": "facebook/bart-large-cnn",
    "max_length": 150,
    "min_length": 30,
    "chunk_size": 512
}
