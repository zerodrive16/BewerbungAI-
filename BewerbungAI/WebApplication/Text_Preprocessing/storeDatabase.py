from ..models import Data


def databaseStorage(resume_data, application_data, app_final, personal_final, AIOutput):
    return Data(
        firstname=resume_data['first_name'],
        lastname=resume_data['last_name'],
        birthday=resume_data['birthday'],
        address=resume_data['address'],
        city=resume_data['city'],
        zipcode=resume_data['zipcode'],
        phone=resume_data['phone'],
        email=resume_data['email'],
        date=resume_data['date'],
        experience=personal_final['experience']['summary'],
        education=personal_final['education']['summary'],
        skills=personal_final['skills']['summary'],
        interests=personal_final['interests']['summary'],

        managerName=application_data['manager_name'],
        companyName=application_data['company_name'],
        companyAddress=application_data['company_address'],
        companyCity=application_data['company_city'],
        companyZipCode=application_data['company_zip_code'],
        jobFieldName=application_data['job_field_name'],
        jobFieldContent=app_final['job']['summary'],
        jobApplicationContent=AIOutput
    )
