import os
from collections import Counter
import re

def get_top_letters_and_words(text, num):
    # Normalize case and remove punctuation
    text_lower = text.lower()
    # Remove all non-alphanumeric except spaces and apostrophes
    text_no_punc = re.sub(r"[^\w\s']", ' ', text_lower)
    # Break contractions (don't -> don t)
    text_no_punc = text_no_punc.replace("'", " ")
    words = text_no_punc.split()
    
    # Count word frequencies
    word_counts = Counter(words)
    # Sort words: frequency descending, then alphabetical
    top_words = sorted(word_counts.items(), key=lambda x: (-x[1], x))[:num]
    
    # Count letter frequencies
    letters = [c for c in text_no_punc if c.isalpha()]
    letter_counts = Counter(letters)
    # Sort letters: frequency descending, then alphabetical
    top_letters = sorted(letter_counts.items(), key=lambda x: (-x[1], x))[:num]
    
    # Format outputs
    letters_out = f"Top {num} letters:\n"
    letters_out += "\n".join(f"{letter}: {count}" for letter, count in top_letters)
    
    words_out = f"\nTop {num} words:\n"
    words_out += "\n".join(f"{word}: {count}" for word, count in top_words)
    
    return letters_out, words_out

# Driver Code 
if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    text = input()
    num = int(input())
    letters,words = get_top_letters_and_words(text,num)
    fptr.write(letters)
    fptr.write("\n")
    fptr.write(words)
    fptr.close()
