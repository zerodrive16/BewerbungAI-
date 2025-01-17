import openai

openai.api_key = "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"


def openAIRequest(resume_data, application_data, finalJobDescription, finalPersonalDescription):

    personalHeader = (
        f"Firstname: {resume_data['first_name']}, Lastname: {resume_data['last_name']}",
        f"Address: {resume_data['address']}",
        f"City: ZipCode: {resume_data['zipcode']}, {resume_data['city']}",
        f"Email: {resume_data['email']}",
        f"Phone: {resume_data['phone']}",
        f"Date: {resume_data['date']}"
    )

    jobHeader = (
        f"managerName: {application_data['manager_name']}",
        f"CompanyName: {application_data['company_name']}",
        f"CompanyAddress: {application_data['company_address']}",
        f"CompanyCity: CompanyZipCode: {application_data['company_zip_code']}, {application_data['company_city']}"
    )

    resume_datas = (
        f"Experience: {finalPersonalDescription['experience']['summary']}",
        f"Education: {finalPersonalDescription['education']['summary']}",
        f"Skills: {finalPersonalDescription['skills']['summary']}",
        f"Interests: {finalPersonalDescription['interests']['summary']}"
    )

    # Join the strings into a single string
    requestField = (
        f"Write me a job Application letter with the following format: \n"
        f"1. Personal Information {', '.join(personalHeader)} \n"
        f"2. Job Information {', '.join(jobHeader)} \n"
        f"3. Start with: 'Dear {application_data['manager_name']}' \n"
        f"4. Continue with the Job Application letter and include: "
        f"Personal Information {', '.join(resume_datas)} and {finalJobDescription['job']['summary']} \n"
        f"5 End it with: 'Sincerely, {resume_data['last_name']}, {resume_data['first_name']} \n"
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