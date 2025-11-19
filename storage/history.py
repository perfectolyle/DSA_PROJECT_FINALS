import json
import os
from collections import deque
from constants import HISTORY_FILE

search_history = deque(maxlen=10)

def save_history():
    try:
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(list(search_history), f, indent=4)
    except Exception as e:
        print(f"❌ Error saving history: {e}")

def load_history():
    global search_history
    if not os.path.exists(HISTORY_FILE):
        return
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            history_list = json.load(f)
            if isinstance(history_list, list):
                search_history.extend(history_list)
            else:
                print(f"❌ History file corrupted: Data in {HISTORY_FILE} is not a list.")
    except json.JSONDecodeError:
        print(f"❌ Error decoding JSON from {HISTORY_FILE}. File may be corrupted.")
    except Exception as e:
        print(f"❌ Error loading history: {e}")

def add_to_history(keyword):
    search_history.append(keyword)

def show_history():
    print("\n📜 Search History:")
    if not search_history:
        print("No searches yet.")
    else:
        for i, keyword in enumerate(reversed(search_history), start=1):
            print(f"{i}. {keyword}")