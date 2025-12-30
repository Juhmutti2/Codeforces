'''

A. Compote
time limit per test1 second
memory limit per test256 megabytes
Nikolay has a lemons, b apples and c pears. He decided to cook a compote. According to the recipe the fruits should be in the ratio 1: 2: 4. It means that for each lemon in the compote should be exactly 2 apples and exactly 4 pears. You can't crumble up, break up or cut these fruits into pieces. These fruits — lemons, apples and pears — should be put in the compote as whole fruits.

Your task is to determine the maximum total number of lemons, apples and pears from which Nikolay can cook the compote. It is possible that Nikolay can't use any fruits, in this case print 0.

Input
The first line contains the positive integer a (1 ≤ a ≤ 1000) — the number of lemons Nikolay has.

The second line contains the positive integer b (1 ≤ b ≤ 1000) — the number of apples Nikolay has.

The third line contains the positive integer c (1 ≤ c ≤ 1000) — the number of pears Nikolay has.

Output
Print the maximum total number of lemons, apples and pears from which Nikolay can cook the compote.

Examples
InputCopy
2
5
7
OutputCopy
7
InputCopy
4
7
13
OutputCopy
21
InputCopy
2
3
2
OutputCopy
0
Note
In the first example Nikolay can use 1 lemon, 2 apples and 4 pears, so the answer is 1 + 2 + 4 = 7.

In the second example Nikolay can use 3 lemons, 6 apples and 12 pears, so the answer is 3 + 6 + 12 = 21.

In the third example Nikolay don't have enough pears to cook any compote, so the answer is 0.


SYÖTE
a=sitruunat
b=omenat
c=päärynät


KOMPAKTI
Montako hedelmää voidaan käyttää kun tarvesuhde on a=1:b=2:c=4 

RATKAISU

iteroidaan läpi 1-1000 hedelmää (raja-arvot), ja lasketaan kustakin hedelmästä onko niitä tarvittava määrä. 

GPT 4.0 TARJOAA

def max_fruits(a, b, c):
    sets = min(a, b // 2, c // 4)
    return sets * 7

# Syötteen luku
if __name__ == '__main__':
    a = int(input())  # lemons
    b = int(input())  # apples
    c = int(input())  # pears
    print(max_fruits(a, b, c))

GPT etsii pienimmän mahdollisen jakajan luvuista. GPT:n koodi on laajennettavissa isommalle kokonaismäärälle, oma vain rajallisesti ratkaisun aikavaatimuksen vuoksi.  
Kuitenkin tällä lukumäärällä oma koodi on nopeampi, johtuen GPT:n min() käytöstä. 


SUORITUS STATISTIIKKA
GPT 93 ms	200 KB
OMA 77 ms	200 KB

LINKKI
https://codeforces.com/problemset/problem/746/A

'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):
        a,b,c=cases
        result=0

        for i in range(1,1000):
            if c-i*4>=0 and b-i*2>=0 and a>=i:
                if i>result:
                    result=i
        
        return result*7#Muistetaan palauttaa hedelmien määrä. 

if __name__ =='__main__':
    a=int(input())
    b=int(input())
    c=int(input())
    cases=[a,b,c]

    test_class=XXX2(cases)
    print(test_class.XXX())
