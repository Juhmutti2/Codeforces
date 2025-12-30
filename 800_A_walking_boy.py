'''

A. Walking Boy
time limit per test2 seconds
memory limit per test256 megabytes
One of the SWERC judges has a dog named Boy. Besides being a good competitive programmer, Boy loves fresh air, so she wants to be walked at least twice a day. Walking Boy requires 120
 consecutive minutes. Two walks cannot overlap, but one can start as soon as the previous one has finished.


Boy before and after getting ACCEPTED on this problem.

Today, the judge sent n
 messages to the SWERC Discord server. The i
-th message was sent ai
 minutes after midnight. You know that, when walking Boy, the judge does not send any messages, but he can send a message right before or right after a walk. Is it possible that the judge walked Boy at least twice today?

Note that a day has 1440
 minutes, and a walk is considered to happen today if it starts at a minute s≥0
 and ends right before a minute e≤1440
. In that case, it must hold that e−s=120
 and, for every i=1,2…,n
, either ai≤s
 or ai≥e
.

Input
Each test contains multiple test cases. The first line contains an integer t
 (1≤t≤100
) — the number of test cases. The descriptions of the t
 test cases follow.

The first line of each test case contains an integer n
 (1≤n≤100
) — the number of messages sent by the judge.

The second line of each test case contains n
 integers a1,a2,…,an
 (0≤a1<a2<⋯<an<1440
) — the times at which the messages have been sent (in minutes elapsed from midnight).

Output
For each test case, output one line containing YES
 if it is possible that Boy has been walked at least twice, and NO
 otherwise.

Example
InputCopy
6
14
100 200 300 400 500 600 700 800 900 1000 1100 1200 1300 1400
12
100 200 300 400 600 700 800 900 1100 1200 1300 1400
13
100 200 300 400 500 600 700 800 900 1100 1200 1300 1400
13
101 189 272 356 463 563 659 739 979 1071 1170 1274 1358
1
42
5
0 1 2 3 40
OutputCopy
NO
YES
NO
YES
YES
YES


SYÖTE
t
n
a

t=testitapaukset
n=testitapauksen pituus
a=testilista

KOMPAKTI
Ulkoilutetaanko koirulia kahdesti 120min kerrallaan kun omistaja säätää puhelimella testilistan minuuteilla.
Kun omistaja säätää puhelimella, koiruli ei ole lenkillä.

RATKAISU
Testataan onko väleissä 120min aukko(=1 lenkki) tai 240min aukko (=2 lenkkiä)

GPT 4.0 TARJOAA

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a = [-1] + a + [1440]  # Lisää alku ja loppu mukaan

    long_enough = 0
    for i in range(1, len(a)):
        gap = a[i] - a[i - 1] - 1
        if gap >= 240:
            long_enough = 2  # Yksi väli riittää kahteen kävelyyn
            break
        elif gap >= 120:
            long_enough += 1

    print("YES" if long_enough >= 2 else "NO")

    
GPT vaatii useamman promptauksen ennen onnistumista. Logiikka on sama, mutta suorituskyky hitaampi.  

SUORITUS STATISTIIKKA
GPT 93 ms	1700 KB
OMA 62 ms	1700 KB

LINKKI
https://codeforces.com/problemset/problem/1776/A

'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):
        results=[]  
        for a in self.cases:
            if not 0 in a:#Päivän alku jos ei ole
                a.append(0)
            if not 1440 in a:#Päivän loppu jos ei ole 
                a.append(1440)
            a.sort()#Lenkkien järjestäminen. 
            counter=0
            for i in range(len(a)-1):#Koska ehdolliset yllä, voidaan vertailla suoraan perättäisiä arvoja. 
                if 240>a[i+1]-a[i]>=120:
                    counter+=1
                elif a[i+1]-a[i]>=240:
                    counter+=2
                    #Mielenkiintoisesti break komento tässä hidastaisi koodin ad 93ms eli suhteellisesti valtavasti
            if counter>=2:#vaaditaan 2 mutta voidaan päätyä mihin tahansa yli kahden counter lukuun. 
                results.append('YES')
            else:
                results.append('NO')

        return "\n".join(results)

if __name__ =='__main__':
    cases=[]
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int, input().split()))#Mielenkiintoisesti tämän muuttaminen append() sisään hidastaisi koodia ad. 77ms
        cases.append(a)

    test_class=XXX2(cases)
    print(test_class.XXX())
