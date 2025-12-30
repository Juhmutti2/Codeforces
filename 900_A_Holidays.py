'''

A. Holidays
time limit per test1 second
memory limit per test256 megabytes
On the planet Mars a year lasts exactly n days (there are no leap years on Mars). But Martians have the same weeks as earthlings — 5 work days and then 2 days off. Your task is to determine the minimum possible and the maximum possible number of days off per year on Mars.

Input
The first line of the input contains a positive integer n (1 ≤ n ≤ 1 000 000) — the number of days in a year on Mars.

Output
Print two integers — the minimum possible and the maximum possible number of days off per year on Mars.

Examples
InputCopy
14
OutputCopy
4 4
InputCopy
2
OutputCopy
0 2
Note
In the first sample there are 14 days in a year on Mars, and therefore independently of the day a year starts with there will be exactly 4 days off .

In the second sample there are only 2 days in a year on Mars, and they can both be either work days or days off.

KOMPAKTI
Montako vapaapäivää on Marsin vuodessa kun syöte on Marsin vuoden päivät ja vapaapäivä noudattaa kaavaa:
5 töitä 2 vapaata

RATKAISU
Lasketaan enemmän, ohjelmoidaan vähemmän.

KTS DOCSTRING
Kuuden jakojäännös muodostaa erikoistilanteen jossa on aina vähintään 1 vapaa mukana. 
Kaikilla muilla jakojäännöksilla vapaapäivien määrä on 0,1 tai 2 riippuen jakojäännöksestä. 

GPT 4.0 TARJOAA

n = int(input())
weeks = n // 7
extra = n % 7

min_holidays = weeks * 2 + (1 if extra == 6 else 0)
max_holidays = weeks * 2 + min(2, extra)

print(min_holidays, max_holidays)

GPT on nopeampi mutta logiikka on mielestäni vaikeaselkoisempi, ainakin ilman kommentointia. Miksei suoraan käytetä divmod()? 
Suoritusero selittyy todennäköisesti divmod() ja kahdella if-else haaralla. 


SUORITUS STATISTIIKKA
GPT     93 ms	200 KB
OMA 	124 ms	200 KB

LINKKI
https://codeforces.com/problemset/problem/670/A

'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):

        full_weeks, days=divmod(self.cases, 7)
        min_days=full_weeks*2
        max_days=full_weeks*2
        if days==6:#KTS DOCSTRING 1
            min_days+=1
            max_days+=2
        else:
            max_days+=min(days, 2)
        return f"{min_days} {max_days}"

if __name__ =='__main__':
    cases=int(input())

    test_class=XXX2(cases)
    print(test_class.XXX())
