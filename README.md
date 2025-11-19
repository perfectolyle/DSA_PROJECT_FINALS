# 📖 Terminal Bible App

A feature-rich, command-line Bible application built with Python that allows users to navigate the King James Version (KJV) Bible, search verses using advanced algorithms, bookmark favorite passages, and more.

## ✨ Features

- **📚 Bible Navigation** - Browse all 66 books, 1,189 chapters, and 31,102 verses
- **🔍 Advanced Search** - KMP (Knuth-Morris-Pratt) algorithm for fast verse searching
- **📌 Bookmarks** - Save and manage your favorite verses
- **📜 Search History** - Track your last 10 searches
- **🌅 Verse of the Day** - Daily random verse (consistent throughout the day)
- **📚 Help System** - In-app guidelines and navigation tips
- **💾 Data Persistence** - Your bookmarks and history are saved between sessions

## 🚀 Quick Start

### Running on Replit

1. Click the **Run** button at the top of the page
2. The app will start in the Console tab
3. Follow the on-screen menu to navigate

### Running Locally

```bash
python home.py
```

**Requirements:** Python 3.11+ (No external dependencies needed)

## 📖 How to Use

### Main Menu

When you start the app, you'll see 8 options:

```
=== 📖 Terminal Bible App ===

1. 📖  Open a Book, Chapter & Verse
2. 🔍  Search for a Verse
3. 📌  Verse of the Day
4. 📜  Show Search History
5. 📑  Show Bookmarks
6. 🗑️   Delete a Bookmark
7. 📚  Help / Guidelines
8. 🚪  Quit
```

### Examples

**Navigate to a Verse:**
```
Choose option 1
→ Enter book number: 19 (Psalms)
→ Enter chapter: 23
→ Enter verse: 1
→ Output: "The LORD is my shepherd; I shall not want."
```

**Search for Verses:**
```
Choose option 2
→ Enter search term: "love"
→ Results: 310 verses containing "love" (paginated)
```

**Bookmark a Verse:**
- After viewing any verse, you'll be asked: "Bookmark this verse? (y/n)"
- Press `y` to save it to your bookmarks

**View Verse of the Day:**
```
Choose option 3
→ See a random verse (same verse all day for everyone)
```

## 🏗️ Technical Architecture

### Data Structures

- **Hierarchical Tree** - Bible organized as Books → Chapters → Verses
- **Hash Table** - Fast O(1) bookmark storage and retrieval
- **Queue** - FIFO search history with automatic size limiting (max 10)
- **Arrays** - Efficient verse storage and random access

### Algorithms

- **KMP String Matching** - O(n+m) time complexity for verse searching
- **Date-Seeded Random** - Deterministic verse of the day selection
- **LPS Array Preprocessing** - Pattern matching optimization

### Project Structure

```
.
├── home.py                 # Main application entry point
├── constants.py            # Configuration constants
├── bible/
│   ├── navigation.py       # Book/chapter/verse navigation
│   ├── search.py           # KMP search algorithm
│   └── verse_of_the_day.py # Daily verse feature
├── storage/
│   ├── bookmarks.py        # Bookmark management
│   └── history.py          # Search history tracking
├── utils/
│   └── ascii_art.py        # ASCII art display
└── data/
    └── KJV.json            # King James Version Bible data
```

## 💾 Data Storage

User data is automatically saved to JSON files:

- `bookmarks.json` - Your saved verses
- `history.json` - Your recent searches (last 10)

These files are created automatically and persist between sessions.

## 🎯 Key Highlights

### Performance
- Searches through 31,102 verses in < 1 second
- KMP algorithm avoids redundant comparisons
- Efficient memory usage with bounded history

### User Experience
- Clean, intuitive menu system
- Input validation prevents errors
- Helpful error messages
- Pagination for long search results

### Code Quality
- Modular design for maintainability
- Well-commented code
- Error handling and data validation
- Separation of concerns

## 🛠️ Dependencies

**None!** This app uses only Python's standard library:
- `json` - Data storage
- `os` - System operations
- `sys` - System parameters
- `datetime` - Date handling
- `random` - Random selection
- `collections` - Deque for history

## 📚 Bible Data

- **Translation:** King James Version (KJV)
- **Books:** 66 (39 Old Testament, 27 New Testament)
- **Chapters:** 1,189
- **Verses:** 31,102
- **Format:** JSON with hierarchical structure

## 🔍 Search Features

### KMP Algorithm Benefits
- **Fast:** O(n+m) instead of O(n×m)
- **Smart:** Preprocesses pattern to avoid redundant checks
- **Accurate:** Case-insensitive matching
- **Scalable:** Efficient even with 31,000+ verses

### Search Navigation
- View 10 results per page
- `[N]` - Next page
- `[B]` - Previous page
- `[F]` - First page
- `[Q]` - Quit to menu

## 🎓 Educational Value

This project demonstrates practical applications of:

- String matching algorithms (KMP)
- Tree data structures (hierarchical organization)
- Hash tables (key-value storage)
- Queues (FIFO ordering)
- File I/O and data persistence
- Algorithm time complexity optimization
- Modular software design

## 🤝 Contributing

This is a student project for a Data Structures and Algorithms course. 

**Group Members:**
- Perfecto S. Gardoce lll
- Maynard L. Villar 
- Mel G. Magdaraog
- Rancel Joy A. Cuervo

## 📄 License

This project is created for educational purposes.

Bible text: King James Version (Public Domain)

## 🙏 Acknowledgments

- King James Version Bible text
- Data Structures and Algorithms course materials
- Python standard library documentation

## 📞 Support

For issues or questions:
- Check the in-app Help (option 7)
- Review this README
- Contact your course instructor

---

**Built with ❤️ using Python and Data Structures**

**Version:** 1.0  
**Last Updated:** November 19, 2024
