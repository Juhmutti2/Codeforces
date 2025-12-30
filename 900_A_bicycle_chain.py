'''
A. Bicycle Chain
time limit per test2 seconds
memory limit per test256 megabytes
Vasya's bicycle chain drive consists of two parts: n stars are attached to the pedal axle, m stars are attached to the rear wheel axle. The chain helps to rotate the rear wheel by transmitting the pedal rotation.

We know that the i-th star on the pedal axle has ai (0 < a1 < a2 < ... < an) teeth, and the j-th star on the rear wheel axle has bj (0 < b1 < b2 < ... < bm) teeth. Any pair (i, j) (1 ≤ i ≤ n; 1 ≤ j ≤ m) is called a gear and sets the indexes of stars to which the chain is currently attached. Gear (i, j) has a gear ratio, equal to the value .

Since Vasya likes integers, he wants to find such gears (i, j), that their ratios are integers. On the other hand, Vasya likes fast driving, so among all "integer" gears (i, j) he wants to choose a gear with the maximum ratio. Help him to find the number of such gears.

In the problem, fraction  denotes division in real numbers, that is, no rounding is performed.

Input
The first input line contains integer n (1 ≤ n ≤ 50) — the number of stars on the bicycle's pedal axle. The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 104) in the order of strict increasing.

The third input line contains integer m (1 ≤ m ≤ 50) — the number of stars on the rear wheel axle. The fourth line contains m integers b1, b2, ..., bm (1 ≤ bi ≤ 104) in the order of strict increasing.

It is guaranteed that there exists at least one gear (i, j), that its gear ratio is an integer. The numbers on the lines are separated by spaces.

Output
Print the number of "integer" gears with the maximum ratio among all "integer" gears.

Examples
InputCopy
2
4 5
3
12 13 15
OutputCopy
2
InputCopy
4
1 2 3 4
5
10 11 12 13 14
OutputCopy
1
Note
In the first sample the maximum "integer" gear ratio equals 3. There are two gears that have such gear ratio. For one of them a1 = 4, b1 = 12, and for the other a2 = 5, b3 = 15.




KOMPAKTI
Halutaan löytää suurin välitys, eli maxtakalistan jäsen /etulistan jäsen)

RATKAISU
Iteroidaan eturatas ja takaratas., katsotaan onko nykyinen välitys suurempi tasaluku kuin aiempi maksimi. 
GPT 4.0 TARJOAA

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

max_ratio = 0
count = 0

for ai in a:
    for bj in b:
        if bj % ai == 0:
            ratio = bj // ai
            if ratio > max_ratio:
                max_ratio = ratio
                count = 1
            elif ratio == max_ratio:
                count += 1

print(count)

GPT ratkaisu on käytännössä sama, mutta mielenkiintoisesti nopeampi. 
Ero syntyy todennäköisesti siitä, että kokonaislukujen käsittely on nopeampaa. 
GPT siis käyttää kokonaislukuja ja mun versio liukulukuja. 


SUORITUS STATISTIIKKA
GPT 186 ms	1500 KB
OMA 216 ms	1500 KB

LINKKI
https://codeforces.com/problemset/problem/215/A

'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):
        max_gear=0
        total=0
        front,rear=self.cases

        for gear in front:
            for cog in rear:
                current=cog/gear
                if current>max_gear and current%1==0:
                    max_gear=current
                    total=1#nollataan
                elif current==max_gear and current%1==0:
                    total+=1

        return total

if __name__ =='__main__':
    n=int(input())
    front=list(map(int,input().split()))
    m=int(input())
    rear=list(map(int,input().split()))
    cases=[front,rear]




    test_class=XXX2(cases)
    print(test_class.XXX())
