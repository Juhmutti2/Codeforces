'''

A. Everybody Likes Good Arrays!
time limit per test1 second
memory limit per test256 megabytes
An array a
 is good if for all pairs of adjacent elements, ai
 and ai+1
 (1≤i<n
) are of different parity. Note that an array of size 1
 is trivially good.

You are given an array of size n
.

In one operation you can select any pair of adjacent elements in which both elements are of the same parity, delete them, and insert their product in the same position.

Find the minimum number of operations to form a good array.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤500
). The description of the test cases follows.

The first line of each test case contains an integer n
 (1≤n≤100
).

The second line of each test case contains n
 integers a1,a2,…,an
 (1≤ai≤109
).

Output
For each test case print an integer, the minimum number of operations required to form a good array.

Example
InputCopy
3
5
1 7 11 2 13
4
1 2 3 4
6
1 1 1 2 2 3
OutputCopy
2
0
3
Note
Consider the first test case. Select the 2
-nd and the 3
-rd integers and apply the operation on them. The array changes from [1,7,11,2,13]
 to [1,77,2,13]
. Next, select the 1
-st and the 2
-nd integers, array changes from [1,77,2,13]
 to [77,2,13]
. Thus we require 2
 operations. It can be proved that this is the minimum number of operations.

In the second test case, the given array is already good. So we require 0
 operations.





SYÖTE
t
n
a
t=testitapaukseet
n=testilistan pituus
a=testilista

KOMPAKTI
Kuinka monella operaatiolla listasta saadaan lista, jossa pariton ja parillinen alkio vuorottelevat. 
yhden pituinen lista on sallittu lopputulos. 

operaatio= kahden saman pariteetin alkion yhdistäminen niiden tuloksi. 

Oivallus: operaatio ei muuta pariteettia, mutta vähentää yhdellä ei-toivottujen lukujen määrää.


RATKAISU

Lasketaan perättäiset saman pariteetin luvut. 

GPT 4.0 TARJOAA

def min_operations_to_good_array(test_cases):
    results = []
    for a in test_cases:
        ops = 0
        i = 0
        while i < len(a) - 1:
            if a[i] % 2 == a[i + 1] % 2:
                ops += 1
                # yhdistetään pari -> korvataan tulolla
                a[i] = a[i] * a[i + 1]
                del a[i + 1]
                # pysytään kohdassa i, koska uusi arvo voi taas muodostaa parin
                if i > 0:
                    i -= 1
            else:
                i += 1
        results.append(ops)
    return results

# Syötteen luku
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append(a)

# Tulostus
answers = min_operations_to_good_array(test_cases)
for ans in answers:
    print(ans)

GPT:n koodia katsoessa tekee mieli kaivaa krusifiksiä. Koodi toimii, mutta on jälleen esimerkki hallusinaatiota lähestyvästä ratkaisusta, 
eli ratkaisusta joka toimii mutta on tarpeettoman monimutkainen. Vastaus on sikäli yllättävä että yleensä GPT 4.0 tuottaa siistin ratkaisun vastaavan tasoisissa tehtävissä. 


SUORITUS STATISTIIKKA
GPT 92 ms	2300 KB
OMA 93 ms	2100 KB


LINKKI

https://codeforces.com/problemset/problem/1777/A

'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):
        results=[]
        for n,a in self.cases:
            counter=0#yhden testin tulos. 
            for i in range(n-1):
                if a[i]%2==a[i+1]%2:#sama parieteetti.
                    counter+=1
            results.append(str(counter))#Muunto merkkijonoksi jotta saadaan vaadittu tulostusmuoto. 


        return "\n".join(results)

if __name__ =='__main__':
    cases=[]
    t=int(input())

    for _ in range(t):
        n=int(input())
        a=list(map(int, input().split()))
        cases.append([n,a])

    test_class=XXX2(cases)
    print(test_class.XXX())
