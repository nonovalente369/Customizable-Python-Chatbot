import json

class IntentManager:
    def __init__(self, intents_file):
        self.intents_file   = intents_file
        self.intents        = self.load_intents()

    def load_intents(self):
        try:
            with open(self.intents_file, 'r') as f:
                return json.load(f)['intents']
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_intents(self):
        data = {"intents": self.intents}
        with open(self.intents_file, 'w') as f:
            json.dump(data, f, indent=4)

    def get_all_tags(self):
        return [intent['tag'] for intent in self.intents]

    def add_intent(self, tag, patterns, responses):
        # Check if tag already exists, if so, just update it
        for intent in self.intents:
            if intent['tag'] == tag:
                intent['patterns'].extend(patterns)
                intent['responses'].extend(responses)
                self.save_intents()
                return
        
        # Otherwise create new
        new_intent = {
            "tag": tag,
            "patterns": patterns,
            "responses": responses
        }
        self.intents.append(new_intent)
        self.save_intents()

    def delete_intent(self, tag):
        # Keep only intents that DO NOT match the tag
        initial_count   = len(self.intents)
        self.intents    = [i for i in self.intents if i['tag'] != tag]
        
        if len(self.intents) < initial_count:
            self.save_intents()
            return True
        return False

    def add_patterns_to_tag(self, tag, new_patterns):
        for intent in self.intents:
            if intent['tag'] == tag:
                intent['patterns'].extend(new_patterns)
                self.save_intents()
                return True
        return False

    def add_responses_to_tag(self, tag, new_responses):
        for intent in self.intents:
            if intent['tag'] == tag:
                intent['responses'].extend(new_responses)
                self.save_intents()
                return True
        return False