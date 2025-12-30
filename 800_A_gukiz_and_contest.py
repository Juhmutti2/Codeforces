'''

A. GukiZ and Contest
time limit per test2 seconds
memory limit per test256 megabytes
Professor GukiZ likes programming contests. He especially likes to rate his students on the contests he prepares. Now, he has decided to prepare a new contest.

In total, n students will attend, and before the start, every one of them has some positive integer rating. Students are indexed from 1 to n. Let's denote the rating of i-th student as ai. After the contest ends, every student will end up with some positive integer position. GukiZ expects that his students will take places according to their ratings.

He thinks that each student will take place equal to . In particular, if student A has rating strictly lower then student B, A will get the strictly better position than B, and if two students have equal ratings, they will share the same position.

GukiZ would like you to reconstruct the results by following his expectations. Help him and determine the position after the end of the contest for each of his students if everything goes as expected.

Input
The first line contains integer n (1 ≤ n ≤ 2000), number of GukiZ's students.

The second line contains n numbers a1, a2, ... an (1 ≤ ai ≤ 2000) where ai is the rating of i-th student (1 ≤ i ≤ n).

Output
In a single line, print the position after the end of the contest for each of n students in the same order as they appear in the input.

Examples
InputCopy
3
1 3 3
OutputCopy
3 1 1
InputCopy
1
1
OutputCopy
1
InputCopy
5
3 5 3 4 5
OutputCopy
4 1 4 3 1
Note
In the first sample, students 2 and 3 are positioned first (there is no other student with higher rating), and student 1 is positioned third since there are two students with higher rating.

In the second sample, first student is the only one on the contest.

In the third sample, students 2 and 5 share the first position with highest rating, student 4 is next with third position, and students 1 and 3 are the last sharing fourth position.

OSOITE
https://codeforces.com/problemset/problem/551/A

SYÖTE
n=listan a pituus
a= testilista

KOMPAKTI
Meillä on n alkion mittainen lista a, jolla on kilpailutuloksista pisteet. 
Haluamme jokaiseen listan indeksiin lopullisen sijoituksen, kun sääntö:
sijoitus on 1+niiden tulosten määrä joissa pisteet ovat tiukasti isommat. 


RATKAISU
Tehdään lista tupleja, joissa (pisteet, sijainti listalla) tämän jälkeen käymme kyseisen listan läpi ja sijoitamme arvot alkuperäisestä lista a:sta kopioituun tuloslistaan. 

OMA HUOM
Tein tehtävän 29.7.2025. Tämän on codeforces alkuaikojen tason 800 tehtävä. Mielestäni tämä on huomattavan vaikea ollakseen tason 800 (=helpoin mahdollinen) harjoitus.


GPT 4.0 TARJOAA

n = int(input())
a = list(map(int, input().split()))

# Tallennetaan arvosanat alkuperäisine indekseineen
with_index = [(val, idx) for idx, val in enumerate(a)]

# Järjestetään laskevaan järjestykseen arvosanojen mukaan
with_index.sort(reverse=True)

# Luodaan sijoituslista
position = [0] * n

# Käydään läpi ja asetetaan sijoitukset
rank = 1
for i in range(n):
    if i > 0 and with_index[i][0] != with_index[i - 1][0]:
        rank = i + 1
    position[with_index[i][1]] = rank

# Tulostetaan tulokset
print(' '.join(map(str, position)))

GPT tarjoaa osin saman ratkaisun (tulosten järjestäminen). Lopullinen järjestäminen eroaa. Ilman kommentteja tämä on huomattavan vaikeaselkoinen. 


SUORITUS STATISTIIKKA
GPT 93 ms	2400 KB
OMA 93 ms	2500 KB


LINKKI
https://codeforces.com/problemset/problem/551/A


'''

class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):

        contest_results=[]
        n,a=self.cases
        final_order=a.copy()#kopioidaan alkuperäinen lista tuloksia varten

        for i, val in enumerate(a):
            contest_results.append((val,i))#val(=pisteet) mukaan tallennus mahdollistaa tarkoituksenmukaisen sorttauksen. 
        
        contest_results=sorted(contest_results,reverse=True)
        current_pos=1#aloitussija
        current_point=contest_results[0][0]#aloituspisteet
        
        for point, position in contest_results:
            if point!=current_point:#esivalmistelu, jos käsiteltävä piste ei ole nykyinen piste
                current_pos+=a.count(current_point)#paljonko nykyisiä pisteitä on. 
                current_point=point
            final_order[position]=current_pos#esivalmistelujen jälkeen tallennus
        return final_order

if __name__ =='__main__':
    n=int(input())
    a=list(map(int, input().split()))
    cases=[n,a]

    test_class=XXX2(cases)
    results=test_class.XXX()
    print(*results)