import asyncio
from transformers import pipeline


# Loading the summarization Model
summarizer = pipeline("summarization", model="t5-small")


def textSummarizationJobDescription(text):
    summary = summarizer(text, max_length=150, min_length=75, do_sample=False)
    return summary[0]['summary_text']


def textSummarizationPersonalInformation(text):
    summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
    return summary[0]['summary_text']
