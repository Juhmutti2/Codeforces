'''

A. Don't Try to Count
time limit per test2 seconds
memory limit per test256 megabytes
Given a string x
 of length n
 and a string s
 of length m
 (n⋅m≤25
), consisting of lowercase Latin letters, you can apply any number of operations to the string x
.

In one operation, you append the current value of x
 to the end of the string x
. Note that the value of x
 will change after this.

For example, if x=
"aba", then after applying operations, x
 will change as follows: "aba" →
 "abaaba" →
 "abaabaabaaba".

After what minimum number of operations s
 will appear in x
 as a substring? A substring of a string is defined as a contiguous segment of it.

Input
The first line of the input contains a single integer t
 (1≤t≤104
) — the number of test cases.

The first line of each test case contains two numbers n
 and m
 (1≤n⋅m≤25
) — the lengths of strings x
 and s
, respectively.

The second line of each test case contains the string x
 of length n
.

The third line of each test case contains the string s
 of length m
.

Output
For each test case, output a single number — the minimum number of operations after which s
 will appear in x
 as a substring. If this is not possible, output −1
.

Example
InputCopy
12
1 5
a
aaaaa
5 5
eforc
force
2 5
ab
ababa
3 5
aba
ababa
4 3
babb
bbb
5 1
aaaaa
a
4 2
aabb
ba
2 8
bk
kbkbkbkb
12 2
fjdgmujlcont
tf
2 2
aa
aa
3 5
abb
babba
1 19
m
mmmmmmmmmmmmmmmmmmm
OutputCopy
3
1
2
-1
1
0
1
3
1
0
2
5
Note
In the first test case of the example, after 2
 operations, the string will become "aaaa", and after 3
 operations, it will become "aaaaaaaa", so the answer is 3
.

In the second test case of the example, after applying 1
 operation, the string will become "eforceforc
", where the substring is highlighted in red.

In the fourth test case of the example, it can be shown that it is impossible to obtain the desired string as a substring.


SYÖTE
t =testitapausten määrä
n, m = x:n pituus, s:n pituus
x = merkkijono x
s=merkkijono s


KOMPAKTI
Kuinka monta kertaa x pitää tuplata, jossa s löytyy x:stä?

RATKAISU
Iteroidaan välillä 1,7. Huom. 1,6 riittää tuottamaan 32 merkkisen jonon jos n=1, mutta koska testaus on loopin alussa, tarvitaan 7.
Joka iteraatiolla tuplataan jono ja tarkistetaan löytyykö x s:stä. 

GPT 4.0 TARJOAA

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    x = input().strip()
    s = input().strip()
    
    current = x
    ops = 0
    found = False
    
    # rakentaen vähintään tarpeeksi pitkän että s voi osua rajakohtaan
    while len(current) < len(s) + len(x)*2:
        if s in current:
            print(ops)
            found = True
            break
        current += current
        ops += 1
        
    if not found:
        # viimeinen tarkistus, jos while päättyi
        if s in current:
            print(ops)
        else:
            print(-1)


GPT:llä on erikoinen lähestymistapa, sillä in range looppi tarjoaa suoraan ops muuttujan i:ssä. 
While muuttujan persoonallinen päättymisehto osoittaa, että koodille on todennäköisesti parempi ratkaisu. 
Käytännön nopeuden kannalta tällä ei ole merkitystä koska vastaus on aina välillä -1 ...5.
Ylläpidettävyyden kannalta kuitenkin oma koodini vie voiton. 

HUOM
Huomasin koodia refaktoroidessani, että alla oleva ratkaisu tuottaisi vielä Hiukan nopeamman lopputuloksen. Kuitenkin, kuten yleensä, jätän alkuperäisen ratkaisuni tähän. Tekevä oppii, sano. 

    def XXX(self):
        results=[]

        for x,s in self.cases:
            for i in range(6):#Luo ylipitkän merkkijonon, mutta koska vertailu alussa, n*m=25 tarvitaan 7, jotta ääriarvot varmistuvat
                if s in x:
                    results.append(str(i))#täydennys edellisellä kierroksella tai ilman muutoksia OK
                    break
                x=x+x
            if s not in x:
                results.append(str(-1))#ei onnistunut. 

        return '\n'.join(results)

SUORITUS STATISTIIKKA
GPT 233 ms	7800 KB
OMA 218 ms	8300 KB
REKFAKTOROITU OMA 203 ms	8300 KB

LINKKI

https://codeforces.com/problemset/problem/1881/A


'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):
        results=[]

        for x,s in self.cases:
            for i in range(1,7):#Luo ylipitkän merkkijonon, mutta koska vertailu alussa, n*m=25 tarvitaan 7, jotta ääriarvot varmistuvat
                if s in x:
                    results.append(str(i-1))#täydennys edellisellä kierroksella tai ilman muutoksia OK
                    break
                x=x+x
            if s not in x:
                results.append(str(-1))#ei onnistunut. 

        return '\n'.join(results)

if __name__ =='__main__':
    cases=[]
    t=int(input())
    for _ in range(t):
        n,m=map(int,input().split())
        x=input()
        s=input()
        cases.append([x,s])


    test_class=XXX2(cases)
    print(test_class.XXX())
