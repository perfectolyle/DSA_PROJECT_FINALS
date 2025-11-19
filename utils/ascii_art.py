import time

def display_ascii_art(delay=0.03):
    ascii_book = r"""
██████╗ ██╗██████╗ ██╗     ███████╗
██╔══██╗██║██╔══██╗██║     ██╔════╝
██████╔╝██║██████╔╝██║     █████╗  
██╔══██╗██║██╔══██╗██║     ██╔══╝  
██████╔╝██║██████╔╝███████╗███████╗
╚═════╝ ╚═╝╚═════╝ ╚══════╝╚══════╝                                                        
"""
    for line in ascii_book.split('\n'):
        if line.strip():
            print(line.rstrip())
            time.sleep(delay)
    print("\n")
