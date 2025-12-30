'''
time limit per test2 seconds
memory limit per test256 megabytes
Little Vasya has received a young builder’s kit. The kit consists of several wooden bars, the lengths of all of them are known. The bars can be put one on the top of the other if their lengths are the same.

Vasya wants to construct the minimal number of towers from the bars. Help Vasya to use the bars in the best way possible.

Input
The first line contains an integer N (1 ≤ N ≤ 1000) — the number of bars at Vasya’s disposal. The second line contains N space-separated integers li — the lengths of the bars. All the lengths are natural numbers not exceeding 1000.

Output
In one line output two numbers — the height of the largest tower and their total number. Remember that Vasya should use all the bars.

Examples
InputCopy
3
1 2 3
OutputCopy
1 3
InputCopy
4
6 5 6 7
OutputCopy
2 3


KOMPAKTI
Tehtävä on hiukan huonosti selitetty. 
Halutaan löytää maksimiesiintymien määrä (=korkein torni) sekä eri lukujen määrä(=tornien määrä)

Jos arvo on olemassa listalla, torni on olemassa. 

RATKAISU
Käytämme Counter, koska esiintymien määrä ratkaisee korkeimman tornin. 

GPT 4.0 TARJOAA

from collections import Counter

n = int(input())
lengths = list(map(int, input().split()))

counter = Counter(lengths)
max_height = max(counter.values())
tower_count = len(counter)

print(max_height, tower_count)

GPT tarjoaa samaa ratkaisua, joka on kuitenkin hiukan hitaampi. ero selittyy max_height kohdalla. 
Mikäli oma koodini refaktoroidaan käyttämään max(counts.values()) suoritusaika ja muistinkäyttö on sama kuin GPT:llä (kts yst alla)


SUORITUS STATISTIIKKA
GPT     218 ms	900 KB
OMA 	186 ms	900 KB

LINKKI
https://codeforces.com/problemset/problem/37/A

'''

from collections import Counter


class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):
        results=[]
        counts=Counter(self.cases)
        results.append(max(counts.most_common(1)[0][1]))#suurin esiintymä=korkein torni
        results.append(len(counts))#Tornien määrä

        return results

if __name__ =='__main__':
    t=int(input())
    cases=list(map(int, input().split()))



    test_class=XXX2(cases)
    print(*test_class.XXX())
