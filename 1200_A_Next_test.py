'''
A. Next Test
time limit per test2 seconds
memory limit per test256 megabytes
«Polygon» is a system which allows to create programming tasks in a simple and professional way. When you add a test to the problem, the corresponding form asks you for the test index. As in most cases it is clear which index the next test will have, the system suggests the default value of the index. It is calculated as the smallest positive integer which is not used as an index for some previously added test.

You are to implement this feature. Create a program which determines the default index of the next test, given the indexes of the previously added tests.

Input
The first line contains one integer n (1 ≤ n ≤ 3000) — the amount of previously added tests. The second line contains n distinct integers a1, a2, ..., an (1 ≤ ai ≤ 3000) — indexes of these tests.

Output
Output the required default value for the next test index.

Examples
InputCopy
3
1 7 2
OutputCopy
3



SYÖTE
n=syötelistan pituus
a= syötelista

KOMPAKTI
Etsitään pienin arvo, joka ei ole listalla

RATKAISU

iteroidaan, if not i in a...

GPT 4.0 TARJOAA

n = int(input())
a = set(map(int, input().split()))

for i in range(1, 3002):  # 3001 riittää, koska max ai = 3000
    if i not in a:
        print(i)
        break

GPT hyödyntää samaa ratkaisua nopeammin tehtynä, koska set() haku on tehokkaampi. 
        

SUORITUS STATISTIIKKA
GPT 186 ms	1700 KB
OMA 218 ms	1700 KB

LINKKI
https://codeforces.com/problemset/problem/27/A

'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):
        n,a=cases
        for i in range(1,n+2):
            if i not in a:
                return i

if __name__ =='__main__':
    n=int(input())
    a=list(map(int, input().split()))

    cases=[n,a]

    test_class=XXX2(cases)
    print(test_class.XXX())
