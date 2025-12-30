'''
A. Bear and Three Balls
time limit per test2 seconds
memory limit per test256 megabytes
Limak is a little polar bear. He has n balls, the i-th ball has size ti.

Limak wants to give one ball to each of his three friends. Giving gifts isn't easy — there are two rules Limak must obey to make friends happy:

No two friends can get balls of the same size.
No two friends can get balls of sizes that differ by more than 2.
For example, Limak can choose balls with sizes 4, 5 and 3, or balls with sizes 90, 91 and 92. But he can't choose balls with sizes 5, 5 and 6 (two friends would get balls of the same size), and he can't choose balls with sizes 30, 31 and 33 (because sizes 30 and 33 differ by more than 2).

Your task is to check whether Limak can choose three balls that satisfy conditions above.

Input
The first line of the input contains one integer n (3 ≤ n ≤ 50) — the number of balls Limak has.

The second line contains n integers t1, t2, ..., tn (1 ≤ ti ≤ 1000) where ti denotes the size of the i-th ball.

Output
Print "YES" (without quotes) if Limak can choose three balls of distinct sizes, such that any two of them differ by no more than 2. Otherwise, print "NO" (without quotes).

Examples
InputCopy
4
18 55 16 17
OutputCopy
YES
InputCopy
6
40 41 43 44 44 44
OutputCopy
NO
InputCopy
8
5 972 3 4 1 4 970 971
OutputCopy
YES
Note
In the first sample, there are 4 balls and Limak is able to choose three of them to satisfy the rules. He must must choose balls with sizes 18, 16 and 17.

In the second sample, there is no way to give gifts to three friends without breaking the rules.

In the third sample, there is even more than one way to choose balls:

Choose balls with sizes 3, 4 and 5.
Choose balls with sizes 972, 970, 971.


KOMPAKTI
syötteet:
n=testilistan pituus
testilista

Onko testilistassa 3 alkiota jotka ovat peräkkäiset ja max 2 kahden päästä toisistaan? Esim 1,2,3 30,31,32 jne


RATKAISU

tehdään set() joka järjestetään, iteroidaan tästä haluttu ehto
Tässä käytetty ehto, jolla yhden välein nousevista alkioista tehty yhtä suuria. 


GPT 4.0 TARJOAA

n = int(input())
balls = list(map(int, input().split()))

unique = sorted(set(balls))  # poista duplikaatit ja järjestä

for i in range(len(unique) - 2):
    if unique[i+2] - unique[i] <= 2:
        print("YES")
        break
else:
    print("NO")

GPT käyttää samaa logiikkaa hiukan hitaamalla (15%) suorituksella. 
Suoritusaikaeron selittää se, että GPT pyytää joka iteraatiolla len(unique). oman koodin refaktorointi pudottaa suoritusajan ad 108ms.

SUORITUS STATISTIIKKA
GPT 109 ms	300 KB
OMA 93 ms	200 KB

LINKKI
https://codeforces.com/problemset/problem/653/A

'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):

        sorted_set_list=sorted(set(cases))
        n=len(sorted_set_list)#saadaan pieni tehokkuushyöty. 
        found=False

        for i in range(1,n-1):
            if sorted_set_list[i-1]==sorted_set_list[i]-1==sorted_set_list[i+1]-2:#iterointiehto
                found=True
        return 'YES' if found else 'NO'
if __name__ =='__main__':
    n=int(input())
    cases=list(map(int, input().split()))
    



    test_class=XXX2(cases)
    print(test_class.XXX())
