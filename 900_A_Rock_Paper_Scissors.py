'''
A. Rock-paper-scissors
time limit per test2 seconds
memory limit per test256 megabytes
Uncle Fyodor, Matroskin the Cat and Sharic the Dog live their simple but happy lives in Prostokvashino. Sometimes they receive parcels from Uncle Fyodor’s parents and sometimes from anonymous benefactors, in which case it is hard to determine to which one of them the package has been sent. A photographic rifle is obviously for Sharic who loves hunting and fish is for Matroskin, but for whom was a new video game console meant? Every one of the three friends claimed that the present is for him and nearly quarreled. Uncle Fyodor had an idea how to solve the problem justly: they should suppose that the console was sent to all three of them and play it in turns. Everybody got relieved but then yet another burning problem popped up — who will play first? This time Matroskin came up with a brilliant solution, suggesting the most fair way to find it out: play rock-paper-scissors together. The rules of the game are very simple. On the count of three every player shows a combination with his hand (or paw). The combination corresponds to one of three things: a rock, scissors or paper. Some of the gestures win over some other ones according to well-known rules: the rock breaks the scissors, the scissors cut the paper, and the paper gets wrapped over the stone. Usually there are two players. Yet there are three friends, that’s why they decided to choose the winner like that: If someone shows the gesture that wins over the other two players, then that player wins. Otherwise, another game round is required. Write a program that will determine the winner by the gestures they have shown.

Input
The first input line contains the name of the gesture that Uncle Fyodor showed, the second line shows which gesture Matroskin showed and the third line shows Sharic’s gesture.

Output
Print "F" (without quotes) if Uncle Fyodor wins. Print "M" if Matroskin wins and "S" if Sharic wins. If it is impossible to find the winner, print "?".

Examples
InputCopy
rock
rock
rock
OutputCopy
?
InputCopy
paper
rock
rock
OutputCopy
F
InputCopy
scissors
rock
rock
OutputCopy
?
InputCopy
scissors
paper
rock
OutputCopy
?


KOMPAKTI
kivi-paperi-sakset, kuka voittaa?


RATKAISU
Huomioitava:
esiintymiskerrat, voittoehto (paperi voittaa kiven jne) ja se että voittava esiintyy vain kerran
Kaikissa muissa tapauksissa voittajaa ei voida määrittää. 

GPT 4.0 TARJOAA

f = input().strip()  # Uncle Fyodor
m = input().strip()  # Matroskin
s = input().strip()  # Sharic

# Voittosäännöt
wins_over = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}

# Laske kuinka monta kertaa kukin ele esiintyy
counts = {}
for gesture in [f, m, s]:
    counts[gesture] = counts.get(gesture, 0) + 1

# Jos kaikki sama tai kaikki eri -> ei voittajaa
if len(counts) != 2:
    print("?")
else:
    # Tarkista voittaako yksin valittu ele molemmat muut
    for gesture in counts:
        if counts[gesture] == 1:
            # tämä ele on valittu vain kerran
            if wins_over[gesture] in counts and counts[wins_over[gesture]] == 2:
                # ja se voittaa molemmat muut
                if f == gesture:
                    print("F")
                elif m == gesture:
                    print("M")
                elif s == gesture:
                    print("S")
                break
    else:
        print("?")

GPT tarjoama ratkaisu vaikuttaa monimutkaiselta, mutta on tehokkaampi suorittaa. 
Koska tehokkuusero on marginaalinen, käyttäisin tässä omaa koodiani joka on mielestäni selkeämpi ja siten helpompi ylläpitää. 

SUORITUS STATISTIIKKA
GPT 154 ms	200 KB
OMA 186 ms	200 KB

LINKKI
https://codeforces.com/problemset/problem/1426/E

'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):

        f,m,s=self.cases
        type2=len(set(self.cases))==2#katsotaan onko syötteessä vain kaksi eri esiintymää. 
        dict={#sanakirja voittajista vertailuun. 
            f:'F',
            m:'M',
            s:'S'
        }#Katsotaan järjestyksessä onko voittajaa kivi, paperi, sakset ja verrataan kuka antoi voittavan veikkauksen. 
        if type2 and 'scissors' in self.cases and 'rock' in self.cases and self.cases.count('rock')==1:
            return dict['rock']
        elif type2 and 'rock' in self.cases  and 'paper' in self.cases and self.cases.count('paper')==1:
            return dict['paper']
        elif type2 and 'paper' in self.cases and 'scissors' in self.cases and self.cases.count('scissors')==1:
            return dict['scissors']
        else:#Muissa tapauksissa voittajaa ei voida määrittää. 
            return '?'


if __name__ =='__main__':
    F=input()
    M=input()
    S=input()
    cases=[F,M,S]



    test_class=XXX2(cases)
    print(test_class.XXX())
