"""Given a string, return True if it is a pangram, False otherwise.

For example::

    >>> is_pangram("The quick brown fox jumps over the lazy dog!")
    True
    
    >>> is_pangram("I love cats, but not mice")
    False
"""


def is_pangram(sentence):
    """Given a string, return True if it is a pangram, False otherwise."""
    alphabeth = 'qwertyuiopasdfghjklzxcvbnm'

    dict_chars = {}

    for char in sentence.lower():
        if char in alphabeth:
            if char not in dict_chars:
                dict_chars[char] = 1
            else:  
                dict_chars[char]+= 1      

    return len(alphabeth) == len(dict_chars)        


            
             
        


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")
