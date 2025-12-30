'''
B. Roadside Trees (Simplified Edition)
time limit per test2 seconds
memory limit per test256 megabytes
Squirrel Liss loves nuts. There are n trees (numbered 1 to n from west to east) along a street and there is a delicious nut on the top of each tree. The height of the tree i is hi. Liss wants to eat all nuts.

Now Liss is on the root of the tree with the number 1. In one second Liss can perform one of the following actions:

Walk up or down one unit on a tree.
Eat a nut on the top of the current tree.
Jump to the next tree. In this action the height of Liss doesn't change. More formally, when Liss is at height h of the tree i (1 ≤ i ≤ n - 1), she jumps to height h of the tree i + 1. This action can't be performed if h > hi + 1.
Compute the minimal time (in seconds) required to eat all nuts.

Input
The first line contains an integer n (1  ≤  n ≤ 105) — the number of trees.

Next n lines contains the height of trees: i-th line contains an integer hi (1 ≤ hi ≤ 104) — the height of the tree with the number i.

Output
Print a single integer — the minimal time required to eat all nuts in seconds.

Examples
InputCopy
2
1
2
OutputCopy
5
InputCopy
5
2
1
2
1
1
OutputCopy
14


KOMPAKTI
n=puiden määrä
a=lista puiden korkeuksista
Halutaan minimiajassa syödä kaikki pähkinät puiden huipuilta. Kurre goes "omnonomnom"
toiminnot per sekunti:
yhden yksikön ylös tai alas. 
syödä pähkinä
hypätä seuraavaan puuhun samalle korkeudelle kuin millä oli. 
ei voida hypätä korkeammasta puusta alas. Täytyy tulla alas ensin. 




RATKAISU
Iteroidaan jokainen puuväli.

GPT 4.0 TARJOAA

n = int(input())
heights = [int(input()) for _ in range(n)]

time = heights[0] + 1  # climb first + eat

for i in range(1, n):
    time += 1  # jump to next tree
    time += abs(heights[i] - heights[i - 1])  # climb up or down
    time += 1  # eat nut

print(time)

GPT tarjoaa koodillisesti hiukan kompaktimpaa ratkaisua joka on suhteellisesti aavistuksen hitaampi (n. 6,5%) mutta millisekunneissa 32.
Ero syntyy siitä, että GPT käyttää tarpeettomasti abs(). Näillä reunaehdoilla suorituskyvyllä ei ole olennaista eroa, 
mutta koodi on esimerkki siitä että tarpeettomia funktiokutsuja kannattaa välttää. 


SUORITUS STATISTIIKKA
GPT 498 ms	8400 KB
OMA 466 ms	8500 KB

LINKKI
https://codeforces.com/problemset/problem/265/B

'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):
        n,a=self.cases
        seconds=a[0]+1#ensimmäisen puuhun kuluvat sekunnit. 
        #Alla olevassa iteraatiossa +2=syönti&hyppy. 
        for i in range(n-1):
            if a[i]>a[i+1]:#edellinen puu korkeampi
                seconds+=a[i]-a[i+1]+2#palataan seuraavan puu maksimikorkeuteen ja syödään
            elif a[i]<a[i+1]:#edellinen puu matalampi
                seconds+=a[i+1]-a[i]+2#hypätään puuhun, kiivetään ylös ja syödään. 
            else:#puut saman pituisia
                seconds+=2
            

        return seconds

if __name__ =='__main__':
    n=int(input())
    a=[]
    for _ in range(n):
        a.append(int(input()))
    cases=[n,a]



    test_class=XXX2(cases)
    print(test_class.XXX())
