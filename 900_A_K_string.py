'''
A. k-String
time limit per test2 seconds
memory limit per test256 megabytes
A string is called a k-string if it can be represented as k concatenated copies of some string. For example, the string "aabaabaabaab" is at the same time a 1-string, a 2-string and a 4-string, but it is not a 3-string, a 5-string, or a 6-string and so on. Obviously any string is a 1-string.

You are given a string s, consisting of lowercase English letters and a positive integer k. Your task is to reorder the letters in the string s in such a way that the resulting string is a k-string.

Input
The first input line contains integer k (1 ≤ k ≤ 1000). The second line contains s, all characters in s are lowercase English letters. The string length s satisfies the inequality 1 ≤ |s| ≤ 1000, where |s| is the length of string s.

Output
Rearrange the letters in string s in such a way that the result is a k-string. Print the result on a single output line. If there are multiple solutions, print any of them.

If the solution doesn't exist, print "-1" (without quotes).

Examples
InputCopy
2
aazz
OutputCopy
azaz
InputCopy
3
abcabcabz
OutputCopy
-1


KOMPAKTI
Toistetaan merkkijono s k kertaa

RATKAISU
Mikäli jokin merkin esiintymä ei ole jaollinen k:lla, mahdotonta.
muulloin:
tehdään yksittäinen merkkijono jota toistetaan k kertaa:
listataan kirjaimet, luodaan tyhjä merkkijono, johon lisätään kirjaimia esiintymä/k kertaa. 

GPT 4.0 TARJOAA

from collections import Counter

k = int(input())
s = input()

counter = Counter(s)

# Tarkista jaollisuus
for count in counter.values():
    if count % k != 0:
        print(-1)
        break
else:
    base = ""
    for char in sorted(counter):  # aakkosjärjestys
        base += char * (counter[char] // k)
    print(base * k)

    
GPT tarjoaa melko samanlaista ratkaisua joka on kuitenkin mielenkiintoisesti merkkitävästi (34,7%) hitaampi.
Osan selittää sorted(), jonka tiputtaminen pois muuttaa GPT:n suoritusaikaa: 216 ms	900 KB. 
Mietin hyvän tovin ja kokeilin eri vaihtoehtoja mutta en saanut eriteltyä mikä täsmälleen vaikuttaa loppuun eroon. 
Mainittakoon että CF kontekstissa pienehkölle erolle (216vs184) voisi löytyä selitys. 
funktiomuoto ja return saattaa olla hiukan nopeampi kuin print, mutta oman koodin refaktorointi käyttämään print() antoi 186ms suoritusajan. 


SUORITUS STATISTIIKKA
GPT 248 ms	900 KB
OMA 184 ms	900 KB

LINKKI
https://codeforces.com/problemset/problem/219/A



'''

from collections import Counter


class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):
        k,string=self.cases
        counts=Counter(string)#esiintymien määrä
        if any(val%k!=0 for val in counts.values()):#jos ei jakaudu tasan per toisto
            return -1
        else:
            chars=list(set(string))#lista kirjaimista
            new=''
            for i in range(len(chars)):
                new+=chars[i]*(counts[chars[i]]//k)#lisätään merkki esiintymä/k kertaa
            return new*k #Toistetaan k kertaa edellistä. 



if __name__ =='__main__':
    k=int(input())
    s=input()
    cases=[k,s]

    test_class=XXX2(cases)
    print(test_class.XXX())
