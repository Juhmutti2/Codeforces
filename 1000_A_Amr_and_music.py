'''
A. Amr and Music
time limit per test1 second
memory limit per test256 megabytes
Amr is a young coder who likes music a lot. He always wanted to learn how to play music but he was busy coding so he got an idea.

Amr has n instruments, it takes ai days to learn i-th instrument. Being busy, Amr dedicated k days to learn how to play the maximum possible number of instruments.

Amr asked for your help to distribute his free days between instruments so that he can achieve his goal.

Input
The first line contains two numbers n, k (1 ≤ n ≤ 100, 0 ≤ k ≤ 10 000), the number of instruments and number of days respectively.

The second line contains n integers ai (1 ≤ ai ≤ 100), representing number of days required to learn the i-th instrument.

Output
In the first line output one integer m representing the maximum number of instruments Amr can learn.

In the second line output m space-separated integers: the indices of instruments to be learnt. You may output indices in any order.

if there are multiple optimal solutions output any. It is not necessary to use all days for studying.

Examples
InputCopy
4 10
4 3 1 2
OutputCopy
4
1 2 3 4
InputCopy
5 6
4 3 1 1 2
OutputCopy
3
1 3 4
InputCopy
1 3
4
OutputCopy
0
Note
In the first test Amr can learn all 4 instruments.

In the second test other possible solutions are: {2, 3, 5} or {3, 4, 5}.

In the third test Amr doesn't have enough time to learn the only presented instrument.a


KOMPAKTI
n,k
t
n=soittimien määrä
k=käytössä olevat päivät
t=lista soittimien oppimiseen tarvittavista päivistä

Kuinka monta soitinta ehditään oppimaan? Tulostetaan määrä ja soittimien indeksit


RATKAISU
perustehtävä on helppo. Haastetta tuottaa, jos tuottaa, indeksien palautus. 


GPT 4.0 TARJOAA

class AmrMusic:
    def __init__(self, n, k, a):
        self.n = n
        self.k = k
        self.a = a

    def solve(self):
        # Tallenna indeksit ja opiskelupäivät tupleina
        instruments = list(enumerate(self.a, start=1))  # (indeksi, päivät)
        instruments.sort(key=lambda x: x[1])  # Järjestetään opiskelupäivien mukaan

        total_days = 0
        learned = []

        for idx, days in instruments:
            if total_days + days <= self.k:
                total_days += days
                learned.append(idx)
            else:
                break

        print(len(learned))
        if learned:
            print(*learned)


if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    solution = AmrMusic(n, k, a)
    solution.solve()

Lähestysmistapa on pitkälti sama. Hiukan hitaampi mutta ei yhtä muistisyöppö. 


SUORITUS STATISTIIKKA
GPT 108 ms	200 KB
OMA 93 ms	1500 KB

LINKKI
https://codeforces.com/problemset/problem/507/A

'''





class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):
        n,k,t=cases
        ref=list(t)#Todellinen kopio, joka ei muutu kun t muuttuu
        t.sort()
        learned=[]
        learned_amount=0
        days=0
        for i in range(n):
            current=t[i]
            days+=current
            if days<=k:
                learned_amount+=1
                index=next(i for i,  v in enumerate(ref) if v== current and i not in learned)#saadaan seuraava indeksi jos samoja listassa.
                learned.append(index) 
            else:
                break
        results=[learned_amount, [i+1 for i in learned]]#1 pohjainen indeksointi

        return results

if __name__ =='__main__':
    n,k=map(int, input().split())
    t=list(map(int,input().split()))
    cases=[n,k,t]



    test_class=XXX2(cases)
    res=test_class.XXX()#Tulostusmuoto
    print(res[0])
    print(*res[1])