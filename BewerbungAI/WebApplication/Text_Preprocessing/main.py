from regex_processing import performRegex
from spacy_summarizer import textSummarizationJobDescription, textSummarizationPersonalInformation


# Information about the Job Description here
jobDescription = [
    """
    Job Title: Senior Developer (C++, Python, JavaScript) ⚙️🚀

    Location: Remote 🌐 / Hybrid 🏢

    Overview:
    Are you a code ninja 🥷 ready to tackle complex challenges? Join us as a Senior Developer 💻 to build innovative software solutions 💡. We're looking for someone who excels in problem-solving 🤔, thrives under pressure 🕒, and enjoys delivering quality code 📋✅.

    Key Responsibilities:

    Develop, debug 🐛, and deploy applications 🚀 in C++, Python, and JavaScript.
    Collaborate 🤝 with cross-functional teams (e.g., Designers 🎨, QA 🧪).
    Implement ✍️ REST APIs & microservices 🧩.
    Optimize system performance 🏎️⚡.
    Maintain detailed documentation 📜📂.
    Requirements:

    5+ years' experience in software development 💾.
    Strong understanding of OOP principles 🌀 & design patterns 🧵.
    Familiarity with Git 🧑‍💻, CI/CD pipelines 🛠️, and Docker 🐳.
    Excellent problem-solving skills (think "Rubik’s Cube 🧩").
    Perks & Benefits:

    Competitive salary 💰💳.
    Flexible work hours ⏰.
    Wellness programs 🏋️‍♂️🧘‍♀️.
    Learning stipends 📚💡.
    How to Apply:
    Submit your résumé 📑, GitHub profile 👾, and portfolio 🖼️ to jobs@techhub.io.

    Let’s build the future together! ✨🌟
    """
]

# Information about the person here
personalInformation = {
    "surname": "Max",
    "lastname": "Musterman",
    "birthday": "19.9.1999",
    "address": "Musterman Straße 2a",
    "city": "Musterstadt",
    "zipcode": "12345",
    "phone": "+49 123 4567890",
    "email": "max.musterman@example.com",
    "date": "10.01.2025",
    "experience": "Worked as a software developer at TechCorp for 3 years. Interned as a data analyst at DataInc.",
    "education": "Bachelor’s Degree in Computer Science from Muster University, graduated in 2021.",
    "skills": "Programming in Python, Java, and SQL. Strong problem-solving and analytical abilities.",
    "interests": "Hiking, photography, and playing chess."
}

# Performing Preprocessing for JobDescription
regex_jobDescription = performRegex(jobDescription)
print(regex_jobDescription)
spacy_jobDescription = textSummarizationJobDescription(regex_jobDescription)

print(spacy_jobDescription)


'''
# Performing Preprocessing for Personal Information
regex_personalInformation = {key: performRegex(value) if isinstance(value, str) else value for key, value in personalInformation.items()}
print("Processed Personal Information:", regex_personalInformation)

# Summarize specific fields
fields_to_summarize = ["experience", "education", "skills", "interests"]
summarized_fields = {}
for field in fields_to_summarize:
    summarized_fields[field] = textSummarizationPersonalInformation(regex_personalInformation[field])

# Display summarized fields
for field, summary in summarized_fields.items():
    print(f"Summary of {field.capitalize()}:\n{summary}\n")
'''
