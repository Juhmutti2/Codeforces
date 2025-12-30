'''

A. Kitchen Utensils
time limit per test1 second
memory limit per test256 megabytes
The king's birthday dinner was attended by k
 guests. The dinner was quite a success: every person has eaten several dishes (though the number of dishes was the same for every person) and every dish was served alongside with a new set of kitchen utensils.

All types of utensils in the kingdom are numbered from 1
 to 100
. It is known that every set of utensils is the same and consist of different types of utensils, although every particular type may appear in the set at most once. For example, a valid set of utensils can be composed of one fork, one spoon and one knife.

After the dinner was over and the guests were dismissed, the king wondered what minimum possible number of utensils could be stolen. Unfortunately, the king has forgotten how many dishes have been served for every guest but he knows the list of all the utensils left after the dinner. Your task is to find the minimum possible number of stolen utensils.

Input
The first line contains two integer numbers n
 and k
 (1≤n≤100,1≤k≤100
)  — the number of kitchen utensils remaining after the dinner and the number of guests correspondingly.

The next line contains n
 integers a1,a2,…,an
 (1≤ai≤100
)  — the types of the utensils remaining. Equal values stand for identical utensils while different values stand for different utensils.

Output
Output a single value — the minimum number of utensils that could be stolen by the guests.

Examples
InputCopy
5 2
1 2 2 1 3
OutputCopy
1
InputCopy
10 3
1 3 3 1 3 5 5 5 5 100
OutputCopy
14
Note
In the first example it is clear that at least one utensil of type 3
 has been stolen, since there are two guests and only one such utensil. But it is also possible that every person received only one dish and there were only six utensils in total, when every person got a set (1,2,3)
 of utensils. Therefore, the answer is 1
.

One can show that in the second example at least 2
 dishes should have been served for every guest, so the number of utensils should be at least 24
: every set contains 4
 utensils and every one of the 3
 guests gets two such sets. Therefore, at least 14
 objects have been stolen. Please note that utensils of some types (for example, of types 2
 and 4
 in this example) may be not present in the set served for dishes.




KOMPAKTI
Syöte:
n,k
t
n= jäljellä olevat aterimet
k=vieraiden määrä
t=luettelo jäljellä olevista aterimista

Kuinka monta aterinta on vähintään varastettu?

RATKAISU
Tehtävä vaatii suhteessa valtavasti enemmän loogista päättelyä kuin ohjelmointitaitoja. 
meidän on pääteltävä miminissään syötyjen ruokalajien määrä sekä erityyppisten aterimien määrä.

ateriat: Koska joka aterialle on oma numeronsa, pitää tiettyä numeroa olla vähintään vieraiden määrällä jaollinen määrä
esim 2:
10 3
1 3 3 1 3 5 5 5 5 100

vitosia =4kpl. Tästä voimme päätellä että aterioita on ollut 2: 6/3=2 eli kaksi vitosta puuttuu. 

Huomattava on, että maksimista ei voida sanoa näillä tiedoilla yhtään mitään. 
Linnassa on voinut olla pitkäkyntisiä, joilla on pohjattoman suuret säkit. 

Koska tehtävä on puhtaan matemaattinen, 1sek aikaraja ja 256MB muistirajoite ovat puhtaan kosmeettisia.

GPT 4.0 TARJOAA

Mielenkiintoisesti GPT 4.0 ei kykene tuottamaan ratkaisua ilman merkittävää apua logiikan rakennuksessa. 
Tässä näkyy GPT:n heikkous kun logiikka ylittää tietyn monimutkaisuuspisteen. 

GPT o4 MINI HIGH TARJOAA

import math

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    freq = {}
    for x in a:
        freq[x] = freq.get(x, 0) + 1

    m = len(freq)
    maxfreq = max(freq.values())

    d = math.ceil(maxfreq / k)
    stolen = k * d * m - n

    print(stolen)

if __name__ == "__main__":
    solve()

mini high ratkaisu toimii. Se on hiukan hitaampi ja muistitehokkaampi. Logiikaltaan se on monimutkaisempi ja siksi hankalampi ylläpitää.
-> Käyttäisin tuotannossa omaa koodiani seuraavalla varauksella: Mikäli syötteen määrä olisi potentiaalisesti hyvin suuri tai edes keskikokoinen, täytyisi tehokkuus tarkistaa. 
Tässä n jää suorastaan häviävän pieneksi (kaikki <=100). Näillä raja-arvoilla oma versioni on ylläpidettävyytensä vuoksi selkeä voittaja. 

SUORITUS STATISTIIKKA
GPT 109 ms	200 KB
OMA 93 ms	900 KB

LINKKI
https://codeforces.com/problemset/problem/1032/A

'''

import math
from collections import Counter

class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):
        n,k,t=cases
        meals=math.ceil(max(Counter(t).values())/k)
        diff_types=len(set(t))
        total_utensils=meals*k*diff_types
        return total_utensils-n

if __name__ =='__main__':
    n,k=map(int, input().split())
    t=list(map(int,input().split()))
    cases=[n,k,t]


    test_class=XXX2(cases)
    print(test_class.XXX())
