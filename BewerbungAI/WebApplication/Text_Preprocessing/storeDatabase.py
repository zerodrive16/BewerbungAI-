from ..models import Data
from datetime import datetime


def databaseStorage(resume_data, application_data, app_final, personal_final, AIOutput):

    try:
        birthday = parse_date(resume_data['birthday'])
        gen_date = parse_date(resume_data['date'])
    except ValueError as e:
        print("Error in parsing")
        return None

    # Parse all the Data to the Attributes in the Database
    data_instance = Data(
        firstname=resume_data['first_name'],
        lastname=resume_data['last_name'],
        birthday=birthday,
        address=resume_data['address'],
        city=resume_data['city'],
        zipcode=resume_data['zipcode'],
        phone=resume_data['phone'],
        email=resume_data['email'],
        date=gen_date,
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

    # Saving the instance
    data_instance.save()
    return data_instance


# Parse as Date format (DateTime)
def parse_date(date_str):
    date_formats = ['%d.%m.%Y', '%Y-%m-%d', '%m/%d/%Y', '%d/%m/%Y']

    for fmt in date_formats:
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Date '{date_str}' is not in a supported format. Expected formats: {', '.join(date_formats)}")
