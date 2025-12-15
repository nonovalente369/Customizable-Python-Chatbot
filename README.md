# 🤖 Self-Learning Voice Chatbot

This is a customizable, self-learning AI chatbot built with Python and PyTorch. Unlike standard bots that are "fixed," you can teach this bot new topics, update its existing knowledge, or delete things it shouldn't know—all while chatting.

## 🚀 How It Works

### 1. Start Up
When you launch the chatbot, it takes a moment to "wake up" and reviews everything it knows to ensure its memory is up to date. Then, it greets you via voice.

### 2. Processing (The Brain)
When you speak or type a sentence, the bot instantly analyzes it. It ignores punctuation, breaks your sentence into key words, and simplifies them (e.g., it knows that "running" and "run" mean the same thing).

### 3. Thinking & Answering
The bot compares your words against its learned database:
* **Confident (>90%):** It understands the topic and replies with a voice response.
* **Unsure:** It admits it doesn't understand ("I don't understand that yet") and automatically switches to **Learning Mode**.

### 4. 🎓 Learning Mode
Instead of giving up, the bot asks for your help to get smarter. It will ask for:
1.  **The Topic:** What is this conversation about? (e.g., "SpaceX")
2.  **The Patterns:** How might you ask about this? (e.g., "Tell me about rockets")
3.  **The Response:** What should it say back? (e.g., "SpaceX designs rockets.")

### 5. Auto-Update
Once you provide the info, the bot:
* Saves the new knowledge to memory.
* Retrains the model instantly.
* Restarts the conversation automatically so you can test the new knowledge immediately.
