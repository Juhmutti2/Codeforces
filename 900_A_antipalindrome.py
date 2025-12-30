'''


A. Antipalindrome
time limit per test1 second
memory limit per test256 megabytes
A string is a palindrome if it reads the same from the left to the right and from the right to the left. For example, the strings "kek", "abacaba", "r" and "papicipap" are palindromes, while the strings "abb" and "iq" are not.

A substring s[l…r]
 (1 ≤ l ≤ r ≤ |s|
) of a string s = s1s2…s|s|
 is the string slsl + 1…sr
.

Anna does not like palindromes, so she makes her friends call her Ann. She also changes all the words she reads in a similar way. Namely, each word s
 is changed into its longest substring that is not a palindrome. If all the substrings of s
 are palindromes, she skips the word at all.

Some time ago Ann read the word s
. What is the word she changed it into?

Input
The first line contains a non-empty string s
 with length at most 50
 characters, containing lowercase English letters only.

Output
If there is such a substring in s
 that is not a palindrome, print the maximum length of such a substring. Otherwise print 0
.

Note that there can be multiple longest substrings that are not palindromes, but their length is unique.

Examples
InputCopy
mew
OutputCopy
3
InputCopy
wuffuw
OutputCopy
5
InputCopy
qqqqqqqq
OutputCopy
0
Note
"mew" is not a palindrome, so the longest substring of it that is not a palindrome, is the string "mew" itself. Thus, the answer for the first example is 3
.

The string "uffuw" is one of the longest non-palindrome substrings (of length 5
) of the string "wuffuw", so the answer for the second example is 5
.

All substrings of the string "qqqqqqqq" consist of equal characters so they are palindromes. This way, there are no non-palindrome substrings. Thus, the answer for the third example is 0
.




SYÖTE
yksirivinen merkkijono

KOMPAKTI
Mikä on pisimmän alimerkkijonon pituus, joka ei ole palindromi

RATKAISU
Iteroidaan merkkijonoa lyhyentäen läpi ja testataan onko palindromi. jos lyhennys EI ole palindromi, vastaus=
len(case)-i

GPT 4.0 TARJOAA

def is_palindrome(s):
    return s == s[::-1]

s = input().strip()

if not is_palindrome(s):
    print(len(s))
elif len(set(s)) == 1:
    print(0)
else:
    print(len(s) - 1)

GPT tarjoaa toisenlaisen lähestymistavan, jossa testataan onko merkkijono palindromi. 
Mikäli ei ole, palautetaan merkkijonon pituus
Mikäli on, tarkistetaan onko kaikki merkit samoja, silloin 0
Muulloin palautetaan merkkijonon pituus -1. 

Ehtolauseiden runsaan määrän vuoksi GPT:n lähestymistapa on tässä hitaampi. Huomattavaa on, että GPT:n ratkaisu on laajennettavissa, siinä missä oma ei ole. 
Oma tosin toimii tehokkaasti tässä tapauksessa. 

SUORITUS STATISTIIKKA
GPT 155 ms	200 KB
OMA 93 ms	200 KB

LINKKI
https://codeforces.com/problemset/problem/981/A

'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):
        case=self.cases

        for i in range(len(case)):
            if case[i:]!=case[i:][::-1]:#Jos leikattu case ei ole palindromi
                return len(case)-i
        return 0

if __name__ =='__main__':
    cases=input()

    test_class=XXX2(cases)
    print(test_class.XXX())
