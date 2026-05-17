from corrector import text_corrector
import time

def main():
    text = input("Introduce the text to correct: ")
    clean_text = text.strip()
    if not clean_text:
        print("No text provided. Exiting.")
        return
    start_time = time.perf_counter()
    result = text_corrector(clean_text)
    print(result["respuesta"])
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Execution time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":   
    main()