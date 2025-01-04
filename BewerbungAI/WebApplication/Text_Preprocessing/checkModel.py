from transformers import GPT2LMHeadModel, GPT2Tokenizer
import os
import nltk

nltk.download('punkt')


# Function to truncate text to the nearest sentence within the word limit
def truncate_to_nearest_sentence(text, word_limit):
    # Split the text into sentences
    sentences = nltk.sent_tokenize(text)

    truncated_text = ""
    word_count = 0

    # Add sentences until the word limit is reached
    for sentence in sentences:
        sentence_word_count = len(sentence.split())
        if word_count + sentence_word_count > word_limit:
            break
        truncated_text += sentence + " "
        word_count += sentence_word_count

    return truncated_text.strip()


# Function to generate text with the fine-tuned model
def generate_text(model, tokenizer, prompt, max_words=200):
    # Encode the prompt text
    inputs = tokenizer(prompt, return_tensors='pt')

    input_ids = inputs['input_ids']
    attention_mask = inputs.get('attention_mask', None)

    # Generate output from the model
    outputs = model.generate(
        input_ids,
        attention_mask=attention_mask,
        max_new_tokens=400,
        do_sample=True,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        temperature=0.7,
        top_k=50,
        pad_token_id=tokenizer.eos_token_id
    )

    # Decode the generated output to text
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Truncate the text to the nearest sentence within the word limit
    truncated_text = truncate_to_nearest_sentence(generated_text, max_words)
    return truncated_text


# Load the fine-tuned model and tokenizer
base_path = os.path.dirname(os.path.abspath(__file__))
dataset_json_file = os.path.join(base_path, 'datasets/dataset2.json')
trained_file = os.path.join(base_path, 'datasets/finetuned_model')
model = GPT2LMHeadModel.from_pretrained(trained_file)
tokenizer = GPT2Tokenizer.from_pretrained(trained_file)
tokenizer.pad_token = tokenizer.eos_token

# Example test prompt
prompt = (
    "Write me a professional job application letter for the person Stefan Nguyen and he studied in University of Applied Sciences about Webdevelopment")

# Generate text based on the prompt
generated_text = generate_text(model, tokenizer, prompt, max_words=200)
print("Generated Text:\n", generated_text)
