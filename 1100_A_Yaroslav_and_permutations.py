'''
A. Yaroslav and Permutations
time limit per test2 seconds
memory limit per test256 megabytes
Yaroslav has an array that consists of n integers. In one second Yaroslav can swap two neighboring array elements. Now Yaroslav is wondering if he can obtain an array where any two neighboring elements would be distinct in a finite time.

Help Yaroslav.

Input
The first line contains integer n (1 ≤ n ≤ 100) — the number of elements in the array. The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 1000) — the array elements.

Output
In the single line print "YES" (without the quotes) if Yaroslav can obtain the array he needs, and "NO" (without the quotes) otherwise.

Examples
InputCopy
1
1
OutputCopy
YES
InputCopy
3
1 1 2
OutputCopy
YES
InputCopy
4
7 7 7 7
OutputCopy
NO
Note
In the first sample the initial array fits well.

In the second sample Yaroslav can get array: 1, 2, 1. He can swap the last and the second last elements to obtain it.

In the third sample Yarosav can't get the array he needs.


OSOITE

https://codeforces.com/problemset/problem/296/A

SYÖTE
n=testitapausten määrä
a=testilista

KOMPAKTI
Voidaanko lista asettaa niin että eri luvut ovat vierekkäin?

RATKAISU
Voidaan, mikäli samoja lukuja on maksimissaan n/2 jos n%2==0 tai n/2+1 jos n%2==1


GPT 4.0 TARJOAA

from collections import Counter
import math

n = int(input())
a = list(map(int, input().split()))

counts = Counter(a)
max_count = max(counts.values())

if max_count <= math.ceil(n / 2):
    print("YES")
else:
    print("NO")

GPT tarjoaa samaa lähestymistapaa hiukan eri tavoin toteutettuna. 


SUORITUS STATISTIIKKA
GPT 186 ms	900 KB
OMA 186 ms	900 KB


LINKKI
https://codeforces.com/problemset/problem/296/A

'''


from collections import Counter

class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):
        n,cases=self.cases

        count=Counter(cases)
        max_count=max(count.values())

        if n%2==1 and max_count<=(n//2)+1:
            return 'YES'
        elif n%2==0 and max_count<=(n//2):
            return 'YES'
        return 'NO'
        
if __name__ =='__main__':
    n=int(input())
    t=list(map(int, input().split()))
    cases=[n,t]

    test_class=XXX2(cases)
    print(test_class.XXX())
