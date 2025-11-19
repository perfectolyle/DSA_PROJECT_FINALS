from storage.history import add_to_history

def compute_lps_array(pattern):
    M = len(pattern)
    lps = [0] * M
    length = 0
    i = 1
    while i < M:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    N, M = len(text), len(pattern)
    if M == 0: return True
    if N == 0 or M > N: return False
    lps = compute_lps_array(pattern)
    i = j = 0
    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == M:
            return True
        elif i < N and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return False

def search_verse(books, keyword):
    if not books: return
    print(f"\n🔍 Searching for: '{keyword}' using KMP algorithm...")
    add_to_history(keyword)
    results = []
    PAGE_SIZE = 10
    keyword_lower = keyword.lower()
    for book in books:
        for chapter in book["chapters"]:
            for verse_obj in chapter["verses"]:
                if kmp_search(verse_obj["text"].lower(), keyword_lower):
                    ref = f"{book['name']} {chapter['chapter']}:{verse_obj['verse']}"
                    results.append((ref, verse_obj["text"]))
    if not results:
        print("No results found.")
        return
    total_results = len(results)
    total_pages = (total_results + PAGE_SIZE - 1) // PAGE_SIZE
    current_page = 1
    while True:
        start_index = (current_page-1)*PAGE_SIZE
        end_index = min(current_page*PAGE_SIZE, total_results)
        print(f"\nFound {total_results} result(s). Displaying Page {current_page} of {total_pages}. Pages: ({current_page}/{total_pages})\n")
        for i, (ref, verse_text) in enumerate(results[start_index:end_index], start=start_index+1):
            print(f"{i}. {ref} - {verse_text[:80]}{'...' if len(verse_text)>80 else ''}")
        if current_page < total_pages and current_page == 1:
            action = input("➡ Press [N]ext page, [Q]uit or any key to main menu: ").lower()
            if action == 'n': current_page += 1
            elif action == 'q': break
            else: break
        elif current_page < total_pages:
            action = input("➡ Press [N]ext page, [B]ack page, [Q]uit or any key to main menu: ").lower()
            if action == 'n': current_page += 1
            elif action == 'b': current_page -= 1
            elif action == 'q': break
            else: break
        elif total_pages == 1:
            input("➡ Press [Q]uit or any key to main menu: ")
            break
        else:
            action = input("➡ End of results. Press [F]irst Page, [B]ack page, [Q]uit or any key to main menu: ").lower()
            if action == 'b': current_page -= 1
            if action == 'f': current_page = 1
            elif action == 'q': break
            else: break
