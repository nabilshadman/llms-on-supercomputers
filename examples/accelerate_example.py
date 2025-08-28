from transformers import AutoModelForSequenceClassification, AutoTokenizer, Trainer, TrainingArguments
from datasets import load_dataset
from accelerate import Accelerator
import torch

def main():
    # Initialize Accelerator
    accelerator = Accelerator()
    
    # Load dataset
    dataset = load_dataset("ag_news")
    
    # Load model and tokenizer
    model_name = "distilbert-base-uncased"
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=4)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    # Tokenize dataset
    def tokenize(batch):
        return tokenizer(batch["text"], padding=True, truncation=True)

    tokenized_dataset = dataset.map(tokenize, batched=True)
    tokenized_dataset = tokenized_dataset.rename_column("label", "labels")
    tokenized_dataset.set_format("torch", columns=["input_ids", "attention_mask", "labels"])
    
    # Prepare data loaders
    train_dataloader = torch.utils.data.DataLoader(tokenized_dataset["train"], batch_size=8, shuffle=True)
    eval_dataloader = torch.utils.data.DataLoader(tokenized_dataset["test"], batch_size=8)

    # Prepare optimizer and learning rate scheduler
    optimizer = torch.optim.AdamW(model.parameters(), lr=5e-5)

    # Prepare everything using accelerator
    model, optimizer, train_dataloader, eval_dataloader = accelerator.prepare(
        model, optimizer, train_dataloader, eval_dataloader
    )

    # Training loop
    model.train()
    for epoch in range(3):
        for batch in train_dataloader:
            optimizer.zero_grad()
            outputs = model(**batch)
            loss = outputs.loss
            accelerator.backward(loss)
            optimizer.step()

    print("Training completed!")

if __name__ == "__main__":
    main()
