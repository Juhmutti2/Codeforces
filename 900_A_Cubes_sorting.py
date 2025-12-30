'''
A. Cubes Sorting
time limit per test1 second
memory limit per test256 megabytes
For god's sake, you're boxes with legs! It is literally your only purpose! Walking onto buttons! How can you not do the one thing you were designed for?
Oh, that's funny, is it? Oh it's funny? Because we've been at this for twelve hours and you haven't solved it either, so I don't know why you're laughing. You've got one hour! Solve it!

Wheatley decided to try to make a test chamber. He made a nice test chamber, but there was only one detail absent — cubes.

For completing the chamber Wheatley needs n
 cubes. i
-th cube has a volume ai
.

Wheatley has to place cubes in such a way that they would be sorted in a non-decreasing order by their volume. Formally, for each i>1
, ai−1≤ai
 must hold.

To achieve his goal, Wheatley can exchange two neighbouring cubes. It means that for any i>1
 you can exchange cubes on positions i−1
 and i
.

But there is a problem: Wheatley is very impatient. If Wheatley needs more than n⋅(n−1)2−1
 exchange operations, he won't do this boring work.

Wheatly wants to know: can cubes be sorted under this conditions?

Input
Each test contains multiple test cases.

The first line contains one positive integer t
 (1≤t≤1000
), denoting the number of test cases. Description of the test cases follows.

The first line of each test case contains one positive integer n
 (2≤n≤5⋅104
) — number of cubes.

The second line contains n
 positive integers ai
 (1≤ai≤109
) — volumes of cubes.

It is guaranteed that the sum of n
 over all test cases does not exceed 105
.

Output
For each test case, print a word in a single line: "YES" (without quotation marks) if the cubes can be sorted and "NO" (without quotation marks) otherwise.

Example
InputCopy
3
5
5 3 2 1 4
6
2 2 2 2 2 2
2
2 1
OutputCopy
YES
YES
NO
Note
In the first test case it is possible to sort all the cubes in 7
 exchanges.

In the second test case the cubes are already sorted.

In the third test case we can make 0
 exchanges, but the cubes are not sorted yet, so the answer is "NO".


KOMPAKTI
Voidaanko järjestää numerot (kuutiot) kun voidaan vaihtaa viereisten paikkoja ja maksimiliikeiden määrä on:
((n(n-1))/2)-1
T=tapausten määrä
n=kuutioiden määrä per tapaus
a= lista kuutioista



RATKAISU
Mikäli listassa on yksikin nouseva lukupari tai yhtäsuuri lukupari, se voidaan järjestää ehtojen puitteissa, muuten ei. 
Käytännössä tämä tarkoittaa että selvitämme onko lista vain laskevia lukuja

GPT 4.0 TARJOAA

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    possible = False
    for i in range(1, n):
        if a[i - 1] <= a[i]:
            possible = True
            break
    
    print("YES" if possible else "NO")

GPT ratkaisu perustuu samaan ideaan. se vaikuttaa äkkiä katsottuna paremmalta, mutta ei kuitenkaan ole sitä. Joskin ero on marginaalinen


SUORITUS STATISTIIKKA
GPT 156 ms	11900 KB
OMA 140 ms	11800 KB

LINKKI
https://codeforces.com/problemset/problem/1420/A

'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):
        results=[]

        for n, cube_list in cases:
            is_decreasing=all(cube_list[i] >cube_list[i+1] for i in range(n-1))#tarkistaan onko jono laskeva. 
            results.append('NO' if is_decreasing  else 'YES')

        return "\n".join(results)

if __name__ =='__main__':
    cases=[]
    t=int(input())

    for _ in range(t):
        n=int(input())
        a=list(map(int, input().split()))
        cases.append([n,a])

    test_class=XXX2(cases)
    print(test_class.XXX())
