import re


def performRegex(text):
    # Remove emojis and non-printable characters
    cleaned_comment = re.sub(r'[^\x00-\x7F]+', '', text)
    # Remove special characters, keeping only letters and numbers (', !, ., ?, +, -, and ,)
    cleaned_comment = re.sub(r'[^a-zA-Z0-9\s\'!,\.\?\+\-]', '', cleaned_comment)
    # Remove extra spaces
    cleaned_comment = re.sub(r'\s+', ' ', cleaned_comment).strip()

    return cleaned_comment