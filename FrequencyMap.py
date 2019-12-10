import re
from collections import Counter

# FrequencyMap() returns all occurrences of a k-mer 
# in a given String text
def FrequencyMap(text, k):
    pattern = "(.{%d})"%k

    return dict(Counter(re.findall(f"(?={pattern})",text)))

#Test
def main():
    k = 3
    text = "CGATATATCCATAG"
    print(FrequencyMap(text, k))

if __name__ == "__main__":
    main()