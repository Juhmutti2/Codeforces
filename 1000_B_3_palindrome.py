'''

B. 3-palindrome
time limit per test1 second
memory limit per test256 megabytes
In the beginning of the new year Keivan decided to reverse his name. He doesn't like palindromes, so he changed Naviek to Navick.

He is too selfish, so for a given n he wants to obtain a string of n characters, each of which is either 'a', 'b' or 'c', with no palindromes of length 3 appearing in the string as a substring. For example, the strings "abc" and "abca" suit him, while the string "aba" doesn't. He also want the number of letters 'c' in his string to be as little as possible.

Input
The first line contains single integer n (1 ≤ n ≤ 2·105) — the length of the string.

Output
Print the string that satisfies all the constraints.

If there are multiple answers, print any of them.

Examples
InputCopy
2
OutputCopy
aa
InputCopy
3
OutputCopy
bba
Note
A palindrome is a sequence of characters which reads the same backward and forward.


SYÖTE
haluttu merkkijonon pituus

KOMPAKTI
halutaan merkkijono käyttäen kirjaimia a, b ja c, jossa ei ole kolmen mittaisia alimerkkijonoja, jotka ovat palindromeja.
lisäksi merkkiä c pitää käyttää mahdollisimman vähän


RATKAISU
On mielestäni puolikompa. Tehtävä kysyy "millainen on merkeistä a ja b muodostettava jono, joka ei sisällä palindromeja"

Varsinainen ratkaisu:
muodostetaan referenssijono, joka muutetaan syötteen mittaiseksi. Tässä käytetty divmod()


GPT 4.0 TARJOAA

n = int(input())
pattern = "aabb"
result = (pattern * ((n + 3) // 4))[:n]
print(result)

GPT tarjoaa samaa ratkaisua, joka on hitaampi ja hiukan muistisyöpömi. Absoluuttisesti erot ovat mitättömiä, selittyvät
todennäköisesti siitä, että gpt rakentaa ensin riittävän pitkän merkkijonon jota lähtee leikkaamaan. Oma koodi palauttaa suoraan tarvittavan pituuden. 


SUORITUS STATISTIIKKA
GPT 93 ms	800 KB
OMA 77 ms	700 KB

LINKKI
https://codeforces.com/problemset/problem/805/B

'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):
        ref='baab'#referenssijono joka toistuu riittävän monta kertaa. Huom, jono on neljän pituinen
        length=divmod(self.cases, 4)


        return ref*length[0]+ref[:length[1]]#rakennetaan riittävä pituus suoraan.

if __name__ =='__main__':
    cases=int(input())

    test_class=XXX2(cases)
    print(test_class.XXX())
