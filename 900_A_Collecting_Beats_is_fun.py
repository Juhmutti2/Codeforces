'''
A. Collecting Beats is Fun
time limit per test1 second
memory limit per test256 megabytes
Cucumber boy is fan of Kyubeat, a famous music game.

Kyubeat has 16 panels for playing arranged in 4 × 4 table. When a panel lights up, he has to press that panel.

Each panel has a timing to press (the preffered time when a player should press it), and Cucumber boy is able to press at most k panels in a time with his one hand. Cucumber boy is trying to press all panels in perfect timing, that is he wants to press each panel exactly in its preffered time. If he cannot press the panels with his two hands in perfect timing, his challenge to press all the panels in perfect timing will fail.

You are given one scene of Kyubeat's panel from the music Cucumber boy is trying. Tell him is he able to press all the panels in perfect timing.

Input
The first line contains a single integer k (1 ≤ k ≤ 5) — the number of panels Cucumber boy can press with his one hand.

Next 4 lines contain 4 characters each (digits from 1 to 9, or period) — table of panels. If a digit i was written on the panel, it means the boy has to press that panel in time i. If period was written on the panel, he doesn't have to press that panel.

Output
Output "YES" (without quotes), if he is able to press all the panels in perfect timing. If not, output "NO" (without quotes).

Examples
InputCopy
1
.135
1247
3468
5789
OutputCopy
YES
InputCopy
5
..1.
1111
..1.
..1.
OutputCopy
YES
InputCopy
1
....
12.1
.2..
.2..
OutputCopy
NO
Note
In the third sample boy cannot press all panels in perfect timing. He can press all the panels in timing in time 1, but he cannot press the panels in time 2 in timing with his two hands.
SYÖTE
k=sormien määrä
4x4 ruudukko

KOMPAKTI
Onko samojen numeroiden määrä maksimissaan 2*k?

RATKAISU
Lasketaan numeroiden esiintymät, jätetään pisteet pois ja verrataan. 

GPT 4.0 TARJOAA

from collections import Counter

k = int(input())
grid = [input().strip() for _ in range(4)]

counter = Counter()

for row in grid:
    for ch in row:
        if ch.isdigit():
            counter[ch] += 1

for count in counter.values():
    if count > 2 * k:
        print("NO")
        break
else:
    print("YES")

GPT suorittaa laskennan ruudukkona hyödyntäen isdigit() funktiota. Todennäköisesti funktiokutsu selittää nopeuseron. 

SUORITUS STATISTIIKKA
GPT 108 ms	900 KB
OMA 93 ms	900 KB

LINKKI
https://codeforces.com/problemset/problem/373/A
'''

from collections import Counter


class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):
        
        k,char=cases
        char_count=Counter(char)
        max_count=max((char_count[char] for char in char_count if char!='.'), default=0)#lasketaan muiden kuin pisteiden maksimimäärä. jos vain pisteitä, 0.
        return 'YES' if max_count<=2*k else 'NO'
        
if __name__ =='__main__':
    cases=[]
    k=int(input())
    chars=[]
    for _ in range(4):
        chars.extend(input().strip())#extend avulla yhdeksi listaksi
    cases=[k,chars]

    test_class=XXX2(cases)
    print(test_class.XXX())
