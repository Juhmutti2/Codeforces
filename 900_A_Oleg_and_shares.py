'''
A. Oleg and shares
time limit per test1 second
memory limit per test256 megabytes
Oleg the bank client checks share prices every day. There are n share prices he is interested in. Today he observed that each second exactly one of these prices decreases by k rubles (note that each second exactly one price changes, but at different seconds different prices can change). Prices can become negative. Oleg found this process interesting, and he asked Igor the financial analyst, what is the minimum time needed for all n prices to become equal, or it is impossible at all? Igor is busy right now, so he asked you to help Oleg. Can you answer this question?

Input
The first line contains two integers n and k (1 ≤ n ≤ 105, 1 ≤ k ≤ 109) — the number of share prices, and the amount of rubles some price decreases each second.

The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 109) — the initial prices.

Output
Print the only line containing the minimum number of seconds needed for prices to become equal, of «-1» if it is impossible.

Examples
InputCopy
3 3
12 9 15
OutputCopy
3
InputCopy
2 2
10 9
OutputCopy
-1
InputCopy
4 1
1 1000000000 1000000000 1000000000
OutputCopy
2999999997
Note
Consider the first example.

Suppose the third price decreases in the first second and become equal 12 rubles, then the first price decreases and becomes equal 9 rubles, and in the third second the third price decreases again and becomes equal 9 rubles. In this case all prices become equal 9 rubles in 3 seconds.

There could be other possibilities, but this minimizes the time needed for all prices to become equal. Thus the answer is 3.

In the second example we can notice that parity of first and second price is different and never changes within described process. Thus prices never can become equal.

In the third example following scenario can take place: firstly, the second price drops, then the third price, and then fourth price. It happens 999999999 times, and, since in one second only one price can drop, the whole process takes 999999999 * 3 = 2999999997 seconds. We can note that this is the minimum possible time.
SYÖTE
n,k
t
n=osakkeiden määrä
k=hintamuutos
t=lista osakkeiden hinnoista

KOMPAKTI
kun yhden osakkeen hinta muuttuu sekunnissa k verran, voiko kaikista osakkeista tulla saman hintaisia?
Tulostetaan tarvittava sekuntien määrä

RATKAISU
Meidän täytyy ensin tarkistaa että jokainen hinnan ja minimihinnan erotus on jaollinen k:lla.
Tämän jälkeen lasketaan sekuntimuutostarve

GPT 4.0 TARJOAA

def min_seconds_to_equal_prices(n, k, a):
    min_val = min(a)
    total_seconds = 0
    
    for price in a:
        diff = price - min_val
        if diff % k != 0:
            return -1
        total_seconds += diff // k #tarpeettoman monimutkainen operaatio. OMA merkkaus. 
        
    return total_seconds

# Lukee syötteen
if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_seconds_to_equal_prices(n, k, a))

GPT:n tarjous on pohjimmiltaan sama, mutta erilaisella rakenteella. Mikäli GPT:n total_seconds laskuoperaatio refaktoroidaan käyttämään vastaavaa kuin omassa versiossani, 
suoritus muuttuu 109 ms	13400 KB. Mielenkiintoisesti aavistuksen toisteisen t[i]-min_price muuttujan muuttaminen esimerksi diff=t[i]-min_price, hidastaisi omaa koodia:
124 ms	13200 KB


SUORITUS STATISTIIKKA
GPT 124 ms	13400 KB
OMA 108 ms	13300 KB

LINKKI
https://codeforces.com/problemset/problem/793/A

'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):

        n,k,t=cases
        total_diff=0
        min_price=min(t)

        for i in range(n):
            if (t[i]-min_price)%k!=0:#onko erotus jaollinen k:lla
                return -1
            total_diff+=t[i]-min_price#hinnanmuutostarve

        return total_diff//k



if __name__ =='__main__':
    n,k=(map(int,input().split()))
    t=list(map(int, input().split()))
    cases=[n,k,t]

    test_class=XXX2(cases)
    print(test_class.XXX())
