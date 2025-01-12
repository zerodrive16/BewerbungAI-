from regex_processing import performRegex
from spacy_summarizer import textSummarizationJobDescription, textSummarizationPersonalInformation
from openai_request import openAIRequest

# Information about the Job Description here
jobDescription = {
    "managerName": "TechSource",
    "companyName": "TechHub Inc.",
    "companyAddress": "123 Innovation Drive",
    "companyCity": "TechCity",
    "companyZipCode": "98765",
    "companyState": "TechState",
    "jobFieldName": "Senior Developer (C++, Python, JavaScript)",
    "jobFieldContent": """
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
}

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
    "skills": "Programming in Python, Java, and SQL. Strong problem-solving and analytical abilities. Experienced in developing RESTful APIs and microservices architecture. Proficient in cloud platforms like AWS and Azure. Skilled in using frameworks like Django, Spring Boot, and Flask. Expertise in database design and optimization for MySQL, PostgreSQL, and MongoDB. Familiar with DevOps tools such as Docker, Kubernetes, and Jenkins. Strong understanding of data structures, algorithms, and design patterns. Adept at working in Agile and Scrum methodologies. Excellent communication and teamwork skills for collaborative development.",
    "interests": "Hiking, photography, and playing chess."
}

# Text Preprocessing Job Description
# Summarize specific fields
jDFieldsSummarize = ["jobFieldContent"]

jDResults = {}

for key, value in jobDescription.items():
    if isinstance(value, str):
        jDProcessedValue = performRegex(value)

        if key in jDFieldsSummarize:
            jDResults[key] = {
                "processed": jDProcessedValue,
                "summary": textSummarizationJobDescription(jDProcessedValue)
            }
        else:
            jDResults[key] = jDProcessedValue
    else:
        jDResults[key] = value

finalJobDescription = jDResults


# Text Preprocessing Personal Information
# Summarize specific fields
pIFieldsSummarize = ["experience", "education", "skills", "interests"]

pIResults = {}

for key, value in personalInformation.items():
    if isinstance(value, str):
        pIProcessedValue = performRegex(value)

        if key in pIFieldsSummarize:
            pIResults[key] = {
                "processed": pIProcessedValue,
                "summary": textSummarizationPersonalInformation(pIProcessedValue)
            }
        else:
            pIResults[key] = pIProcessedValue
    else:
        pIResults[key] = value

finalPersonalDescription = pIResults

# OpenAI request
openAIOutput = openAIRequest(personalInformation, jobDescription, finalJobDescription, finalPersonalDescription)
print(openAIOutput)
