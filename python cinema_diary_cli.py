# cinema_diary_cli.py
# CLI app to manage Rishi's Cinema Diary

import json
import os

DIARY_FILE = "cinema_diary.json"

def load_diary():
    if os.path.exists(DIARY_FILE):
        with open(DIARY_FILE, 'r') as f:
            return json.load(f)
    return []

def save_diary(entries):
    with open(DIARY_FILE, 'w') as f:
        json.dump(entries, f, indent=2)

def add_entry():
    print("\n🎬 Add a New Movie Entry")
    title = input("Movie Title: ")
    language = input("Language: ")
    comment = input("What did you feel about it?: ")
    platform = input("Where did you watch it?: ")
    
    entry = {
        "title": title,
        "language": language,
        "comment": comment,
        "platform": platform
    }
    
    diary = load_diary()
    diary.append(entry)
    save_diary(diary)
    print("✅ Movie added to your diary!")

def view_diary():
    diary = load_diary()
    if not diary:
        print("\n📭 No entries found.")
        return

    print("\n📖 Your Cinema Diary:")
    for i, entry in enumerate(diary, 1):
        print(f"\n{i}. {entry['title']} ({entry['language']})")
        print(f"   Watched on: {entry['platform']}")
        print(f"   Thoughts: {entry['comment']}")

def main():
    while True:
        print("\n🎥 Welcome to Rishi's Cinema Diary CLI")
        print("1. Add new movie")
        print("2. View diary")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ")
        
        if choice == '1':
            add_entry()
        elif choice == '2':
            view_diary()
        elif choice == '3':
            print("👋 Goodbye, boss! Keep watching great cinema.")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()