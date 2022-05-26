# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = str(word).lower()
    anagram = str(anagram).lower()
    if sorted(word) == sorted(anagram):
       	return True
    else:
           return False
print(find_anagram("Flower", "begger"))
print(find_anagram("Flower", "lowFer"))