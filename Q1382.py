"""Check if the Sentence Is Pangram
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false
 

Constraints:

1 <= sentence.length <= 1000
sentence consists of lowercase English letters."""
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        frequency=[]
        length=len(sentence)
        print (length)
        if length<26:
            return False
        else:
            for s in sentence:
                if s not in frequency:
                    frequency.append(s)
            print(frequency)
            if len(frequency)==26:
                return True
            else:
                return False