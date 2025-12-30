'''

A. Minimum Difficulty
time limit per test2 seconds
memory limit per test256 megabytes
Mike is trying rock climbing but he is awful at it.

There are n holds on the wall, i-th hold is at height ai off the ground. Besides, let the sequence ai increase, that is, ai < ai + 1 for all i from 1 to n - 1; we will call such sequence a track. Mike thinks that the track a1, ..., an has difficulty . In other words, difficulty equals the maximum distance between two holds that are adjacent in height.

Today Mike decided to cover the track with holds hanging on heights a1, ..., an. To make the problem harder, Mike decided to remove one hold, that is, remove one element of the sequence (for example, if we take the sequence (1, 2, 3, 4, 5) and remove the third element from it, we obtain the sequence (1, 2, 4, 5)). However, as Mike is awful at climbing, he wants the final difficulty (i.e. the maximum difference of heights between adjacent holds after removing the hold) to be as small as possible among all possible options of removing a hold. The first and last holds must stay at their positions.

Help Mike determine the minimum difficulty of the track after removing one hold.

Input
The first line contains a single integer n (3 ≤ n ≤ 100) — the number of holds.

The next line contains n space-separated integers ai (1 ≤ ai ≤ 1000), where ai is the height where the hold number i hangs. The sequence ai is increasing (i.e. each element except for the first one is strictly larger than the previous one).

Output
Print a single number — the minimum difficulty of the track after removing a single hold.

Examples
InputCopy
3
1 4 6
OutputCopy
5
InputCopy
5
1 2 3 4 5
OutputCopy
2
InputCopy
5
1 2 3 7 8
OutputCopy
4
Note
In the first sample you can remove only the second hold, then the sequence looks like (1, 6), the maximum difference of the neighboring elements equals 5.

In the second test after removing every hold the difficulty equals 2.

In the third test you can obtain sequences (1, 3, 7, 8), (1, 2, 7, 8), (1, 2, 3, 8), for which the difficulty is 4, 5 and 5, respectively. Thus, after removing the second element we obtain the optimal answer — 4.



KOMPAKTI
Mikä jää sarjan pienimmäksi väliksi kun siitä voidaan poistaa yksi arvo. Ensimmäistä ja viimeistä ei saa poistaa. 

RATKAISU
Iteroidaan pienin i ja i+2 väli. Poistetaan pienimmästä välistä indeksin i+1 arvo. 
Mikäli kyseinen väli on 2, lopetetaan ja poistetaan se. 

GPT 4.0 TARJOAA

n = int(input())
a = list(map(int, input().split()))

min_difficulty = float('inf')

for i in range(1, n - 1):  # poistetaan a[i], ei saa olla eka eikä vika
    temp = a[:i] + a[i+1:]  # poistetaan yksi välikahva
    max_diff = 0
    for j in range(1, len(temp)):
        max_diff = max(max_diff, temp[j] - temp[j-1])
    min_difficulty = min(min_difficulty, max_diff)

print(min_difficulty)

GPT testaa jokaista poistoväliä, tästä suoritusero. 

SUORITUS STATISTIIKKA
GPT 77 ms	1500 KB
OMA 77 ms	200 KB

LINKKI
https://codeforces.com/problemset/problem/496/A

'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):
        n, numbers=self.cases
        min_diff=float('inf')
        index=None

        for i in range(n-2):#Iteroidaan pienin poistoväli
            current=numbers[i+2]-numbers[i]
            if current<min_diff:
                min_diff=current
                index=i+1
                if current==2:#tätä pienempää ei voi olla.
                    break
        del numbers[index]#Poistetaan haluttu arvo
        max_diff=0
        for i in range(n-2):#Muuten 1, mutta koska sieltä on poistettu 1, niin siksi -2
            current=numbers[i+1]-numbers[i]#Katsotaan maksimiarvo
            if current>max_diff:
                max_diff=current
        return max_diff




if __name__ =='__main__':
    n=int(input())
    numbers=list(map(int, input().split()))
    cases=[n, numbers]



    test_class=XXX2(cases)
    print(test_class.XXX())
