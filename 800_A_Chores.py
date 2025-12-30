'''

A. Chores
time limit per test2 seconds
memory limit per test256 megabytes
Petya and Vasya are brothers. Today is a special day for them as their parents left them home alone and commissioned them to do n chores. Each chore is characterized by a single parameter — its complexity. The complexity of the i-th chore equals hi.

As Petya is older, he wants to take the chores with complexity larger than some value x (hi > x) to leave to Vasya the chores with complexity less than or equal to x (hi ≤ x). The brothers have already decided that Petya will do exactly a chores and Vasya will do exactly b chores (a + b = n).

In how many ways can they choose an integer x so that Petya got exactly a chores and Vasya got exactly b chores?

Input
The first input line contains three integers n, a and b (2 ≤ n ≤ 2000; a, b ≥ 1; a + b = n) — the total number of chores, the number of Petya's chores and the number of Vasya's chores.

The next line contains a sequence of integers h1, h2, ..., hn (1 ≤ hi ≤ 109), hi is the complexity of the i-th chore. The numbers in the given sequence are not necessarily different.

All numbers on the lines are separated by single spaces.

Output
Print the required number of ways to choose an integer value of x. If there are no such ways, print 0.

Examples
InputCopy
5 2 3
6 2 3 100 1
OutputCopy
3
InputCopy
7 3 4
1 1 9 1 1 1 1
OutputCopy
0
Note
In the first sample the possible values of x are 3, 4 or 5.

In the second sample it is impossible to find such x, that Petya got 3 chores and Vasya got 4.

SYÖTE
n,a,b
h
n=h listan koko
a=Petya, vanhemman veljen askareet
b=Vasya, nuoremman veljen askareet

KOMPAKTI
Kuinka monella tavalla voidaan asettaa x annetusta syötteestä joka määrittää veljesten askareiden määrän


RATKAISU
Järjestetään lista, katsotaan kullekin veljelle indeksi, joka antaa molemmille riittävän määrän askareita ja lasketaan indeksien arvojen erotus. 

GPT 4.0 TARJOAA

def solve():
    n, a, b = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort()

    # Vasya saa b helpointa tehtävää eli h[0:b]
    # Petya saa a vaikeinta tehtävää eli h[b:n]

    # Vain jos h[b-1] < h[b], jako on mahdollinen
    # (eli kaikki helpot ovat varmasti helpompia kuin vaikeat)
    if h[b - 1] < h[b]:
        print(h[b] - h[b - 1])
    else:
        print(0)

solve()

GPT tarjoaa samaa logiikkaa hiukan monimutkaisemmin. GPT ei oivalla, että indeksien vähennys tuottaa joka tapauksessa oikean vastauksen, erillistä else -haaraa ei tarvita. 

SUORITUS STATISTIIKKA
GPT 108 ms	1400 KB
OMA 109 ms	1500 KB

LINKKI

https://codeforces.com/problemset/problem/169/A

'''

class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):

        a,b,h=cases
        h.sort()
        older_index=h[-a]#listan lopusta
        younger_index=h[b-1]#listan alusta

        return older_index-younger_index

if __name__ =='__main__':
    n,a,b=map(int, input().split())
    h=list(map(int,input().split()))
    cases=[a,b,h]

    test_class=XXX2(cases)
    print(test_class.XXX())
