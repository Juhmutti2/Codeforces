'''

A. Chips
time limit per test2 seconds
memory limit per test256 megabytes
There are n walruses sitting in a circle. All of them are numbered in the clockwise order: the walrus number 2 sits to the left of the walrus number 1, the walrus number 3 sits to the left of the walrus number 2, ..., the walrus number 1 sits to the left of the walrus number n.

The presenter has m chips. The presenter stands in the middle of the circle and starts giving the chips to the walruses starting from walrus number 1 and moving clockwise. The walrus number i gets i chips. If the presenter can't give the current walrus the required number of chips, then the presenter takes the remaining chips and the process ends. Determine by the given n and m how many chips the presenter will get in the end.

Input
The first line contains two integers n and m (1 ≤ n ≤ 50, 1 ≤ m ≤ 104) — the number of walruses and the number of chips correspondingly.

Output
Print the number of chips the presenter ended up with.

Examples
InputCopy
4 11
OutputCopy
0
InputCopy
17 107
OutputCopy
2
InputCopy
3 8
OutputCopy
1
Note
In the first sample the presenter gives one chip to the walrus number 1, two chips to the walrus number 2, three chips to the walrus number 3, four chips to the walrus number 4, then again one chip to the walrus number 1. After that the presenter runs out of chips. He can't give anything to the walrus number 2 and the process finishes.

In the third sample the presenter gives one chip to the walrus number 1, two chips to the walrus number 2, three chips to the walrus number 3, then again one chip to the walrus number 1. The presenter has one chip left and he can't give two chips to the walrus number 2, that's why the presenter takes the last chip.



SYÖTE
n,m

n=mursujen määrä
m=sipsien määrä
KOMPAKTI
Mursuille jaetaan sipsejä mursun järjestysluvun mukaan. Mursulle pitää antaa järjestysluvun mukainen määrä sipsejä tai ei yhtään Jääkö sipsejä yli?

RATKAISU

lasketaan kulutus kierrosta kohden ja sen jälkeen paljonko sipsejä jää yli täydestä kierroksesta
Iteroidaan viimeistä kierrosta niin kauan kuin sipsejä riittää. 

GPT 4.0 TARJOAA


def remaining_chips(n, m):
    i = 1
    while True:
        if m >= i:
            m -= i
            i += 1
            if i > n:
                i = 1
        else:
            return m

# Lukee syötteen ja tulostaa vastauksen
n, m = map(int, input().split())
print(remaining_chips(n, m))


GPT tuottaa kompaktimman mutta hyvin paljon vaikeammin hahmotettavan koodin, joka käyttää suhteellisesti merkkitävästi enemmän muistia. 
Absoluuttisesti ero on hyvin pieni. 

SUORITUS STATISTIIKKA
GPT 186 ms	1300 KB
OMA 186 ms	200 KB

LINKKI

https://codeforces.com/problemset/problem/92/A


'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):
        n,m=cases
        per_round=(n*(n+1))//2#Kulutus kierroksella aritmeettisen summan mukaan. 
        remaining_chips=divmod(m, per_round)[1]#paljonko sipsejä jää yli täydestä kierroksesta


        for i in range(1,n+1):
            if remaining_chips-i>=0:#Niin kauan kuin sipsejä riittää. 
                remaining_chips-=i
            else:#Pieni optimointi
                break
        return remaining_chips

if __name__ =='__main__':
    cases=[]
    n,m=map(int,input().split())

    cases=[n,m]

    test_class=XXX2(cases)
    print(test_class.XXX())
