# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word):
    # [assignment] Add your code here

   
  rev_str = ''.join(reversed(word))
  if (word == rev_str):
    return True
  else:
    return False

print(find_anagrams('Hello'))
print(find_anagrams('pawpaw'))
print(find_anagrams('racecar'))