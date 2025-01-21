from transformers import pipeline


# Loading the summarization Model
summarizer = pipeline("summarization", model="t5-small")


# Summarizes the Job Description
async def textSummarizationJobDescription(text):
    input_length = len(text.split())
    # Skip the summarization if it's less than 75 words
    if input_length <= 75:
        return text
    else:
        summary = summarizer(text, max_length=150, min_length=75, do_sample=False)
        return summary[0]['summary_text']


# Summarizes the Personal Information
async def textSummarizationPersonalInformation(text):
    input_length = len(text.split())
    # Skip the summarization if it's less than 50 words
    if input_length <= 50:
        return text
    else:
        max_length = min(200, max(50, input_length // 2)) # Divide if it goes the 50 words mark
        min_length = max(25, max_length // 2)

        summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        return summary[0]['summary_text']