import openai
import asyncio
import aiohttp

openai.api_key = "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"


def openAIRequest(personalInformation, jobInformation, finalJobDescription, finalPersonalInformation):

    personalHeader = (
        f"surname: {personalInformation['surname']}, lastname: {personalInformation['lastname']}",
        f"Address: {personalInformation['address']}",
        f"City: ZipCode: {personalInformation['zipcode']}, {personalInformation['city']}",
        f"Email: {personalInformation['email']}",
        f"Phone: {personalInformation['phone']}",
        f"Date: {personalInformation['date']}"
    )

    jobHeader = (
        f"managerName: {jobInformation['managerName']}",
        f"CompanyName: {jobInformation['companyName']}",
        f"CompanyAddress: {jobInformation['companyAddress']}",
        f"CompanyCity: CompanyZipCode: {jobInformation['companyZipCode']}, {jobInformation['companyCity']}"
    )

    personalInformations = (
        f"Experience: {finalPersonalInformation['experience']['summary']}",
        f"Education: {finalPersonalInformation['education']['summary']}",
        f"Skills: {finalPersonalInformation['skills']['summary']}",
        f"Interests: {finalPersonalInformation['interests']['summary']}"
    )

    # Join the strings into a single string
    requestField = (
        f"Write me a job Application letter with the following format: \n"
        f"1. Personal Information {', '.join(personalHeader)} \n"
        f"2. Job Information {', '.join(jobHeader)} \n"
        f"3. Start with: 'Dear {jobInformation['managerName']}' \n"
        f"4. Continue with the Job Application letter and include: "
        f"Personal Information {', '.join(personalInformations)} and {finalJobDescription['jobFieldContent']['summary']} \n"
        f"5 End it with: 'Sincerely, {personalInformation['lastname']}, {personalInformation['surname']} \n"
        f"Please generate the job application letter in the format as instructed"
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages = [
                {"role": "system", "content": "You are an expert assistant in writing professional job application letters. Your advice and responses should focus on helping users craft compelling and tailored letters for job applications."},
                {"role": "user", "content": requestField}
            ]
        )

        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error occurred: {e}"

