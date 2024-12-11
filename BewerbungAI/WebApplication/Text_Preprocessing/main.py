import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments, TextDataset, \
    DataCollatorForLanguageModeling, AutoModelForCausalLM
import json
from datasets import Dataset


def loadingModelTokenizer():
    model_name = "gpt2"
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    return model, tokenizer


def loadDataset(training_file, tokenizer):
    with open(training_file, 'r') as file:
        data = json.load(file)




def fineTuning(model, tokenizer, training_file, output_file):
    dataset = loadDataset(training_file, tokenizer)


    training_args = TrainingArguments(
        output_dir=output_file,
        overwrite_output_dir=True,
        num_train_epochs=10,
        per_device_train_batch_size=4,
        save_steps=500,
        save_total_limit=2,
        logging_dir=f"{output_file}/logs",
        logging_steps=100,
        learning_rate=5e-5,
        weight_decay=0.01,
        warmup_steps=500,
        evaluation_strategy="steps",
        eval_steps=500,
        save_strategy="steps"

    )

def main():
    training_file = "datasets/dataset.json"
    output_file = "datasets/finetunedDataset.json"

    # Defining the Model and Tokenizer
    model, tokenizer = loadingModelTokenizer()

    # Finetuning Model
    fineTuning(model, tokenizer, training_file, output_file)



if __name__ == "__main__":
    main()