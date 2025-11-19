import datetime
import random

def verse_of_the_day(books):
    if not books: return
    today = datetime.date.today()
    random.seed(today.toordinal())
    book = random.choice(books)
    chapter = random.choice(book["chapters"])
    verse = random.choice(chapter["verses"])
    print(f"\n📖 Verse of the Day: {book['name']} {chapter['chapter']}:{verse['verse']}")
    print(verse["text"])
