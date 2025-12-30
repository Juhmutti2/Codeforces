'''

A. 123-sequence
time limit per test2 seconds
memory limit per test256 megabytes
There is a given sequence of integers a1, a2, ..., an, where every number is from 1 to 3 inclusively. You have to replace the minimum number of numbers in it so that all the numbers in the sequence are equal to each other.

Input
The first line contains an integer n (1 ≤ n ≤ 106). The second line contains a sequence of integers a1, a2, ..., an (1 ≤ ai ≤ 3).

Output
Print the minimum number of replacements needed to be performed to make all the numbers in the sequence equal.

Examples
InputCopy
9
1 3 2 2 2 1 1 2 3
OutputCopy
5
Note
In the example all the numbers equal to 1 and 3 should be replaced by 2.

KOMPAKTI
n= syötteen pituus
a= syöte

Syöte on numeroja 1,2,3. Halutaan tietää minimimäärä vaihtoja joilla koko syötelistan summasta tulee sama. 

RATKAISU

Halutaan siis tietää montako samaa lukua on. kaikki muut muutetaan samoiksi. 


GPT 4.0 TARJOAA

from collections import Counter

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    count = Counter(a)
    max_freq = max(count[1], count[2], count[3])
    min_replacements = n - max_freq
    print(min_replacements)


if __name__=='__main__':
    solve()

GPT tarjoaa samaa ratkaisua mutta ylimääräisillä askelilla. 

SUORITUS STATISTIIKKA
GPT 654 ms	97500 KB
OMA 592 ms	97600 KB

LINKKI
https://codeforces.com/problemset/problem/52/A


'''

from collections import Counter


class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):
        n,a=cases
        return n-max(Counter(a).values())

if __name__ =='__main__':
    n=int(input())
    a=list(map(int, input().split()))
    cases=[n,a]

    test_class=XXX2(cases)
    print(test_class.XXX())
