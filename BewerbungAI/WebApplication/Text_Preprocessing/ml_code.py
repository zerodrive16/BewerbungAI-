from transformers import AutoModelForCausalLM, AutoTokenizer

# Using the Pre-Trained Model from GPT-2
model_name = "gpt2"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Loading the CSV
def pLoadCsv(personal_data):
    pass

def jobRequirementsCsv(job_requirements):
    pass

def generate_text(prompt, max_length=200):
    # Encodes the tokenized so gpt-2 can understand
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs,
                             # Limit the length of text to 200 tokens
                             max_length=max_length,
                             # Only one text should be generated
                             num_return_sequence=1,
                             # No repeating multiple generated phrases
                             no_repeat_ngram_size=2,
                             # Make text creative
                             top_p=0.95,top_k=50)
                             # Can be more restrictions or additons...

    # Converting the tokens back to human-readable text
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def createJobApplication(pData):
    prompt = (f"Write a creative and professional application for the candidate: "
              f"FName: {pData['FMame']}"
              f"LName: {pData['LName']}"
              f"Date: {pData['Date']}"
              f"PlaceOfBirth: {pData['PlaceOfBirth']}"
              f"Nationality: {pData['Nationality']}"
              f"Address: {pData['Address']}"
              f"Phone: {pData['Phone']}"
              f"Email: {pData['Email']}"
              f"Work experience: {pData['WorkExperience']}"
              f"Education: {pData['Education']}"
              f"Skills: {pData['Skills']}"
              f"Languages: {pData['Languages']}"
              f"Interests: {pData['Interests']}"
              f"It should also consists of the follow criteria of the {pData['JobRequirements']}")

    return generate_text(prompt)

def main(csv_path_personal, csv_path_job_requirements):
    data = pLoadCsv(csv_path_personal), jobRequirementsCsv(csv_path_job_requirements)

    for row in data:
        print(f"Generating the Job application for {row['FName']}, {row['LName']}...\n")
        print(f"Considering the Job requirements...\n")
        requestApplication = createJobApplication(row)
        print(requestApplication)



if __name__ == "__main__":
    # Take both CSV files
    csv_path_personal = ".personal_csv file"
    csv_path_job_requirements = ".job_requirements_csv"
    main(csv_path_personal, csv_path_job_requirements)
