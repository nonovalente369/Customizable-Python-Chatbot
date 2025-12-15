from intent_manager import IntentManager
from utils import print_slow, get_multi_line_input

def manage_intents(intents_file='intents.json'):
    manager = IntentManager(intents_file)
    
    print("\n" + "="*40)
    print("      TEACHING MODE ACTIVATED")
    print("="*40)
    
    while True:
        print("\nWhat would you like to do?")
        print("1. ADD a completely new Topic")
        print("2. UPDATE an existing Topic (Add words/replies)")
        print("3. DELETE a Topic")
        print("4. Cancel & Return to Chat")
        
        choice = input("\nSelect (1-4): ").strip()
        
        # --- OPTION 1: ADD NEW ---
        if choice == '1':
            tag = input("\nStep 1: What is the TOPIC tag? (e.g. 'sports'): ").strip()
            
            if not tag: continue
            
            patterns    = get_multi_line_input("Step 2: What questions triggers this?", "phrase")
            responses   = get_multi_line_input("Step 3: How should I answer?", "response")
            
            manager.add_intent(tag, patterns, responses)
            print_slow("\n[New topic saved! Rebooting...]")
            return True

        # --- OPTION 2: UPDATE EXISTING ---
        elif choice == '2':
            current_tags = manager.get_all_tags()
            print(f"\nAvailable Topics: {', '.join(current_tags)}")
            tag = input("Which topic do you want to update?: ").strip()
            
            if tag not in current_tags:
                print(f"[!] Topic '{tag}' not found.")
                continue
                
            print(f"\nUpdating '{tag}':")
            print("a. Add more trigger phrases")
            print("b. Add more responses")
            sub_choice = input("Select (a/b): ").strip().lower()
            
            if sub_choice == 'a':
                new_patterns = get_multi_line_input(f"Add phrases for '{tag}'", "phrase")
                manager.add_patterns_to_tag(tag, new_patterns)
                print_slow("\n[Knowledge updated! Rebooting...]")
                return True
            
            elif sub_choice == 'b':
                new_responses = get_multi_line_input(f"Add responses for '{tag}'", "response")
                manager.add_responses_to_tag(tag, new_responses)
                print_slow("\n[Knowledge updated! Rebooting...]")
                return True

        # --- OPTION 3: DELETE ---
        elif choice == '3':
            current_tags = manager.get_all_tags()
            print(f"\nAvailable Topics: {', '.join(current_tags)}")
            
            tag     = input("Which topic do you want to DELETE?: ").strip()
            confirm = input(f"Are you sure you want to delete '{tag}'? (y/n): ").lower()
            
            if confirm == 'y':
                if manager.delete_intent(tag):
                    print_slow(f"\n[Topic '{tag}' deleted. Rebooting...]")
                    return True
                else:
                    print(f"[!] Could not find tag '{tag}'.")
            else:
                print("[Deletion cancelled]")

        # --- OPTION 4: CANCEL ---
        elif choice == '4':
            return False
        
        else:
            print("[!] Invalid choice.")