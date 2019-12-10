"""
Program to receive a pattern and text 
and return how many times the pattern appears in the text
"""

import re

#Implementation using RegEx 
#[?=name: lookahead assertion, matches pattern but does not consume any of the string]
def PatternCount(pattern, text):
    return len(re.findall(f"(?={pattern})", text))

#Test
def main():
    print(PatternCount("AGA", "AGAAGACTAGCTAGA"))


if __name__ == "__main__":
    main()