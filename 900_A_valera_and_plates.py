'''

A. Valera and Plates
time limit per test1 second
memory limit per test256 megabytes
Valera is a lazy student. He has m clean bowls and k clean plates.

Valera has made an eating plan for the next n days. As Valera is lazy, he will eat exactly one dish per day. At that, in order to eat a dish, he needs exactly one clean plate or bowl. We know that Valera can cook only two types of dishes. He can eat dishes of the first type from bowls and dishes of the second type from either bowls or plates.

When Valera finishes eating, he leaves a dirty plate/bowl behind. His life philosophy doesn't let him eat from dirty kitchenware. So sometimes he needs to wash his plate/bowl before eating. Find the minimum number of times Valera will need to wash a plate/bowl, if he acts optimally.

Input
The first line of the input contains three integers n, m, k (1 ≤ n, m, k ≤ 1000) — the number of the planned days, the number of clean bowls and the number of clean plates.

The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 2). If ai equals one, then on day i Valera will eat a first type dish. If ai equals two, then on day i Valera will eat a second type dish.

Output
Print a single integer — the minimum number of times Valera will need to wash a plate/bowl.

Examples
InputCopy
3 1 1
1 2 1
OutputCopy
1
InputCopy
4 3 1
1 1 1 1
OutputCopy
1
InputCopy
3 1 2
2 2 2
OutputCopy
0
InputCopy
8 2 2
1 2 1 2 1 2 1 2
OutputCopy
4
Note
In the first sample Valera will wash a bowl only on the third day, so the answer is one.

In the second sample, Valera will have the first type of the dish during all four days, and since there are only three bowls, he will wash a bowl exactly once.

In the third sample, Valera will have the second type of dish for all three days, and as they can be eaten from either a plate or a bowl, he will never need to wash a plate/bowl.


SYÖTE
n,m,k
a lista 

n= päivien määrä
m=kuppien määrä
k=lautasten määrä
a= lista onko päivän ruoka 1(=kuppi) vai 2(=kuppi / lautanen)

KOMPAKTI
Kun 2 ruuan voi syödä joko kupista tai lautaselta, 1 ruuan vain kupista ja aina pitää olla puhdas astia, montako astiaa pitää vähintään tiskata?

RATKAISU
Tehtävän voi ratkaista joko laskemalla tai iteroimalla. Koska aika-raja on 1sek ja n <=1000, iteraatio on aivan riittävä lähestymistapa. Lisäksi yhtälöittäminen on hiukan vaativampaa. 
Haluttu käyttää omassa versiossa matemaattista lähestymistapaa ohjelmallisen laskemisen taitojen parantamiseksi. 


GPT 4.0 TARJOAA


n, m, k = map(int, input().split())  # n=päivät, m=kulhot, k=lautaset
a = list(map(int, input().split()))

wash_count = 0

for dish in a:
    if dish == 1:
        if m > 0:
            m -= 1
        else:
            wash_count += 1
    else:  # dish == 2
        if k > 0:
            k -= 1
        elif m > 0:
            m -= 1
        else:
            wash_count += 1

print(wash_count)

GPT tarjoilee iteratiivisen lähestymistavan, josta puuttuu kommentit, mutta joka on selkeä kunhan muuttujien sisältö avautuu lukijalle. 
Kommentoimatta GPT:n koodia ei tietenkään voisi tuotantoon lyödä, paitsi jos vihaa ylläpitäjiä palavasti. 

SUORITUS STATISTIIKKA
GPT 108 ms	300 KB
OMA 108 ms	300 KB

LINKKI
https://codeforces.com/problemset/problem/369/A

'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):
        m,k,a=self.cases
        bowls=a.count(1)-m#positiivinen =tiskaustarve, negatiivinen = ylijäämä
        plates=(a.count(2)-k)+min(bowls,0)#lisätään bowls vain jos bolws<0
        
        return max(bowls,0)+max(plates,0)#Koska molemmissa muuttujissa positiivinen on tiskaustarve. 




if __name__ =='__main__':

    n,m,k=map(int,input().split())
    a=list(map(int, input().split()))
    cases=[m,k,a]

    test_class=XXX2(cases)
    print(test_class.XXX())
