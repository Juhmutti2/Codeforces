'''
A. Bank Robbery
time limit per test2 seconds
memory limit per test256 megabytes
A robber has attempted to rob a bank but failed to complete his task. However, he had managed to open all the safes.

Oleg the bank client loves money (who doesn't), and decides to take advantage of this failed robbery and steal some money from the safes. There are many safes arranged in a line, where the i-th safe from the left is called safe i. There are n banknotes left in all the safes in total. The i-th banknote is in safe xi. Oleg is now at safe a. There are two security guards, one of which guards the safe b such that b < a, i.e. the first guard is to the left of Oleg. The other guard guards the safe c so that c > a, i.e. he is to the right of Oleg.

The two guards are very lazy, so they do not move. In every second, Oleg can either take all the banknotes from the current safe or move to any of the neighboring safes. However, he cannot visit any safe that is guarded by security guards at any time, becaues he might be charged for stealing. Determine the maximum amount of banknotes Oleg can gather.

Input
The first line of input contains three space-separated integers, a, b and c (1 ≤ b < a < c ≤ 109), denoting the positions of Oleg, the first security guard and the second security guard, respectively.

The next line of input contains a single integer n (1 ≤ n ≤ 105), denoting the number of banknotes.

The next line of input contains n space-separated integers x1, x2, ..., xn (1 ≤ xi ≤ 109), denoting that the i-th banknote is located in the xi-th safe. Note that xi are not guaranteed to be distinct.

Output
Output a single integer: the maximum number of banknotes Oleg can take.

Examples
InputCopy
5 3 7
8
4 7 5 5 3 6 2 8
OutputCopy
4
InputCopy
6 5 7
5
1 5 7 92 3
OutputCopy
0
Note
In the first example Oleg can take the banknotes in positions 4, 5, 6 (note that there are 2 banknotes at position 5). Oleg can't take the banknotes in safes 7 and 8 because he can't run into the second security guard. Similarly, Oleg cannot take the banknotes at positions 3 and 2 because he can't run into the first security guard. Thus, he can take a maximum of 4 banknotes.

For the second sample, Oleg can't take any banknotes without bumping into any of the security guards.


SYÖTE
a,b,c
n
x
a=Rosvon sijainti(oleg)
b ja c= paikallaan olevien vartijoiden sijainnit
n=setelien määrä
x=lista setelien sijainneista


KOMPAKTI
Montako seteliä rosvo voi kähveltää?


RATKAISU
Lasketaan osavälimäärä sum() avulla.
Huom, tässä muuttujat on jätetty hyvin vaikeasti tulkittaviksi kirjaimiksi. 

GPT 4.0 TARJOAA

# Luetaan syöte
a, b, c = map(int, input().split())
n = int(input())
x = list(map(int, input().split()))

# Lasketaan, kuinka monta seteliä on välillä (b, c)
count = sum(1 for pos in x if b < pos < c)

# Tulostetaan vastaus
print(count)

GPT tarjoaa täysin samaa ratkaisua



SUORITUS STATISTIIKKA
GPT 155 ms	13700 KB
OMA 155 ms	14400 KB

LINKKI
https://codeforces.com/problemset/problem/794/A



'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):

        a,b,c,n,x=cases#Otettu selkeyden vuoksi kaikki muuttujat mukaan vaikka osa on turhia. Tuotantokoodissa turhat pois ja tolkulliset nimet tilalle. 
        x_sum=sum(1 for y in x if b<y<c)#jos x:n alkio(=y) on vartijoiden b ja c välissä. 

        return x_sum

if __name__ =='__main__':
    cases=[]
    a,b,c=map(int,input().split())
    n=int(input())
    x=list(map(int, input().split()))
    cases=[a,b,c,n,x]



    test_class=XXX2(cases)
    print(test_class.XXX())
