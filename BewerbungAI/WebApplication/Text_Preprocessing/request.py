import openai

openai.api_key = "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"


def chat(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages = [
                {"role": "system", "content": "You are an expert assistant in writing professional job application letters. Your advice and responses should focus on helping users craft compelling and tailored letters for job applications."},
                {"role": "user", "content": prompt}
            ]
        )

        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error occurred: {e}"


if __name__ == "__main__":
    user_input = input("Write something...")

    response = chat(user_input)

    print("Result: ", response)
