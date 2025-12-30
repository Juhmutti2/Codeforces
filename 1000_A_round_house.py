'''
A. Round House
time limit per test1 second
memory limit per test256 megabytes
Vasya lives in a round building, whose entrances are numbered sequentially by integers from 1 to n. Entrance n and entrance 1 are adjacent.

Today Vasya got bored and decided to take a walk in the yard. Vasya lives in entrance a and he decided that during his walk he will move around the house b entrances in the direction of increasing numbers (in this order entrance n should be followed by entrance 1). The negative value of b corresponds to moving |b| entrances in the order of decreasing numbers (in this order entrance 1 is followed by entrance n). If b = 0, then Vasya prefers to walk beside his entrance.

Illustration for n = 6, a = 2, b =  - 5.
Help Vasya to determine the number of the entrance, near which he will be at the end of his walk.

Input
The single line of the input contains three space-separated integers n, a and b (1 ≤ n ≤ 100, 1 ≤ a ≤ n,  - 100 ≤ b ≤ 100) — the number of entrances at Vasya's place, the number of his entrance and the length of his walk, respectively.

Output
Print a single integer k (1 ≤ k ≤ n) — the number of the entrance where Vasya will be at the end of his walk.

Examples
InputCopy
6 2 -5
OutputCopy
3
InputCopy
5 1 3
OutputCopy
4
InputCopy
3 2 7
OutputCopy
3
Note
The first example is illustrated by the picture in the statements.

OSOITE
https://codeforces.com/problemset/problem/659/A

SYÖTE
n,a,b
n=sisäänkäyntien määrä
a=kotiosoite(alku)
b=lenkin pituus sisäänkäyntien määrässä mitattuna


KOMPAKTI
Minkä numeron ovelle lenkki päättyy kun ovet on numeroitu 1-n?

RATKAISU
Tehtävä on ympäri menevä laskuri, eli summa%laskurin kierrokset

GPT 4.0 TARJOAA

n, a, b = map(int, input().split())
final = ((a - 1 + b) % n) + 1
print(final)

GPT:n ratkaisu on sama, mutta ei kuitenkaan. GPT muuttaa askeleet nollapohjaiseksi ja palauttaa ne 1-pohjaiseksi. 
Vertailussa GPT kehuu, että GPT:n tyyli suositeltavaa. Sanoisin, että ilman selkeää tarvetta nollapohjaiselle indeksoinnille, sitä ei tulisi tehdä. 
Lisähuomiona mielestäni tässä näkyy jälleen kerran GPT:n puutteellinen kyky ymmärtää asiayhteyksillä. Juuri näillä vaatimuksilla ja reunaehdoilla esittämäni ratkaisu on kompakti ja siten ylläpidettävä.



SUORITUS STATISTIIKKA
GPT 93 ms	200 KB
OMA 93 ms	200 KB

LINKKI
https://codeforces.com/problemset/problem/659/A

'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):

        n,a,b=self.cases
        result=(a+b)%n#ovien summa%ovien määrä
   
        return result if result!=0 else n #Nolla tarkoittaa kotiovea. 

if __name__ =='__main__':
    n,a,b=map(int,input().split())
    cases=[n,a,b]

    test_class=XXX2(cases)
    print(test_class.XXX())
