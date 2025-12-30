'''
B. Lucky String
time limit per test2 seconds
memory limit per test256 megabytes
Petya loves lucky numbers. We all know that lucky numbers are the positive integers whose decimal representations contain only the lucky digits 4 and 7. For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.

Petya recently learned to determine whether a string of lowercase Latin letters is lucky. For each individual letter all its positions in the string are written out in the increasing order. This results in 26 lists of numbers; some of them can be empty. A string is considered lucky if and only if in each list the absolute difference of any two adjacent numbers is a lucky number.

For example, let's consider string "zbcdzefdzc". The lists of positions of equal letters are:

b: 2
c: 3, 10
d: 4, 8
e: 6
f: 7
z: 1, 5, 9
Lists of positions of letters a, g, h, ..., y are empty.
This string is lucky as all differences are lucky numbers. For letters z: 5 - 1 = 4, 9 - 5 = 4, for letters c: 10 - 3 = 7, for letters d: 8 - 4 = 4.

Note that if some letter occurs only once in a string, it doesn't influence the string's luckiness after building the lists of positions of equal letters. The string where all the letters are distinct is considered lucky.

Find the lexicographically minimal lucky string whose length equals n.

Input
The single line contains a positive integer n (1 ≤ n ≤ 105) — the length of the sought string.

Output
Print on the single line the lexicographically minimal lucky string whose length equals n.

Examples
InputCopy
5
OutputCopy
abcda
InputCopy
3
OutputCopy
abc
Note
The lexical comparison of strings is performed by the < operator in modern programming languages. String a is lexicographically less than string b if exists such i (1 ≤ i ≤ n), that ai < bi, and for any j (1 ≤ j < i) aj = bj.





SYÖTE
n=onnekkaan merkkijonon pituus

KOMPAKTI
Halutaan maksimipituinen onnekas merkkijono. Onnekkuuden määritelmä = toistuvien merkkien väli tulee olla 4 tai 7 JA saadun merkkijonon tulee olla leksikografisesti pienin mahdollinen. 


RATKAISU
Leksikografisesti pienin tarkoittaa että toistamme jonoa 'abcd' tarvittavan monta kertaa. 
divmod auttaa määrittämään kuinka monta täyttä ja vajaata jonoa tarvitsemme. 
divmod[0]= täydet jonot
divmod[1]=vajaan jonon pituus

GPT 4.0 TARJOAA

def generate_lucky_string(n):
    pattern = "abcd"
    result = (pattern * ((n // 4) + 1))[:n]
    return result

if __name__ == "__main__":
    n = int(input())
    print(generate_lucky_string(n))

GPT on merkittävästi nopeampi mutta [:n] vaati itselle merkittävää pohdintaa. Selitys: GPT rakentaa ylimittaisen merkkijonon ja ottaa siitä vain tarvittavat n merkkiä. 
Mielestäni divmod ratkaisu näyttää selkeämmin kokonaiskertoimen ja jäännöksen. GPT tuumii että ratkaisuni on "teknisempi", jota en ihan osta. 

SUORITUS STATISTIIKKA
GPT 156 ms	200 KB
OMA 278 ms	200 KB

LINKKI
https://codeforces.com/problemset/problem/110/B


'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):
        cases=self.cases
        ref='abcd'#perusjono
        coef=divmod(cases,4)#Kuinka monta täyttä perusjonoa ja kuinka monta merkkiä vajaata vajaata. 


        return ref*coef[0]+ref[:coef[1]]#rakennetaan jono

if __name__ =='__main__':
    cases=int(input())

    test_class=XXX2(cases)
    print(test_class.XXX())
