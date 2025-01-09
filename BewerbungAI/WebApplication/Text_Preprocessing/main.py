from regex_processing import performRegex
from spacy_summarizer import process_job_description


text_example = [
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

processed_text = performRegex(text_example)
print(processed_text)
res = process_job_description(processed_text)

print("Entities:", res["Entities"])
print("Summary:", res["Summary"])
print("Keywords:", res["Keywords"])