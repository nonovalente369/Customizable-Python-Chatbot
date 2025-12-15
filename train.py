import json
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from nltk_utils import tokenize, stem, bag_of_words
from model import NeuralNet

class TextClassificationDataset(Dataset):
    """Custom PyTorch Dataset for the chatbot"""
    def __init__(self, X_train, y_train):
        self.n_samples = len(X_train)
        self.x_data = X_train
        self.y_data = y_train

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.n_samples

def train():
    """
    Loads intents, processes NLP data, trains the Neural Network, 
    and saves the model state to 'data.pth'.
    """
    # --- Config ---
    BATCH_SIZE      = 8
    HIDDEN_SIZE     = 8
    LEARNING_RATE   = 0.001
    NUM_EPOCHS      = 1000
    INTENTS_FILE    = 'intents.json'
    SAVE_FILE       = 'data.pth'
    
    # 1. Load Data
    try:
        with open(INTENTS_FILE, 'r') as f:
            intents = json.load(f)
    except FileNotFoundError:
        print(f"[Error] Could not find {INTENTS_FILE}. Please ensure it exists.")
        return

    # 2. NLP Preprocessing
    all_words   = []
    tags        = []
    xy          = []

    for intent in intents['intents']:
        tag = intent['tag']
        tags.append(tag)
        for pattern in intent['patterns']:
            w = tokenize(pattern)
            all_words.extend(w)
            xy.append((w, tag))

    # Filter out punctuation and stem words (e.g., "running" -> "run")
    ignore_words    = ['?', '!', '.', ',']
    all_words       = [stem(w) for w in all_words if w not in ignore_words]
    all_words       = sorted(set(all_words))
    tags            = sorted(set(tags))

    # 3. Create Training Data
    X_train = []
    y_train = []

    for (pattern_sentence, tag) in xy:
        bag = bag_of_words(pattern_sentence, all_words)
        X_train.append(bag)
        label = tags.index(tag)
        y_train.append(label)

    X_train = np.array(X_train)
    y_train = np.array(y_train)

    # 4. PyTorch Setup
    input_size      = len(X_train[0])
    output_size     = len(tags)
    device          = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    dataset         = TextClassificationDataset(X_train, y_train)
    train_loader    = DataLoader(dataset=dataset, batch_size=BATCH_SIZE, shuffle=True, num_workers=0)
    
    # Set up the Brain
    model       = NeuralNet(input_size, HIDDEN_SIZE, output_size).to(device)
    criterion   = nn.CrossEntropyLoss()
    optimizer   = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)

    # 5. Training Loop
    for epoch in range(NUM_EPOCHS):
        for (words, labels) in train_loader:
            words   = words.to(device)
            labels  = labels.to(device).long()

            # Forward pass
            outputs = model(words)
            loss    = criterion(outputs, labels)

            # Backward and optimize
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

    # 6. Save Model
    data = {
        "model_state": model.state_dict(),
        "input_size": input_size,
        "hidden_size": HIDDEN_SIZE,
        "output_size": output_size,
        "all_words": all_words,
        "tags": tags
    }

    torch.save(data, SAVE_FILE)
    print(f'Training complete. Model saved to {SAVE_FILE}')