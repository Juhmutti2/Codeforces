'''

B. Squares
time limit per test2 seconds
memory limit per test256 megabytes
Vasya has found a piece of paper with a coordinate system written on it. There are n distinct squares drawn in this coordinate system. Let's number the squares with integers from 1 to n. It turned out that points with coordinates (0, 0) and (ai, ai) are the opposite corners of the i-th square.

Vasya wants to find such integer point (with integer coordinates) of the plane, that belongs to exactly k drawn squares. We'll say that a point belongs to a square, if the point is located either inside the square, or on its boundary.

Help Vasya find a point that would meet the described limits.

Input
The first line contains two space-separated integers n, k (1 ≤ n, k ≤ 50). The second line contains space-separated integers a1, a2, ..., an (1 ≤ ai ≤ 109).

It is guaranteed that all given squares are distinct.

Output
In a single line print two space-separated integers x and y (0 ≤ x, y ≤ 109) — the coordinates of the point that belongs to exactly k squares. If there are multiple answers, you are allowed to print any of them.

If there is no answer, print "-1" (without the quotes).

Examples
InputCopy
4 3
5 1 3 4
OutputCopy
2 1
InputCopy
3 1
2 4 1
OutputCopy
4 0
InputCopy
4 50
5 1 10 2
OutputCopy
-1


SYÖTE
n,k
a
n=neliöiden kokonaismäärä määrä, k= tavoite määrä neliöitä
a= neliöiden koordinaatti


KOMPAKTI
Anna koordinaattipiste, jonka sisällä on k määrä neliöitä, kun neliöiden vastakkaiset kulmat ovat aina pisteessä (0,0) ja (A_i,A_i)
Mikä tahansa vastaus kelpaa

RATKAISU
Oivallus: jos a:n järjestää laskevasti, saadaan tilanne jossa suurimman neliön ulkoreunat ovat varmasti vain yhdellä neliöllä
-> 
vastaus on a[k-1] a[k-1] koska se on uloin kulma. Poikkeuksen muodostaa tilanne jos k>n, silloin tehtävä on mahdoton. 



GPT 4.0 TARJOAA

n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

# lisätään yksi "ääriarvo" helpottamaan
a = [0] + a + [10**9 + 1]

for i in range(1, n+2):
    # katsotaan raja-arvot
    upper = a[i]
    lower = a[i-1]
    cnt = n - (i - 1)
    if cnt == k:
        # valitaan jokin t arvo
        t = lower + 1  # koska lower ei kuulu, mutta upper kyllä
        print(t, 0)
        exit()

print(-1)

GPT tarjoilee erittäin monimutkaisen ratkaisun, josta näkee mitä nykyinen tekoäly pohjimmiltaan on: 
Se yhdistelee asioita tilastollisen todennäköisyyden perusteella ilman ymmärrystä siitä mitä ollaan tekemässä. 

SUORITUS STATISTIIKKA
GPT 186 ms	200 KB
OMA 186 ms	200 KB

LINKKI
https://codeforces.com/problemset/problem/263/B


'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):

        n,k,a=self.cases
        if k>n:
            return -1
        a=sorted(a, reverse=True)

        return f'{a[k-1]} {a[k-1]}'#Kts yst otsikko RATKAISU

if __name__ =='__main__':
    n,k=map(int,input().split())
    a=list(map(int, input().split()))
    cases=[n,k,a]

    test_class=XXX2(cases)
    print(test_class.XXX())
