'''
A. Guess the Maximum
time limit per test1 second
memory limit per test256 megabytes
Alice and Bob came up with a rather strange game. They have an array of integers a1,a2,…,an
. Alice chooses a certain integer k
 and tells it to Bob, then the following happens:

Bob chooses two integers i
 and j
 (1≤i<j≤n
), and then finds the maximum among the integers ai,ai+1,…,aj
;
If the obtained maximum is strictly greater than k
, Alice wins, otherwise Bob wins.
Help Alice find the maximum k
 at which she is guaranteed to win.

Input
Each test consists of multiple test cases. The first line contains a single integer t
 (1≤t≤104
) — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer n
 (2≤n≤5⋅104
) — the number of elements in the array.

The second line of each test case contains n
 integers a1,a2,…,an
 (1≤ai≤109
) — the elements of the array.

It is guaranteed that the sum of n
 over all test cases does not exceed 5⋅104
.

Output
For each test case, output one integer — the maximum integer k
 at which Alice is guaranteed to win.

Example
InputCopy
6
4
2 4 1 7
5
1 2 3 4 5
2
1 1
3
37 8 16
5
10 10 10 10 9
10
3 12 9 5 2 3 2 9 8 2
OutputCopy
3
1
0
15
9
2
Note
In the first test case, all possible subsegments that Bob can choose look as follows: [2,4],[2,4,1],[2,4,1,7],[4,1],[4,1,7],[1,7]
. The maximums on the subsegments are respectively equal to 4,4,7,4,7,7
. It can be shown that 3
 is the largest integer such that any of the maximums will be strictly greater than it.

In the third test case, the only segment that Bob can choose is [1,1]
. So the answer is 0
.


KOMPAKTI
Alice ja Bob pelaavat. Alice valitsee ENSIN minkä tahansa luvun, ja bob valitsee indeksiä testilistalta.
Alice voittaa, jos  Bobin valitseman indeksivälin maksimi on suurempi kuin Alicen luku. 

RATKAISU
Mitkä tahansa kaksi indeksiä tarkoittavat jokaista mahdollista paria testilistalta. 
Ratkaisu= haetaan näistä pareista pienin maksimiarvo ja otetaan pois -1


GPT 4.0 TARJOAA
def guess_the_maximum(test_cases):
    results = []
    for arr in test_cases:
        min_of_pair_max = float('inf')
        for i in range(len(arr) - 1):
            pair_max = max(arr[i], arr[i + 1])
            min_of_pair_max = min(min_of_pair_max, pair_max)
        results.append(min_of_pair_max - 1)
    return results

GPT:n tarjous on käytännössä sama. 

SUORITUS STATISTIIKKA
GPT 171 ms	7900 KB
OMA 124 ms	8600 KB

HUOM

Pieni hupinyanssi: Kirjoittelin koodia alunperin aivan pata jäässä aiempien muistiinpanojen pohjalta. 
Luin muistiinpanoja huonosti ja rakensin alla olevan koodin, joka vastoin kaikkia odotuksia toimii. En pysty kirjoitushetkellä käsittämään miksi.

Jätän tämän muistuttamaan, että 18.5.2025 pystyin kovassa kohmeessa muodostamaan kohtuullisen hyvän koodin uudestaan. 
Siinäkin on toki parannettavaa, mutta tässä näkyy kehittyminen. 

class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):
        results=[]

        for case in self.cases:
            target_list=[]
            n, case_list=case
            min_diff=float('inf')#asetetaan hyvin suureksi
            target=0
            for i in range(n-1):
                a=case_list[i]
                b=case_list[i+1]
                current=a-b
                if current<=min_diff:
                    target=max(a,b)-1
                    target_list.append(target)
            results.append(str(min(target_list)))
        

        return "\n".join(results)

LINKKI
https://codeforces.com/problemset/problem/1979/A

'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):
        results=[]

        for case in self.cases:

            target_list=[]#Jostain syystä olen katsonut hyväksi kerätä tulokset listaan ilman suoraa min vertailua ':D'
            n, case_list=case

            for i in range(n-1):
                current=max(case_list[i],case_list[i+1])-1
                target_list.append(current)
                if current==0:#pienin mahdollinen ero. 
                    break
            results.append(str(min(target_list)))
        

        return "\n".join(results)

if __name__ =='__main__':
    cases=[]
    t=int(input())

    for _ in range(t):
        n=int(input())
        b=list(map(int, input().split()))
        cases.append([n,b])


    test_class=XXX2(cases)
    print(test_class.XXX())
