'''
A. Laptops
time limit per test1 second
memory limit per test256 megabytes
One day Dima and Alex had an argument about the price and quality of laptops. Dima thinks that the more expensive a laptop is, the better it is. Alex disagrees. Alex thinks that there are two laptops, such that the price of the first laptop is less (strictly smaller) than the price of the second laptop but the quality of the first laptop is higher (strictly greater) than the quality of the second laptop.

Please, check the guess of Alex. You are given descriptions of n laptops. Determine whether two described above laptops exist.

Input
The first line contains an integer n (1 ≤ n ≤ 105) — the number of laptops.

Next n lines contain two integers each, ai and bi (1 ≤ ai, bi ≤ n), where ai is the price of the i-th laptop, and bi is the number that represents the quality of the i-th laptop (the larger the number is, the higher is the quality).

All ai are distinct. All bi are distinct.

Output
If Alex is correct, print "Happy Alex", otherwise print "Poor Alex" (without the quotes).

Examples
InputCopy
2
1 2
2 1
OutputCopy
Happy Alex


KOMPAKTI
n määrä lukupareja. 
A_i, B_i

Onko syötteessä kaksi lukuparia joissa A_i1<B_1 ja A_i2>A_i1 ja B_i1>B_i2

RATKAISU

Ratkaisun avain on ehdossa "(1 ≤ ai, bi ≤ n)" sekä rivissä "All ai are distinct. All bi are distinct." Tästä seuraa, että mikäli yksikin lukupari ei ole esim 4,4 tai 1,1 ehto toteutuu. 
Myös n=10^5 ja aikaraja 1sek viittaavat siihen, että valtavan monimutkaista iterointia ei voida suorittaa. 
Tämä on huomionarvoista, koska matemaattinen iterointi tarvitsisi äkkiä erittäin monimutkaisia ehtoja. 


GPT 4.0 TARJOAA

n = int(input())
laptops = [tuple(map(int, input().split())) for _ in range(n)]

# Järjestetään hinnan mukaan nousevasti
laptops.sort()

# Etsitään kohta, jossa laatu pienenee, vaikka hinta nousee
for i in range(n - 1):
    if laptops[i][1] > laptops[i + 1][1]:
        print("Happy Alex")
        break
else:
    print("Poor Alex")



SUORITUS STATISTIIKKA
GPT 530 ms	13700 KB
OMA 296 ms	15800 KB

Mielenkiintoisesti GPT väitttää, että oma ratkaisuni ei voi toimia. GPT ei selvästikään huomioinut reunaehtoja riittävän tarkasti. 
Tämä on hiukan yllättävää, sillä tehtävä ei ole monimutkainen. Yleensä GPT suoriutuu suoraviivaisista matemaattisista toimeksiannoista paremmin. 

LINKKI
https://codeforces.com/problemset/problem/456/A

'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):

        for a,b in self.cases:
            if a!=b:
                return "Happy Alex"
        return "Poor Alex"


if __name__ =='__main__':
    cases=[]
    n=int(input())

    for _ in range(n):
        cases.append(tuple(map(int, input().split())))



    test_class=XXX2(cases)
    print(test_class.XXX())
