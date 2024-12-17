from transformers import GPT2LMHeadModel, Trainer, TrainingArguments, DataCollatorForLanguageModeling, GPT2Tokenizer
import json


def loadModelAndTokenizer():
    model_name = "gpt2"

    # Initializing the Tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    # Set pad_token as eos_token (batch same length required)
    tokenizer.pad_token = tokenizer.eos_token

    # Setting up the model
    model = GPT2LMHeadModel.from_pretrained(model_name)
    return model, tokenizer


def retrievalDataset(dataset, tokenizer, block_size=128):
    # Open the dataset
    with open(dataset, 'r') as file:
        data = json.load(file)

    # Enter the array of "train"
    train_data = data.get("train", [])

    # Joining Array to String
    string_data = [
        f"Prompt: {' '.join(entry['prompt'])} Completion: {' '.join(entry['completion'])}"
        for entry in train_data
    ]

    # Tokenizing the dataset
    inputs = []
    for text in string_data:
        tokenization = tokenizer(text, truncation=True, padding="max_length", max_length=block_size, return_tensors="pt")
        inputs.append({
            "input_ids": tokenization["input_ids"].squeeze(), "attention_mask": tokenization["attention_mask"].squeeze()
        })

    return inputs


def fineTuneGPT2(model, tokenizer, dataset_file, trained_file):
    tokenized_dataset = retrievalDataset(dataset_file, tokenizer)

    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False
    )

    # Training arguments
    training_args = TrainingArguments(
        output_dir=trained_file,
        overwrite_output_dir=True,
        num_train_epochs=20,
        per_device_train_batch_size=4,
        save_steps=500,
        save_total_limit=2,
        logging_dir=f"{trained_file}/logs",
        logging_steps=100,
        learning_rate=5e-5,
        weight_decay=0.01,
        warmup_steps=500,
        save_strategy="steps",  # Saving Model in intervals
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=tokenized_dataset,
    )

    # Start training
    trainer.train()

    # Save the model and tokenizer
    model.save_pretrained(trained_file)
    tokenizer.save_pretrained(trained_file)


if __name__ == '__main__':
    # Calling the dataset
    dataset_file = "datasets/dataset2.json"
    trained_file = "datasets/finetuned_model"

    # Setting up the GPT-2 model and tokenizer
    model, tokenizer = loadModelAndTokenizer()

    # FineTune the Model with Dataset
    fineTuneGPT2(model, tokenizer, dataset_file, trained_file)