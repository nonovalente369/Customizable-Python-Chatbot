## 👥 Team & Acknowledgements

This project was developed in collaboration with:

* **Dyari Karim**
    * GitHub: https://github.com/nonovalente369
    * Role: Responsible for designing and implementing the deep learning model (PyTorch), the NLP data pipeline (NLTK utilities), and managing the training process.


* **Ceyhun Bozkurt**
    * GitHub: https://github.com/ceybozz
    * Role: Lead developer for the administrative interface, intent management


# 🤖 Self-Learning Python Chatbot

This is a customizable, self-learning AI chatbot built with Python and PyTorch. Unlike standard bots that are "fixed," you can teach this bot new topics, update its existing knowledge, or delete things it shouldn't know—all while chatting.

## ⚠️ Requirements

* **Python 3.10** (Recommended)
* Basic familiarity with the terminal/command prompt

---

## 🚀 How It Works

### 1. Start Up
When you launch the chatbot, it reviews its learned database (`intents.json`) to ensure its memory is up to date. Then, it greets you with a welcome message.

### 2. Processing (The Brain)
When you **type** a sentence and press Enter, the bot instantly analyzes it. It ignores punctuation, breaks your sentence into key words, and simplifies them (e.g., it knows that "running" and "run" mean the same thing).

### 3. Thinking & Answering
The bot compares your text against its learned database:
* **Confident (>90%):** It understands the topic and prints the correct response immediately.
* **Unsure:** It admits it doesn't understand ("I don't understand that yet") and automatically switches to **Learning Mode**.

### 4. 🎓 Learning Mode
Instead of giving up, the bot asks for your help to get smarter. It will ask you to input:
1.  **The Topic:** What is this conversation about? (e.g., "SpaceX")
2.  **The Patterns:** How might you ask about this? (e.g., "Tell me about rockets")
3.  **The Response:** What should it reply? (e.g., "SpaceX designs rockets.")

### 5. Auto-Update
Once you provide the info, the bot:
* Saves the new knowledge to memory.
* Retrains the model instantly.
* Restarts the conversation automatically so you can test the new knowledge immediately.

---

## 🛠️ Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/nonovalente369/Custom-Python-Chatbot.git](https://github.com/nonovalente369/Custom-Python-Chatbot.git)
    cd Custom-Python-Chatbot
    ```

2.  **Install Dependencies**
    ```bash
    # Windows
    py -3.10 -m pip install -r requirements.txt
    
    # Mac/Linux
    pip3 install -r requirements.txt
    ```

3.  **Run the Bot**
    ```bash
    # Windows
    py -3.10 chat.py
    
    # Mac/Linux
    python3 chat.py
    ```
