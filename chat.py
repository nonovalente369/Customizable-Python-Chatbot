import random
import json
import torch
import nltk
from nltk_utils import bag_of_words, tokenize
from train import train

# --- NEW IMPORTS FROM OUR CUSTOM FILES ---
from utils import print_slow
from model_handler import load_model_data, init_model
from admin import manage_intents

# Ensure this is downloaded (Uncomment if running on a new PC)
# nltk.download('punkt_tab')

def chat_loop(model, device, all_words, tags, intents, bot_name):
    print("\n" + "*"*50)
    print(f"  System Online. You are speaking with {bot_name}.")
    print("  Commands: 'quit' to exit | 'admin' to edit brain | 'help' for info")
    print("*"*50 + "\n")
    
    while True:
        sentence = input("You: ")
        
        # --- COMMAND HANDLING ---
        if sentence.lower() == "quit":
            return False
        
        elif sentence.lower() == "help":
            print("\n" + "-"*30)
            print("      SYSTEM COMMANDS")
            print("-" * 30)
            print("1. 'admin' -> Enter Teaching Mode (Add/Edit/Delete topics)")
            print("2. 'quit'  -> Exit the program")
            print("3. 'help'  -> Show this menu")
            print("-" * 30 + "\n")
            continue

        elif sentence.lower() == "admin":
            if manage_intents():
                return True
            continue

        # --- NORMAL CHAT ---
        sentence_tokenized = tokenize(sentence)
        X = bag_of_words(sentence_tokenized, all_words)
        X = torch.from_numpy(X).to(device).float().reshape(1, -1)

        with torch.no_grad():
            output = model(X)
        
        _, predicted    = torch.max(output, dim=1)
        tag             = tags[predicted.item()]
        probs           = torch.softmax(output, dim=1)
        prob            = probs[0][predicted.item()]

        if prob.item() > 0.90:
            for intent in intents['intents']:
                if tag == intent['tag']:
                    print(f"{bot_name}: {random.choice(intent['responses'])}")
                    break
        else:
            print(f"{bot_name}: I'm sorry, I don't understand that yet.")
            print_slow(f"{bot_name}: Would you like to enter Teaching Mode? (y/n)")
            
            choice = input("> ").lower()
            if choice == 'y':
                if manage_intents():
                    return True 
            else:
                print(f"{bot_name}: Okay, let's talk about something else.")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    bot_name = "Chatbot"
    
    print("Checking memory...")
    try:
        train()
    except Exception as e:
        print(f"Initial setup failed: {e}")

    while True:
        try:
            # Load Data
            file_path = "data.pth"
            input_size, hidden_size, output_size, all_words, tags, model_state = load_model_data(file_path)
            model, device = init_model(input_size, hidden_size, output_size, model_state)
            
            # Load Intents
            with open('intents.json') as json_data:
                intents = json.load(json_data)

            # Start Chat
            restart_needed = chat_loop(model, device, all_words, tags, intents, bot_name)
            
            if restart_needed:
                print("\n" + "="*30)
                print("   LEARNING NEW DATA... PLEASE WAIT")
                print("="*30)
                train() 
                print_slow("...Update Complete. Rebooting Conversation...\n")
            else:
                print_slow("Shutting down... Goodbye!")
                break
        
        except FileNotFoundError:
            print("\n[Error] Could not find 'data.pth'. Please ensure training completed successfully.")
            break