import json
import os
from constants import BOOKMARK_FILE

bookmarks = {}

def save_bookmarks():
    try:
        with open(BOOKMARK_FILE, "w", encoding="utf-8") as f:
            json.dump(bookmarks, f, indent=4)
    except Exception as e:
        print(f"❌ Error saving bookmarks: {e}")

def load_bookmarks():
    global bookmarks
    if not os.path.exists(BOOKMARK_FILE):
        return
    try:
        with open(BOOKMARK_FILE, "r", encoding="utf-8") as f:
            loaded_data = json.load(f)
            if isinstance(loaded_data, dict):
                bookmarks.update(loaded_data)
            else:
                print(f"❌ Bookmark file corrupted: Data in {BOOKMARK_FILE} is not a dictionary.")
    except json.JSONDecodeError:
        print(f"❌ Error decoding JSON from {BOOKMARK_FILE}. File may be corrupted.")
    except Exception as e:
        print(f"❌ Error loading bookmarks: {e}")

def add_bookmark(ref, verse_text):
    bookmarks[ref] = verse_text
    save_bookmarks()
    print(f"✅ Bookmarked {ref}!")

def show_bookmarks():
    print("\n📌 Bookmarked Verses:")
    if not bookmarks:
        print("No bookmarks yet.")
        return
    for ref, verse_text in bookmarks.items():
        print(f"| {ref} - {verse_text[:100]}{'...' if len(verse_text) > 100 else ''}")

def delete_bookmark():
    if not bookmarks:
        print("❌ No bookmarks to delete.")
        return
    print("\n📌 Bookmarked Verses (Select a number to delete):")
    for i, ref in enumerate(bookmarks.keys(), start=1):
        print(f"{i}. {ref}")
    choice = input("\nEnter the number of the bookmark to delete: ")
    if not choice.isdigit():
        print("❌ Invalid input!")
        return
    choice = int(choice)
    if not (1 <= choice <= len(bookmarks)):
        print("❌ Bookmark number out of range!")
        return
    ref_to_delete = list(bookmarks.keys())[choice - 1]
    del bookmarks[ref_to_delete]
    save_bookmarks()
    print(f"🗑️ Deleted bookmark: {ref_to_delete}")