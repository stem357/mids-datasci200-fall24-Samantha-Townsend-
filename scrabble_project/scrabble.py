#!/usr/bin/env python
# coding: utf-8

# In[25]:



from wordscore import score_word

def run_scrabble(rack):
    """
    Given a rack of 2-7 characters, finds all valid Scrabble words that can be made from the rack
    and returns the words along with their Scrabble scores.
    
    The function also handles wildcard characters ('*' and '?').
    
    Parameters:
    rack (str): A string containing 2 to 7 characters representing the Scrabble rack.
    
    Returns:
    tuple: A sorted list of (score, word) tuples and the total number of valid words.
    """
    # Handle invalid input
    if not (2 <= len(rack) <= 7):
        return "Error: The rack must contain between 2 and 7 characters."
    
    # Load the list of valid Scrabble words from 'sowpods.txt'
    with open("C:/Users/Samantha Townsend/Desktop/HW6/sowpods.txt", "r") as infile:
        raw_input = infile.readlines()
        valid_words = [datum.strip().upper() for datum in raw_input]
    
    results = []

    # Helper function to check if a word can be made from the rack
    def can_form_word(rack, word):
        rack_copy = list(rack.upper())
        for letter in word:
            if letter in rack_copy:
                rack_copy.remove(letter)
            elif '*' in rack_copy or '?' in rack_copy:
                rack_copy.remove('*' if '*' in rack_copy else '?')
            else:
                return False
        return True

    # Find all valid words that can be made from the rack
    for word in valid_words:
        if can_form_word(rack, word):
            word_score = score_word(word)
            results.append((word_score, word))
    
    # Sort the results by score and alphabetically by word
    sorted_results = sorted(results, key=lambda x: (-x[0], x[1]))

    return sorted_results, len(sorted_results)


# In[ ]:





# In[ ]:





# In[ ]:




