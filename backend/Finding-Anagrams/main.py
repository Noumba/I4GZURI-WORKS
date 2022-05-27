# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if(len(word) == len(anagram)):
        if(sorted(word.lower()) == sorted(anagram.lower())):
            return True
        else:
            return False
    else:
        return False


print(find_anagram('LEONARD', 'leonard'))
