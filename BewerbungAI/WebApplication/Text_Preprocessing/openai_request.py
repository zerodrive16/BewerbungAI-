import openai

openai.api_key = "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"


def openAIRequest(personalInformation, jobInformation, finalJobDescription, finalPersonalInformation):

    requestField = f"Write me a job application letter including the jobDescription: {finalJobDescription['jobFieldContent']['summary']} and the personal information {finalPersonalInformation['experience']['summary']}, {finalPersonalInformation['education']['summary']}, {finalPersonalInformation['skills']['summary']}, {finalPersonalInformation['interests']['summary']}"

    personalHeader = (
        f"surname: {personalInformation['surname']}, lastname: {personalInformation['lastname']}",
        f"Address: {personalInformation['address']}",
        f"City: {personalInformation['city']}, State: {personalInformation['state']}, ZipCode: {personalInformation['zipcode']}",
        f"Email: {personalInformation['email']}",
        f"Phone: {personalInformation['phone']}",
        f"Date: {personalInformation['date']}"
    )

    jobHeader = (
        f""
    )

    personalInformation = (
        f"Experience: {finalPersonalInformation['experience']['summary']}",
        f"Education: {finalPersonalInformation['education']['summary']}",
        f"Skills: {finalPersonalInformation['skills']['summary']}",
        f"Interests: {finalPersonalInformation['interests']['summary']}"
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

