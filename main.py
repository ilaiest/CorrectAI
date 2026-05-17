from corrector import text_corrector
import time
import pyperclip


def terminal_mode():
    text = input("Introduce the text to correct: ")
    clean_text = text.strip()
    if not clean_text:
        print("No text provided. Exiting.")
        return
    start_time = time.perf_counter()
    result = text_corrector(clean_text)
    print(result["response"])
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Execution time: {elapsed_time:.2f} seconds") 

def clipboard_mode():
    print("Reading from clipboard...")
    text = pyperclip.paste()
    clean_text = text.strip()
    if not clean_text:
        print("No text found in clipboard. Please copy some text and try again.")
        return
    start_time = time.perf_counter()
    result = text_corrector(clean_text)
    pyperclip.copy(result["response"])
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Text corrected and copied to clipboard. Execution time: {elapsed_time:.2f} seconds")


def main():
    options = input("Choose an option:\n1. Terminal \n2. Clipboard\n")
    if options == "1":
        terminal_mode()
    elif options == "2":
        clipboard_mode()
    else:
        print("Invalid option. Please choose 1 or 2.")


if __name__ == "__main__":   
    main()