'''

G. University Classes
time limit per test1 second
memory limit per test256 megabytes
There are n student groups at the university. During the study day, each group can take no more than 7 classes. Seven time slots numbered from 1 to 7 are allocated for the classes.

The schedule on Monday is known for each group, i. e. time slots when group will have classes are known.

Your task is to determine the minimum number of rooms needed to hold classes for all groups on Monday. Note that one room can hold at most one group class in a single time slot.

Input
The first line contains a single integer n (1 ≤ n ≤ 1000) — the number of groups.

Each of the following n lines contains a sequence consisting of 7 zeroes and ones — the schedule of classes on Monday for a group. If the symbol in a position equals to 1 then the group has class in the corresponding time slot. In the other case, the group has no class in the corresponding time slot.

Output
Print minimum number of rooms needed to hold all groups classes on Monday.

Examples
InputCopy
2
0101010
1010101
OutputCopy
1
InputCopy
3
0101011
0011001
0110111
OutputCopy
3
Note
In the first example one room is enough. It will be occupied in each of the seven time slot by the first group or by the second group.

In the second example three rooms is enough, because in the seventh time slot all three groups have classes.





SYÖTE
n=rivien määrä
rivit


KOMPAKTI
Montako huonetta tarvitaan kun annettuna on varaustaulukko? 0 = ei  käytössä, 1 = käytössä.
Yksi sarake on yksi tunti


RATKAISU
Tarkastellaan montako varausta on sarakkeessa. Vastaus on ykkösten maksimimäärä missään sarakkeessa. 
(Kts tarvittaessa esimerkki 2 viimeinen sarake)

GPT 4.0 TARJOAA

n = int(input())
slots = [0] * 7

for _ in range(n):
    line = input().strip()
    for i in range(7):
        if line[i] == '1':
            slots[i] += 1

print(max(slots))

GPT käyttää myös vastaavaa laskuritekniikkaa, se on huomattavasti hitaampi ja muistisyöpömpi kuin omani. Absoluuttinen muistiero ei ole iso,
mutta suoritusajassa on merkittävä ero. Erotus selittyy ilmeisesti sillä että slots = [0] * 7 rakennetaan joka kohdalle erikseen ja näistä haetaan lopuksi max. 


SUORITUS STATISTIIKKA
GPT 155 ms	2200 KB
OMA 93 ms	1700 KB

LINKKI
https://codeforces.com/problemset/problem/847/G

'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):


        n,cases=self.cases
        current=0

        for i in range(7):
            row=[cases[j][i] for j in range(n)]
            current=max(row.count('1'),current)
        return current

if __name__ =='__main__':
    case=[]
    n=int(input())

    for _ in range(n):
        case.append(str(input()))
    cases=[n,case]


    test_class=XXX2(cases)
    print(test_class.XXX())