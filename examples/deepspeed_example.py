
# Import necessary libraries
from accelerate import Accelerator
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer, TrainingArguments, Trainer
from datasets import load_dataset
import deepspeed

# Initialize Accelerate
accelerator = Accelerator()

# Load the dataset
dataset = load_dataset("imdb", split="train[:2000]")  # Using a small subset for demonstration
eval_dataset = load_dataset("imdb", split="test[2000:2500]")  # Subset for quick evaluation

# Load the model and tokenizer
model_name = "distilbert-base-uncased"
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Tokenize the dataset
def tokenize(batch):
    return tokenizer(batch["text"], padding=True, truncation=True)

tokenized_dataset = dataset.map(tokenize, batched=True)
tokenized_eval_dataset = eval_dataset.map(tokenize, batched=True)

# Define training arguments with DeepSpeed config
training_args = TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=80, # Match DeepSpeed config
    num_train_epochs=1,
    evaluation_strategy="epoch",
    learning_rate=0.00015,  # Match DeepSpeed config
    weight_decay=0.01,  # Match DeepSpeed config
    fp16=True,  # Match DeepSpeed config
    report_to="none"
)

# Define the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    eval_dataset=tokenized_eval_dataset
)

# Prepare model and data with Accelerate
model, tokenized_dataset = accelerator.prepare(model, tokenized_dataset)

# Start training
trainer.train()
