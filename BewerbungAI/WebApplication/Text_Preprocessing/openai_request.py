import openai
from dotenv import load_dotenv
import os

load_dotenv()

# Open AI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")


# Format the OpenAI request for Job Application Letter
def openAIRequest(resume_data, application_data, finalJobDescription, finalPersonalDescription):

    # Adding the Personal Header
    personalHeader = (
        f"Firstname: {resume_data['first_name']}, Lastname: {resume_data['last_name']}",
        f"Address: {resume_data['address']}",
        f"City: ZipCode: {resume_data['zipcode']}, {resume_data['city']}",
        f"Email: {resume_data['email']}",
        f"Phone: {resume_data['phone']}",
        f"Date: {resume_data['date']}"
    )

    # Adding the Job Header
    jobHeader = (
        f"managerName: {application_data['manager_name']}",
        f"CompanyName: {application_data['company_name']}",
        f"CompanyAddress: {application_data['company_address']}",
        f"CompanyCity: CompanyZipCode: {application_data['company_zip_code']}, {application_data['company_city']}"
    )

    # The content in the job application letter
    resume_datas = (
        f"Experience: {finalPersonalDescription['experience']['summary']}",
        f"Education: {finalPersonalDescription['education']['summary']}",
        f"Skills: {finalPersonalDescription['skills']['summary']}",
        f"Interests: {finalPersonalDescription['interests']['summary']}"
    )

    # Building the request
    requestField = (
        f"Write me a job Application letter with the following format and ensure it includes no extra commentary or text beyond the letter itself: \n"
        f"1. Personal Information {', '.join(personalHeader)} \n"
        f"2. Job Information {', '.join(jobHeader)} \n"
        f"3. Start with: 'Dear {application_data['manager_name']}' \n"
        f"4. Continue with the Job Application letter and include: "
        f"Personal Information {', '.join(resume_datas)} and {finalJobDescription['job']['summary']} \n"
        f"5 End it with: 'Sincerely, {resume_data['last_name']}, {resume_data['first_name']} \n"
        f"Please generate the job application letter in the format as instructed and should not include any explanations or extra information."
    )

    # Calling the ChatCompletion creation to build the job application letter and parse our desired preferences
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages = [
                {"role": "system", "content": "You are an expert assistant in writing professional job application letters. Focus strictly on generating the job application letter without adding any additional commentary."},
                {"role": "user", "content": requestField}
            ]
        )

        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error occurred: {e}"