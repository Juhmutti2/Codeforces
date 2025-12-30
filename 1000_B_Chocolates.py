'''
B. Chocolates
time limit per test2 seconds
memory limit per test256 megabytes
You went to the store, selling n
 types of chocolates. There are ai
 chocolates of type i
 in stock.

You have unlimited amount of cash (so you are not restricted by any prices) and want to buy as many chocolates as possible. However if you buy xi
 chocolates of type i
 (clearly, 0≤xi≤ai
), then for all 1≤j<i
 at least one of the following must hold:

xj=0
 (you bought zero chocolates of type j
)
xj<xi
 (you bought less chocolates of type j
 than of type i
)
For example, the array x=[0,0,1,2,10]
 satisfies the requirement above (assuming that all ai≥xi
), while arrays x=[0,1,0]
, x=[5,5]
 and x=[3,2]
 don't.

Calculate the maximum number of chocolates you can buy.

Input
The first line contains an integer n
 (1≤n≤2⋅105
), denoting the number of types of chocolate.

The next line contains n
 integers ai
 (1≤ai≤109
), denoting the number of chocolates of each type.

Output
Print the maximum number of chocolates you can buy.

Examples
InputCopy
5
1 2 1 3 6
OutputCopy
10
InputCopy
5
3 2 5 4 10
OutputCopy
20
InputCopy
4
1 1 1 1
OutputCopy
1
Note
In the first example, it is optimal to buy: 0+0+1+3+6
 chocolates.

In the second example, it is optimal to buy: 1+2+3+4+10
 chocolates.

In the third example, it is optimal to buy: 0+0+0+1
 chocolates.


OSOITE
https://codeforces.com/problemset/problem/1139/B



SYÖTE
n=testilistan pituus
a=testilista

KOMPAKTI
paljonko suklaita voidaan ostaa kun:
jos ostat indeksin i suklaan, indeksien j suklaita ei osteta joko yhtään tai vähemmän. 



RATKAISU
Iteroidaan lopusta alkuun vertaillen viereisiä arvoja. 
mikäli a[i]>a[i+1] lisätään a[i] sellaisenaan. Muussa tapauksessa 
täytyy päivittää a[i+1] arvo vastaamaan lisättyä arvoa a[i] vähennettynä yhdellä.
Mikäli jokin alkio menee nollaan, läpikäynnin voi katkaista, koska lisätävää ei ole.

HUOM. laajemmassa ohjelmassa kannattaisi pyrkiä rakentamaan toimintatapa, joka ei muuta annettua listaa.
Tässä siitä ei ole haittaa, koska ohjelma ei palauta muutettua dataa mihinkään


GPT 4.0 TARJOAA

def solve(n, a):
    res = 0
    prev = float('inf')
    for i in range(n - 1, -1, -1):
        cur = min(a[i], prev - 1)
        if cur < 0:
            cur = 0
        res += cur
        prev = cur
    print(res)

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    solve(n, a)



SUORITUS STATISTIIKKA
GPT 140 ms	26200 KB
OMA 156 ms	26200 KB
'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):
        n,a=self.cases
        decreasing_sum=0
        last_sum=a[-1]
        exited=False

        for i in range(n-1,0,-1):
            if a[i]> a[i-1]:
                decreasing_sum+=a[i]#hiukan toisteinen mutta koen olevan selkeämpi näin. 
            else:
                decreasing_sum+=a[i]
                a[i-1]=a[i]-1#a[i-1] arvoa päivitettävä. 
                if a[i-1]<1:#ei lisättävää tässä tapauksessa.
                    exited=True
                    break
        if a[0]>=1 and not exited:#Lisätään viimeinen alkio, mikäli ehdot. 
            decreasing_sum+=a[0]


        return max(decreasing_sum,last_sum)

if __name__ =='__main__':
    cases=[]
    n=int(input())
    a=list(map(int, input().split()))
    cases=[n,a]

    test_class=XXX2(cases)
    print(test_class.XXX())
