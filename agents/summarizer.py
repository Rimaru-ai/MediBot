from transformers import pipeline

# Load once at module level for efficiency
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_report(report_text: str) -> str:
    """Summarize medical report text."""
    if not report_text.strip():
        return "No text provided."
    summary = summarizer(report_text, max_length=60, min_length=25, do_sample=False)
    return summary[0]['summary_text']
