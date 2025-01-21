import re


# performs the Regular Expression for various user input fields
def performRegex(text):
    if not isinstance(text, str):
        text = str(text)

    # Remove emojis and non-printable characters / Unicode
    cleaned_comment = re.sub(r'[^\x20-\x7E]', '', text)
    # Remove special characters, keeping only letters and numbers (', !, ., ?, +, -, and ,)
    cleaned_comment = re.sub(r'[^a-zA-Z0-9\s\'!,\.\?\+\-]', '', cleaned_comment)
    # Remove extra spaces
    cleaned_comment = re.sub(r'\s+', ' ', cleaned_comment).strip()

    return cleaned_comment