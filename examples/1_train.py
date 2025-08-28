# 1_train.py
from accelerate import Accelerator
import torch
from torch.utils.data import DataLoader, TensorDataset

def main():
    # Initialize the accelerator
    accelerator = Accelerator()

    # Log device setup
    print(f"Accelerator initialized on device: {accelerator.device}")

    # Example data
    data = torch.randn(1000, 10)
    labels = torch.randint(0, 2, (1000,))
    dataset = TensorDataset(data, labels)
    dataloader = DataLoader(dataset, batch_size=32)

    # Model and optimizer
    model = torch.nn.Linear(10, 2)
    optimizer = torch.optim.Adam(model.parameters())

    # Place model, optimizer, and dataloader on the appropriate device
    model, optimizer, dataloader = accelerator.prepare(model, optimizer, dataloader)

    # Example training loop
    print("Starting training loop...")
    for batch_idx, batch in enumerate(dataloader):
        optimizer.zero_grad()
        inputs, targets = batch
        outputs = model(inputs)
        loss = torch.nn.functional.cross_entropy(outputs, targets)
        accelerator.backward(loss)
        optimizer.step()

        # Print loss every 10 batches
        if batch_idx % 10 == 0:
            print(f"Batch {batch_idx}, Loss: {loss.item()}")

    print("Training completed!")

if __name__ == "__main__":
    main()
