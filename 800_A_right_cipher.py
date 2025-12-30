'''
A. Right-Left Cipher
time limit per test1 second
memory limit per test256 megabytes
Polycarp loves ciphers. He has invented his own cipher called Right-Left.

Right-Left cipher is used for strings. To encrypt the string s=s1s2…sn
 Polycarp uses the following algorithm:

he writes down s1
,
he appends the current word with s2
 (i.e. writes down s2
 to the right of the current result),
he prepends the current word with s3
 (i.e. writes down s3
 to the left of the current result),
he appends the current word with s4
 (i.e. writes down s4
 to the right of the current result),
he prepends the current word with s5
 (i.e. writes down s5
 to the left of the current result),
and so on for each position until the end of s
.
For example, if s
="techno" the process is: "t" →
 "te" →
 "cte" →
 "cteh" →
 "ncteh" →
 "ncteho". So the encrypted s
="techno" is "ncteho".

Given string t
 — the result of encryption of some string s
. Your task is to decrypt it, i.e. find the string s
.

Input
The only line of the input contains t
 — the result of encryption of some string s
. It contains only lowercase Latin letters. The length of t
 is between 1
 and 50
, inclusive.

Output
Print such string s
 that after encryption it equals t
.

Examples
InputCopy
ncteho
OutputCopy
techno
InputCopy
erfdcoeocs
OutputCopy
codeforces
InputCopy
z
OutputCopy
z



OSOITE
https://codeforces.com/problemset/problem/1085/A
SYÖTE
yksirivinen merkkijono

KOMPAKTI
Tehtävässä on annettu salausalgoritmi, joka pitää purkaa. Salaus on tehty:
parillinen indeksi: merkki tulee merkkijonon vasemmalle puolelle, pariton indeksi, merkki tulee oikealle puolelle

RATKAISU
Salaus voidaan purkaa ottamalla alusta ja lopusta merkkejä.

mikäli merkkijonon pituus on parillinen, otetaan lopusta merkki ja parittomalla alusta. 
Mikäli merkkijonon pituus on pariton, toimitaan päinvastoin. 
Molemmissa tapauksissa lisäys on aina vasemmalle puolelle. 

GPT 4.0 TARJOAA

def decrypt(t):
    n = len(t)
    indices = []
    for i in range(n):
        if i % 2 == 0:
            indices.insert(0, i)
        else:
            indices.append(i)

    # nyt indices[i] kertoo, mihin kohtaan t[i] sijoitettiin salauksessa
    # meidän pitää rakentaa alkuperäinen merkkijono s siten, että
    # s[indices[i]] = t[i]
    s = [''] * n
    for i in range(n):
        s[indices[i]] = t[i]
    return ''.join(s)

# Testit
if __name__ == '__main__':
    t = input()
    print(decrypt(t))

GPT kompuroi melkoisesti koodin rakentamisessa. Se onnistuu lopulta toteuttamaan toimivan version, mielestäni tarpeettoman monimutkaisesti, joskin tehokkaasti. 

SUORITUS STATISTIIKKA
GPT 77 ms	300 KB
OMA 77 ms	200 KB

'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):
        cases=self.cases
        result=''
        i=0
        end=-1
        start=0
        while i <len(cases):
            if len(cases)%2==0:#koodatun merkkijonon pituus parillinen
                if i%2==0:
                    result=cases[end]+result
                    end-=1#liikkuu alkua kohti
                else:
                    result=cases[start]+result
                    start+=1#liikkuu loppua kohti
            else:#koodatun merkkijonon pituus pariton
                if i%2==0:
                    result=cases[start]+result
                    start+=1
                else:
                    result=cases[end]+result
                    end-=1
            i+=1

        return result

if __name__ =='__main__':
    cases=input()

    test_class=XXX2(cases)
    print(test_class.XXX())