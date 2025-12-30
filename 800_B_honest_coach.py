'''B. Honest Coach
time limit per test2 seconds
memory limit per test256 megabytes
There are n
 athletes in front of you. Athletes are numbered from 1
 to n
 from left to right. You know the strength of each athlete — the athlete number i
 has the strength si
.

You want to split all athletes into two teams. Each team must have at least one athlete, and each athlete must be exactly in one team.

You want the strongest athlete from the first team to differ as little as possible from the weakest athlete from the second team. Formally, you want to split the athletes into two teams A
 and B
 so that the value |max(A)−min(B)|
 is as small as possible, where max(A)
 is the maximum strength of an athlete from team A
, and min(B)
 is the minimum strength of an athlete from team B
.

For example, if n=5
 and the strength of the athletes is s=[3,1,2,6,4]
, then one of the possible split into teams is:

first team: A=[1,2,4]
,
second team: B=[3,6]
.
In this case, the value |max(A)−min(B)|
 will be equal to |4−3|=1
. This example illustrates one of the ways of optimal split into two teams.

Print the minimum value |max(A)−min(B)|
.

Input
The first line contains an integer t
 (1≤t≤1000
) — the number of test cases in the input. Then t
 test cases follow.

Each test case consists of two lines.

The first line contains positive integer n
 (2≤n≤50
) — number of athletes.

The second line contains n
 positive integers s1,s2,…,sn
 (1≤si≤1000
), where si
 — is the strength of the i
-th athlete. Please note that s
 values may not be distinct.

Output
For each test case print one integer — the minimum value of |max(A)−min(B)|
 with the optimal split of all athletes into two teams. Each of the athletes must be a member of exactly one of the two teams.

Example
InputCopy
5
5
3 1 2 6 4
6
2 1 3 2 4 3
4
7 9 3 1
2
1 1000
3
100 150 200
OutputCopy
1
0
2
999
50
Note
The first test case was explained in the statement. In the second test case, one of the optimal splits is A=[2,1]
, B=[3,2,4,3]
, so the answer is |2−2|=0
.

KOMPAKTI:
Mikä on syötteestä rakennettavien listojen A ja B minimi max(A)-min(B) kun säännöt:
Molemmissa vähintään 1 alkio

RATKAISU:
Pienin mahdollinen erotus syötelistan alkioiden välillä. 
Voidaan lajitella, koska indeksiarvoilla ei tehdä mitään. Ainoa merkkaava on erotus. 


GPT 4.0 TARJOILEE:

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = list(map(int, input().split()))
        s.sort()
        min_diff = float('inf')
        for i in range(n - 1):
            min_diff = min(min_diff, s[i + 1] - s[i])#HUOM
        print(min_diff)

if __name__ == "__main__":
    solve()

HUOM: 
Näyttää näppärältä mutta suoritusstatistiikat:
140 ms	3000 KB GPT
109 ms	3000 KB OMA
eli GPT:n ratkaisu on noin 28% hitaampi. Molemmat ovat hyvin nopeita, mutta ero on suhteellisesti merkitsevä.

LINKKI
https://codeforces.com/problemset/problem/1360/B

    

'''

class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):
        results=[]

        for case in self.cases:
            min_diff=float('inf')
            current_diff=float('inf')#Tämä on näköjään tarpeeton. Jälleen kerran, pidän tämän tässä, koska oppiminen. 
            n, case_list=case
            sorted_case=sorted(case_list)
            for i in range(n-1):
                current_diff=abs(sorted_case[i]-sorted_case[i+1])
                if current_diff<min_diff:
                    min_diff=current_diff
                    if current_diff==0:#0= pienin mahdollinen erotus. GPT kehui että on fiksu ratkaisu tämä.  
                        break
            results.append(str(min_diff))



        return "\n".join(results)

if __name__ =='__main__':
    cases=[]
    t=int(input())

    for _ in range(t):
        case=[]
        case.append(int(input()))
        case.append(list(map(int, input().split())))
        cases.append(case)


    test_class=XXX2(cases)
    print(test_class.XXX())
