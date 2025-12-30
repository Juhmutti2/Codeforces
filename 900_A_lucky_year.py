'''

A. Lucky Year
time limit per test1 second
memory limit per test256 megabytes
Apart from having lots of holidays throughout the year, residents of Berland also have whole lucky years. Year is considered lucky if it has no more than 1 non-zero digit in its number. So years 100, 40000, 5 are lucky and 12, 3001 and 12345 are not.

You are given current year in Berland. Your task is to find how long will residents of Berland wait till the next lucky year.

Input
The first line contains integer number n (1 ≤ n ≤ 109) — current year in Berland.

Output
Output amount of years from the current year to the next lucky one.

Examples
InputCopy
4
OutputCopy
1
InputCopy
201
OutputCopy
99
InputCopy
4000
OutputCopy
1000
Note
In the first example next lucky year is 5. In the second one — 300. In the third — 5000.


SYÖTE
yksi luku, nykyinen vuosi

KOMPAKTI
Onnekas vuosi on vuosi, jossa on vain yksi 1-9 ja muut nollia. 

RATKAISU
Hyödynnetään kymmenpotenssia ja luvun pituutta.
vastaus on aina:
(10**len(cases)-1)-luku josta on poistettu ensimmäinen numero
Ohjelmallisesti alle kymmenenen oleva luku vaatii erityiskäsittelyn. alla lähestytty try - except lohkolla.  

GPT 4.0 TARJOAA

def next_lucky_year(n):
    power = 1
    while True:
        candidate = ((n // power) + 1) * power
        if str(candidate).count('0') >= len(str(candidate)) - 1:#Tämä on erittäin omituinen ehto
            return candidate - n
        power *= 10

n = int(input())
print(next_lucky_year(n))

GPT tarjoaa iteraatiota, joka on täysin tarpeeton ja hiukan sekava lähestymistapa. Oman ratkaisuni vaatii ymmärryksen kymmenpotenssien toiminnasta. 
Kommentoitu rivi vieläpä tarkistaa erikseen lucky ehdon, joka vaikeuttaa koodin hahmottamista entisestään. "Mikä tämä on?", "Miksi se on tässä?".



SUORITUS STATISTIIKKA
GPT 108 ms	300 KB
OMA 108 ms	300 KB

LINKKI
https://codeforces.com/problemset/problem/808/A

'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):
        potency=10**(len(self.cases)-1)#jos self.cases<10, potency=1

        try:
            last_numbers=int(self.cases[1:])#last numbers määrää aina eron seuraavaan potencyyn, joka = haettu lucky number
        except ValueError:#alle kymmenen antaa value errorin, jolloin pituus =0
            last_numbers=0

        return potency-last_numbers

if __name__ =='__main__':
    cases=input()

    test_class=XXX2(cases)
    print(test_class.XXX())