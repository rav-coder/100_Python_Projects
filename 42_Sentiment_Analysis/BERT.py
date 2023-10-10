"""
Reference:
    https://github.com/LinkedInLearning/transformers-text-classification-for-nlp-using-bert-2478096/blob/main/IMDB_text_classification.ipynb
"""

import torch
from torch import nn, optim
from torch.utils.data import Dataset, DataLoader
from sklearn.metrics import confusion_matrix, f1_score, accuracy_score
from transformers import BertTokenizer, BertForSequenceClassification
from datasets import load_dataset


# Define the SentimentDataset class
class SentimentDataset(Dataset):
    def __init__(self, reviews, targets, tokenizer, max_length):
        self.reviews = reviews
        self.targets = targets
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.reviews)

    def __getitem__(self, index):
        review = str(self.reviews[index])
        target = self.targets[index]

        encoding = self.tokenizer.encode_plus(
            review,
            add_special_tokens=True,
            max_length=self.max_length,
            return_token_type_ids=False,
            padding='max_length',
            truncation=True,
            return_attention_mask=True,
            return_tensors='pt'
        )

        return {
            'input_ids': encoding['input_ids'].flatten(),
            'attention_mask': encoding['attention_mask'].flatten(),
            'target': torch.tensor(target, dtype=torch.long)
        }


# Define the custom collate function for DataLoader
def custom_collate(batch):
    input_ids = torch.stack([item['input_ids'] for item in batch])
    attention_mask = torch.stack([item['attention_mask'] for item in batch])
    targets = torch.stack([item['target'] for item in batch])
    return {
        'input_ids': input_ids,
        'attention_mask': attention_mask,
        'target': targets
    }


# Function to train a single epoch
def train_epoch(model, data_loader, optimizer, device):
    model.train()
    total_loss = 0
    for batch in data_loader:
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        targets = batch['target'].to(device)

        optimizer.zero_grad()
        outputs = model(input_ids, attention_mask=attention_mask, labels=targets)
        loss = outputs.loss
        total_loss += loss.item()

        loss.backward()
        optimizer.step()

    return total_loss / len(data_loader)


# Function to evaluate the model
def evaluate_model(model, data_loader, device):
    model.eval()
    y_pred = []
    y_true = []

    with torch.no_grad():
        for batch in data_loader:
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            targets = batch['target'].to(device)

            outputs = model(input_ids, attention_mask=attention_mask)
            _, predicted = torch.max(outputs.logits, dim=1)

            y_pred.extend(predicted.tolist())
            y_true.extend(targets.tolist())

    return y_pred, y_true


# Set the device (GPU or CPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the BERT tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Load the IMDb dataset
imdb_dataset = load_dataset("imdb")

# Get the reviews and targets from the IMDb dataset
reviews = imdb_dataset["train"]["text"]
targets = imdb_dataset["train"]["label"]

# Split the dataset into training and test sets
train_reviews = reviews[:25000]
train_targets = targets[:25000]
test_reviews = reviews[25000:50000]
test_targets = targets[25000:50000]

# Create the training dataset
train_dataset = SentimentDataset(train_reviews, train_targets, tokenizer, max_length=512)

# Create the test dataset
test_dataset = SentimentDataset(test_reviews, test_targets, tokenizer, max_length=512)

# Create the data loaders
batch_size = 8
train_loader = DataLoader(
    train_dataset,
    batch_size=batch_size,
    shuffle=True,
    collate_fn=custom_collate
)

test_loader = DataLoader(
    test_dataset,
    batch_size=batch_size,
    shuffle=False,
    collate_fn=custom_collate
)

# Initialize the BERT model for sequence classification
model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2).to(device)

# Define the optimizer and learning rate
optimizer = optim.AdamW(model.parameters(), lr=2e-5)

# Training loop
num_epochs = 5
for epoch in range(num_epochs):
    train_loss = train_epoch(model, train_loader, optimizer, device)
    train_y_pred, train_y_true = evaluate_model(model, train_loader, device)
    test_y_pred, test_y_true = evaluate_model(model, test_loader, device)

    train_accuracy = accuracy_score(train_y_true, train_y_pred)
    test_accuracy = accuracy_score(test_y_true, test_y_pred)
    train_f1 = f1_score(train_y_true, train_y_pred)
    test_f1 = f1_score(test_y_true, test_y_pred)
    train_cm = confusion_matrix(train_y_true, train_y_pred)
    test_cm = confusion_matrix(test_y_true, test_y_pred)

    print(f"Epoch {epoch + 1}/{num_epochs}")
    print(f"Train Loss: {train_loss:.4f} - Train Accuracy: {train_accuracy:.4f} - Train F1: {train_f1:.4f}")
    print(f"Test Accuracy: {test_accuracy:.4f} - Test F1: {test_f1:.4f}")
