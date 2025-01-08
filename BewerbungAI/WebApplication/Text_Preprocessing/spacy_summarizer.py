import spacy
from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Example Job Description
job_description = """
Ausführung von Inspektions-, Wartungs- u. Instandsetzungsarbeiten an Niederspannungsanlagen, Erdungs- u. Blitzschutzanlagen, Ex Schutzanlagen sowie an Antrieben
Revision von Schaltplänen / Schaltungsunterlagen
Bearbeitung der Aufträge aus dem Anlagenfahrbetrieb.
Überprüfungen der Anlagen u. Einrichtungen nach DGUV-Vorschrift 3 als zur Prüfung befähigte Person gemäß BetrSichV/TRBS (Besichtigen, Messen, Erproben u. Protokollieren) und Beseitigung der festgestellten Mängel.
Anfertigen u. Auswerten von Prüf- u. Messprotokollen.
Durchführung von Installationsarbeiten
Koordinierung von externen Dienstleistern
"""

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
    summarizer = pipeline("summarization", model="t5-small")  # Open-source summarization
    summary = summarizer(text, max_length=100, min_length=25, do_sample=False)
    return summary[0]['summary_text']

# Step 3: Extract Keywords with TF-IDF
def extract_keywords(text, num_keywords=5):
    vectorizer = TfidfVectorizer(stop_words="english", max_features=num_keywords)
    vectors = vectorizer.fit_transform([text])
    keywords = vectorizer.get_feature_names_out()
    return keywords

# Process Job Description
entities = extract_entities(job_description)
summary = summarize_text(job_description)
keywords = extract_keywords(job_description)

# Display Results
print("Extracted Entities:", entities)
print("Job Description Summary:", summary)
print("Top Keywords:", keywords)