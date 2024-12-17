from transformers import GPT2LMHeadModel, GPT2Tokenizer
import os


# Function to generate text with the fine-tuned model
def generate_text(model, tokenizer, prompt, max_length=500):
    # Encode the prompt text
    inputs = tokenizer(prompt, return_tensors='pt')

    input_ids = inputs['input_ids']
    attention_mask = inputs.get('attention_mask', None)

    # Generate output from the model
    outputs = model.generate(
        input_ids,
        attention_mask=attention_mask,
        max_length=max_length,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        temperature=0.7,
        top_k=50,
        pad_token_id=tokenizer.eos_token_id
    )

    # Decode the generated output to text
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text


# Load the fine-tuned model and tokenizer
base_path = os.path.dirname(os.path.abspath(__file__))
dataset_json_file = os.path.join(base_path, 'datasets/dataset2.json')
trained_file = os.path.join(base_path, 'datasets/finetuned_model')
model = GPT2LMHeadModel.from_pretrained(trained_file)
tokenizer = GPT2Tokenizer.from_pretrained(trained_file)
tokenizer.pad_token = tokenizer.eos_token

# Example test prompt
prompt = ("Write me a professional job application letter in the field of SAP Consulting with around 50 words.")

# Generate text based on the prompt
generated_text = generate_text(model, tokenizer, prompt)
print("Generated Text:\n", generated_text)
