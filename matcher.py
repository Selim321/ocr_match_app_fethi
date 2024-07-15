import re
import string
from typing import List, Tuple, Set

def count_words(name):
    return len(name.split())

def word_similarity(word1, word2):
    matching_chars = sum(c1 == c2 for c1, c2 in zip(word1, word2))
    return matching_chars / max(len(word1), len(word2))

def match_product_names(scanned_name, database_names):
    scanned_name = scanned_name.lower()
    scanned_words = scanned_name.split()
    
    for db_name in database_names:
        db_name_lower = db_name.lower()
        db_words = db_name_lower.split()
        
        if len(scanned_words) == len(db_words):
            # Check if each word in db_name shares at least 60% characters with the corresponding word in scanned_name
            if all(word_similarity(sw, dw) >= 0.6 for sw, dw in zip(scanned_words, db_words)):
                return db_name
        else:
            # Case 2: Word count is different, check for 100% character match (ignoring spaces)
            scanned_chars = ''.join(scanned_words)
            db_chars = ''.join(db_words)
            if scanned_chars == db_chars:
                return db_name
    
    return None  # No match found
        
def check_match(scanned_name: str, product_name: str, alternate_names: List[str]) -> Tuple[bool, List[str]]:
    """Check if the scanned name matches the product name or any of the alternate names."""
    words_list = [product_name] + alternate_names
    matches = match_product_names(scanned_name, words_list)
    return bool(matches), matches