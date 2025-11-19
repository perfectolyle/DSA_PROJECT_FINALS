import os
import json, sys
from storage import bookmarks, history
from bible import navigation, search, verse_of_the_day
from utils import ascii_art

# --- Clear screen function ---
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- Load Bible Data ---
try:
    with open("data/KJV.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    books = data["books"]
    print("✅ Bible data loaded successfully.")
except Exception as e:
    print(f"FATAL ERROR: {e}")
    sys.exit(1)

# --- Help/Guidelines ---
def show_help():
    clear_screen()
    print("\n=== HELP / GUIDELINES ===\n")
    print("📖 Navigate the Bible by choosing book, chapter, and verse.")
    print("🔍 Search for any keyword using the KMP-powered search.")
    print("📌 Bookmark verses to quickly revisit them later.")
    print("📜 View your search history to track past searches.")
    print("➡ Navigation hints:")
    print("   - Enter numbers for menu or book/chapter/verse selection.")
    print("   - [N] = Next page, [B] = Back page, [Q] = Quit to menu.")
    print("\nPress Enter or Any key to return to main menu.")
    input()

# --- Main Program Loop ---
def main():
    clear_screen()
    print("⏳ Loading user data...")
    bookmarks.load_bookmarks()
    history.load_history()
    ascii_art.display_ascii_art()
    
    while True:
        print("\n=== 📖 Terminal Bible App ===\n")
        print("1. 📖  Open a Book, Chapter & Verse")
        print("2. 🔍  Search for a Verse")
        print("3. 📌  Verse of the Day")
        print("4. 📜  Show Search History")
        print("5. 📑  Show Bookmarks")
        print("6. 🗑️   Delete a Bookmark")
        print("7. 📚  Help / Guidelines")
        print("8. 🚪  Quit\n")
        
        choice = input("Enter your choice (1-8): ").strip()
        clear_screen()
        
        if choice=="1":
            navigation.list_books(books)
            b = input("\n➡ Enter book number: ")
            if not b.isdigit(): print("❌ Invalid input! Try again."); continue
            bi=int(b)-1
            if not (0<=bi<len(books)): print("❌ Book out of range! Try again."); continue
            book=books[bi]
            print(f"✅ Selected: {book['name']} ({len(book['chapters'])} chapters)")
            c=input(f"\n➡ Enter chapter number (1-{len(book['chapters'])}): ")
            if not c.isdigit(): print("❌ Invalid input! Try again."); continue
            ci=int(c)-1
            if not (0<=ci<len(book['chapters'])): print("❌ Chapter out of range! Try again."); continue
            chap=book['chapters'][ci]
            print(f"✅ Selected Chapter: {chap['chapter']} ({len(chap['verses'])} verses)")
            v=input(f"\n➡ Enter verse number (1-{len(chap['verses'])}): ")
            if not v.isdigit(): print("❌ Invalid input! Try again."); continue
            vi=int(v)-1
            ref, text=navigation.show_verse(books, bi, ci, vi)
            if ref and text:
                y=input("\n📌 Bookmark this verse? (y/n): ").lower()
                if y=='y': bookmarks.add_bookmark(ref,text)
                elif y=='n': pass
                else: print("❌ Invalid choice! Returning to main menu.")
        
        elif choice=="2":
            kw=input("🔍 Enter a word or phrase to search: ").strip()
            if kw: search.search_verse(books,kw)
        
        elif choice=="3":
            verse_of_the_day.verse_of_the_day(books)
        
        elif choice=="4":
            history.show_history()
        
        elif choice=="5":
            bookmarks.show_bookmarks()
        
        elif choice=="6":
            bookmarks.delete_bookmark()
        
        elif choice=="7":
            show_help()
        
        elif choice=="8":
            history.save_history()
            print("\n👋 Exiting program. God bless!\n")
            break
        
        else:
            print("❌ Invalid choice! Please select between 1-8.")
        
        print("\n" + "-"*50 + "\n")


main()
