'''
B. Permutation
time limit per test2 seconds
memory limit per test256 megabytes
"Hey, it's homework time" — thought Polycarpus and of course he started with his favourite subject, IT. Polycarpus managed to solve all tasks but for the last one in 20 minutes. However, as he failed to solve the last task after some considerable time, the boy asked you to help him.

The sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

You are given an arbitrary sequence a1, a2, ..., an containing n integers. Each integer is not less than 1 and not greater than 5000. Determine what minimum number of elements Polycarpus needs to change to get a permutation (he should not delete or add numbers). In a single change he can modify any single sequence element (i. e. replace it with another integer).

Input
The first line of the input data contains an integer n (1 ≤ n ≤ 5000) which represents how many numbers are in the sequence. The second line contains a sequence of integers ai (1 ≤ ai ≤ 5000, 1 ≤ i ≤ n).

Output
Print the only number — the minimum number of changes needed to get the permutation.

Examples
InputCopy
3
3 1 2
OutputCopy
0
InputCopy
2
2 2
OutputCopy
1
InputCopy
5
5 3 3 3 1
OutputCopy
2
Note
The first sample contains the permutation, which is why no replacements are required.

In the second sample it is enough to replace the first element with the number 1 and that will make the sequence the needed permutation.

In the third sample we can replace the second element with number 4 and the fourth element with number 2

OSOITE
https://codeforces.com/problemset/problem/137/B
SYÖTE
n=luku johon asti halutaan permutaatio, on myös listan a pituus
a= lista numeroita

KOMPAKTI
montako numeroa täytyy muuttaa kun halutaan n asti permutaatio listan a luvuista.
Listan a luvut ovat välillä 1 ... 5000


RATKAISU

Tehtävä on mahdollista ratkaista ilman iteraatiota järjestämällä testilistan, ja etsimällä bisect avulla arvon n paikka. 
Tämän jälkeen ottamalla alilista n indeksiin asti saamme halutun permutaation jäsenet.

GPT 4.0 TARJOAA

n = int(input())
a = list(map(int, input().split()))

from collections import Counter

count = Counter()
duplicates = []
for x in a:
    if 1 <= x <= n:
        count[x] += 1
    else:
        # Jos x ei voi kuulua permutaatioon, laitetaan heti duplikaattilistaan
        duplicates.append(x)

missing = []
for i in range(1, n+1):
    if count[i] == 0:
        missing.append(i)
    elif count[i] > 1:
        duplicates.extend([i] * (count[i] - 1))

# Tarvitaan yhtä monta korvausta kuin puuttuvia lukuja
print(len(missing))

gpt lähestyy asiaa mielestäni huomattavasti monimutkaisemmin peräti kahdella iteraatiolla. Vaikka suoritus on gpt:llä nopeampi, se kuluttaa muistia lähes tuplat.
Absoluuttiset arvot ovat maltillisia mutta monimutkaisuuden vuoksi gpt:n ratkaisu on paljon haastavampi ylläpitää: Ymmärrän tehtävän, mutta minun on hankala suorilta ymmärtää mitä gpt:n koodi tekee. 
"Miksi periaatteessa suoraviivainen asia on tehty näin monimutkaisesti, ja mitä tässä edes tapahtuu?"

Mielenkiintoisesti pyydettäessä arviota omasta koodista, GPT menee aivan puihin ja väittää sitä epäluotettavaksi. 
Gpt ottaa erityisesti esiin koodin epäluotettavuuden "muuttuvilla raja-arvoilla". Vaikuttaa siltä, ettei gpt hoksaa katsoa edellisestä viestistä tehtävän raja-arvoja, ellei sitä erikseen pyydetä. 

Mielestäni tämä tehtävä osoittaa GPT:n rajallisen hyödyllisyyden koodatessa. Täsmällisemmin, mielestäni törmäämme gpt:n puutteelliseen kykyyn hahmottaa monimutkaisia asiayhteyksiä. 


SUORITUS STATISTIIKKA
GPT 186 ms	3200 KB
OMA 218 ms	1800 KB




'''

import bisect

class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):

        n,a=self.cases
        a.sort()#järjestetään jotta bisect toimii
        n_index=bisect.bisect(a,n)#palauttaa indeksin jossa n on tai pitäisi olla
        wanted_permutation=a[:n_index]#listassa on aina permutaation halutut jäsenet. jos jäseniä ei ole, lista on tyhjä. 


        return n-len(set(wanted_permutation))

if __name__ =='__main__':
    n=int(input())
    a=list(map(int, input().split()))
    cases=[n,a]

    test_class=XXX2(cases)
    print(test_class.XXX())