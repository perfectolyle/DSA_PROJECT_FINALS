from storage.bookmarks import add_bookmark
from storage.history import add_to_history

def list_books(books):
    print("\n=== LIST OF BIBLE BOOKS ===\n")
    columns = 3


    # Split books into rows of col_height
    rows = (len(books) + columns - 1) // columns  # Total rows needed

    # Create a 2D list for display
    table = []
    for r in range(rows):
        row = []
        for c in range(columns):
            idx = r + c * rows
            if idx < len(books):
                row.append(f"{idx+1}. {books[idx]['name']}")
            else:
                row.append("")  # Empty string for missing items
        table.append(row)

    print("\n📖 Available Bible Books:\n")
    # Print each row
    for row in table:
        print(" | ".join(f"{item:<25}" for item in row))
    print("\n")
    

def show_verse(books, book_index, chapter_index, verse_index):
    book = books[book_index]
    chapter = book["chapters"][chapter_index]
    verses = chapter["verses"]
    if not (0 <= verse_index < len(verses)):
        print("❌ Verse out of range!")
        return None, None
    verse = verses[verse_index]
    ref = f"{book['name']} {chapter['chapter']}:{verse['verse']}"
    print(f"\n📖 {ref} - {verse['text']}")
    return ref, verse['text']
