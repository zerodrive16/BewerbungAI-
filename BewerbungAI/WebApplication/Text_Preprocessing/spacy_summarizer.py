import spacy
from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer

# Load required models
nlp = spacy.load("en_core_web_sm")
summarizer = pipeline("summarization", model="t5-small")

def process_job_description(text, num_keywords=5):
    # Step 1: Extract Entities
    def extract_entities(text):
        doc = nlp(text)
        entities = {"Job Title": [], "Skills": [], "Qualifications": []}
        for ent in doc.ents:
            if ent.label_ == "JOB_TITLE":
                entities["Job Title"].append(ent.text)
            elif ent.label_ == "SKILL":
                entities["Skills"].append(ent.text)
            elif ent.label_ == "EDUCATION":
                entities["Qualifications"].append(ent.text)
        return entities

    # Step 2: Summarize Job Description
    def summarize_text(text):
        summary = summarizer(text, max_length=100, min_length=50, do_sample=False)
        return summary[0]['summary_text']

    # Step 3: Extract Keywords with TF-IDF
    def extract_keywords(text, num_keywords):
        vectorizer = TfidfVectorizer(stop_words="english", max_features=num_keywords)
        vectors = vectorizer.fit_transform([text])
        keywords = vectorizer.get_feature_names_out()
        return keywords

    # Process the text
    entities = extract_entities(text)
    summary = summarize_text(text)
    keywords = extract_keywords(text, num_keywords)

    # Return results as a dictionary
    return {
        "Entities": entities,
        "Summary": summary,
        "Keywords": keywords
    }