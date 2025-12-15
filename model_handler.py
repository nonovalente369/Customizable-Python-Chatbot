import torch
from model import NeuralNet

def load_model_data(file):
    """Loads the saved data dictionary"""
    data = torch.load(file)
    return data['input_size'], data['hidden_size'], data['output_size'], data['all_words'], data['tags'], data['model_state']

def init_model(input_size, hidden_size, output_size, model_state):
    """Creates the neural net and loads weights"""
    device  = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model   = NeuralNet(input_size, hidden_size, output_size).to(device)
    model.load_state_dict(model_state)
    model.eval()
    return model, device