'''

A. Dice Tower
time limit per test2 seconds
memory limit per test256 megabytes
A dice is a cube, its faces contain distinct integers from 1 to 6 as black points. The sum of numbers at the opposite dice faces always equals 7. Please note that there are only two dice (these dices are mirror of each other) that satisfy the given constraints (both of them are shown on the picture on the left).


Alice and Bob play dice. Alice has built a tower from n dice. We know that in this tower the adjacent dice contact with faces with distinct numbers. Bob wants to uniquely identify the numbers written on the faces of all dice, from which the tower is built. Unfortunately, Bob is looking at the tower from the face, and so he does not see all the numbers on the faces. Bob sees the number on the top of the tower and the numbers on the two adjacent sides (on the right side of the picture shown what Bob sees).

Help Bob, tell whether it is possible to uniquely identify the numbers on the faces of all the dice in the tower, or not.

Input
The first line contains a single integer n (1 ≤ n ≤ 100) — the number of dice in the tower.

The second line contains an integer x (1 ≤ x ≤ 6) — the number Bob sees at the top of the tower. Next n lines contain two space-separated integers each: the i-th line contains numbers ai, bi (1 ≤ ai, bi ≤ 6; ai ≠ bi) — the numbers Bob sees on the two sidelong faces of the i-th dice in the tower.

Consider the dice in the tower indexed from top to bottom from 1 to n. That is, the topmost dice has index 1 (the dice whose top face Bob can see). It is guaranteed that it is possible to make a dice tower that will look as described in the input.

Output
Print "YES" (without the quotes), if it is possible to to uniquely identify the numbers on the faces of all the dice in the tower. If it is impossible, print "NO" (without the quotes).

Examples
InputCopy
3
6
3 2
5 4
2 4
OutputCopy
YES
InputCopy
3
3
2 6
4 1
5 3
OutputCopy
NO

SYÖTE
n= noppien määrä
x=päällimmäisen nopan silmäluku, joka nähtävissä 
n lukuparia, jotka ovat noppien nähtävissä olevat silmäluvut

KOMPAKTI
Onko torni mahdollinen nopilla joiden vastapäiset sivut muodostavat summan 7 ja joissa jokainen luku esiintyy vain kerran?

RATKAISU

Iteroidaan jokainen noppa, rakennetaan jokaisen nopan jokainen sivu ja tarkistetaan tuliko duplikaatteja per noppa. 

GPT 4.0 TARJOAA

def is_tower_unique(n, top, sides):
    for a, b in sides:
        bottom = 7 - top
        # Jos näkyvä kylkinumero on joko päällä tai pohjassa, ei voi olla ainutlaatuinen
        if a == top or a == bottom or b == top or b == bottom:
            return "NO"
    return "YES"

# Lukeminen
n = int(input())
top = int(input())
sides = [tuple(map(int, input().split())) for _ in range(n)]

print(is_tower_unique(n, top, sides))


GPT käyttää erityyppistä lähestymistapaa, joka on hitaampi runsaiden ehtolauseiden vuoksi.
Mielenkiintoisesti pyydettäessä vertailua ilman johdattelua, GPT tuumii, että GPT ratkaisu on "tehokkaampi", mikä ei yksiselitteisesti ole totta. (Kts yst statistiikka alta)
GPT tuumii myös että GPT ratkaisu on "yksinkertaisempi". Tämä jättää hiukan tulkinnanvaraa. En tehtävän ratkaistuani loppuun asti hahmota miksi GPT koodi toimii:
Ts. eikö sivunumeroissa voi aivan yhtä hyvin olla duplikaatteja? Kuitenkin, vaikka en itse hahmota asiaa, voi olla että taitavammalle yksilölle asia on täysin selvä. 

SUORITUS STATISTIIKKA
GPT 216 ms	200 KB
OMA 186 ms	200 KB

LINKKI
https://codeforces.com/problemset/problem/225/A

'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):
        
        n,x,dices=cases
        up=x#periaatteessa tarpeeton, mutta luodaan selkeyden vuoksi
        bottom=7-x#Oivallus: Bottom ja up ovat koko tornin ajan samoja. 
        for i in range(n):
            current=[]#Nykyisen nopan sivut
            first, second=dices[i]
            third=7-first
            fourth=7-second
            current=[up,bottom,first,second,third,fourth]
            if len(set(current))!=6:#samoja lukuja. 
                return 'NO'
        return 'YES'

            
if __name__ =='__main__':
    n=int(input())
    x=int(input())
    dices=[]

    for _ in range(n):
        dice=tuple(map(int, input().split()))
        dices.append(dice)
    cases=[n,x,dices]

    test_class=XXX2(cases)
    print(test_class.XXX())
