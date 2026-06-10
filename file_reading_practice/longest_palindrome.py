"""
## 5. Longest Palindrome in the File  *(Hard)*

=================================================
LONGEST PALINDROME
=================================================

Problem Statement:
Read the text file `sowpods.txt` and find the
LONGEST PALINDROME word in the file.

If multiple palindromes share the maximum
length, print ALL of them.

-------------------------------------------------
Input Example (sowpods.txt sample):
level
radar
noon
civic
deified
racecar
rotator
malayalam

Output Example:
Longest palindrome length: 9
malayalam

-------------------------------------------------
Explanation:
Lengths of the palindromes in the sample:
   level    -> 5
   radar    -> 5
   noon     -> 4
   civic    -> 5
   deified  -> 7
   racecar  -> 7
   rotator  -> 7
   malayalam -> 9
The longest is "malayalam" with 9 characters.
=================================================

"""
f = open("sowpods.txt", "r")
words = f.read().splitlines()
f.close()

palindromes = []
for w in words:
    rev = ""
    i = len(w) - 1
    while i >= 0:
        rev = rev + w[i]
        i = i - 1
    if w == rev:
        palindromes.append(w)

max_len = 0
for w in palindromes:
    if len(w) > max_len:
        max_len = len(w)

for w in palindromes:
    if len(w) == max_len:
        print("Longest palindrome length:", max_len)
        print(w)
