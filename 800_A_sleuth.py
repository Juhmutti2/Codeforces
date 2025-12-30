'''
A. Sleuth
time limit per test2 seconds
memory limit per test256 megabytes
Vasya plays the sleuth with his friends. The rules of the game are as follows: those who play for the first time, that is Vasya is the sleuth, he should investigate a "crime" and find out what is happening. He can ask any questions whatsoever that can be answered with "Yes" or "No". All the rest agree beforehand to answer the questions like that: if the question’s last letter is a vowel, they answer "Yes" and if the last letter is a consonant, they answer "No". Of course, the sleuth knows nothing about it and his task is to understand that.

Unfortunately, Vasya is not very smart. After 5 hours of endless stupid questions everybody except Vasya got bored. That’s why Vasya’s friends ask you to write a program that would give answers instead of them.

The English alphabet vowels are: A, E, I, O, U, Y

The English alphabet consonants are: B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Z

Input
The single line contains a question represented by a non-empty line consisting of large and small Latin letters, spaces and a question mark. The line length does not exceed 100. It is guaranteed that the question mark occurs exactly once in the line — as the last symbol and that the line contains at least one letter.

Output
Print answer for the question in a single line: YES if the answer is "Yes", NO if the answer is "No".

Remember that in the reply to the question the last letter, not the last character counts. I. e. the spaces and the question mark do not count as letters.

Examples
InputCopy
Is it a melon?
OutputCopy
NO
InputCopy
Is it an apple?
OutputCopy
YES
InputCopy
  Is     it a banana ?
OutputCopy
YES
InputCopy
Is   it an apple  and a  banana   simultaneouSLY?
OutputCopy
YES

SYÖTE
merkkijonorivi


KOMPAKTI
Päättyykö lause vokaaliin vai konsonanttiin

RATKAISU
Poistetaan välit ja verrataan toiseksi viimeistä merkkiä vokaaleihin. Konsonantteja ei tarvita. 

GPT 4.0 TARJOAA

def answer_question(question):
    vowels = set("AEIOUYaeiouy")
    # Käydään merkit läpi taaksepäin ja etsitään viimeinen kirjain
    for char in reversed(question):
        if char.isalpha():
            return "YES" if char in vowels else "NO"

# Syöte
question = input()
# Tulostus
print(answer_question(question))

GPT:n ratkaisu on persoonallisempi. Tehtävä ei jätä juurikaan varaa luovuudelle. 

GPT:n ratkaisussa huomataan GPT:n rajoittuneisuus, joka välillä pilkahtaa esiin: Mitä monimutkaisempi kysymys, sitä vaikeampaa GPT:llä on. 
Kuitenkin tässä GPT epäonnistuu kriittisen ehdon huomaamisessa: merkkijono päättyy kysymysmerkkiin ja etsitty merkki on toiseksi viimeinen. 
Tämä johtaa tarpeettoman monimutkaisen ratkaisun rakentamiseen. On kuitenkin hiukan hämmentävää, että hallusinaatiota lähestyvä ratkaisu esiintyy näinkin suoraviivaisessa tehtävässä.  

Mielenkiintoisesti upper() funktion jättäminen pois + set laajennus tuottaa käytännössä saman statistiikan: (186 ms	200 KB)

SUORITUS STATISTIIKKA
GPT 216 ms	200 KB
OMA 184 ms	200 KB

LINKKI
https://codeforces.com/problemset/problem/49/A
'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):

        vowels= set('AEIOUY')#Nopeampi kuin listahaku

        if cases[-2].upper() in vowels:
            return 'YES'
        return 'NO'



if __name__ =='__main__':
    cases=input().replace(' ','')

    test_class=XXX2(cases)
    print(test_class.XXX())
