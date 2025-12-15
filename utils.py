import sys
import time

def print_slow(text):
    """Effect to print text like a typewriter"""
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)
    print()

def get_multi_line_input(prompt_text, item_name):
    """Helper to ask the user for multiple inputs comfortably"""
    items = []
    print(f"\n--- {prompt_text} ---")
    print(f"(Type a {item_name} and press Enter. Press Enter again when you are done)")
    
    while True:
        user_input = input(f"> ").strip()
        if user_input == "":
            if len(items) == 0:
                print(f"   [!] You must add at least one {item_name}.")
                continue
            break
        items.append(user_input)
    return items