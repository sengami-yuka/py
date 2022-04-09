from typing import List

MORSE = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        return len(set("".join(MORSE[ord(ch) - 97] for ch in word) for word in words))
