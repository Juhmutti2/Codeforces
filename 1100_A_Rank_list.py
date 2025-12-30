'''

A. Rank List
time limit per test2 seconds
memory limit per test256 megabytes
Another programming contest is over. You got hold of the contest's final results table. The table has the following data. For each team we are shown two numbers: the number of problems and the total penalty time. However, for no team we are shown its final place.

You know the rules of comparing the results of two given teams very well. Let's say that team a solved pa problems with total penalty time ta and team b solved pb problems with total penalty time tb. Team a gets a higher place than team b in the end, if it either solved more problems on the contest, or solved the same number of problems but in less total time. In other words, team a gets a higher place than team b in the final results' table if either pa > pb, or pa = pb and ta < tb.

It is considered that the teams that solve the same number of problems with the same penalty time share all corresponding places. More formally, let's say there is a group of x teams that solved the same number of problems with the same penalty time. Let's also say that y teams performed better than the teams from this group. In this case all teams from the group share places y + 1, y + 2, ..., y + x. The teams that performed worse than the teams from this group, get their places in the results table starting from the y + x + 1-th place.

Your task is to count what number of teams from the given list shared the k-th place.

Input
The first line contains two integers n and k (1 ≤ k ≤ n ≤ 50). Then n lines contain the description of the teams: the i-th line contains two integers pi and ti (1 ≤ pi, ti ≤ 50) — the number of solved problems and the total penalty time of the i-th team, correspondingly. All numbers in the lines are separated by spaces.

Output
In the only line print the sought number of teams that got the k-th place in the final results' table.

Examples
InputCopy
7 2
4 10
4 10
4 10
3 20
2 1
2 1
1 10
OutputCopy
3
InputCopy
5 4
3 1
3 1
5 3
3 1
3 1
OutputCopy
4
Note
The final results' table for the first sample is:

1-3 places — 4 solved problems, the penalty time equals 10
4 place — 3 solved problems, the penalty time equals 20
5-6 places — 2 solved problems, the penalty time equals 1
7 place — 1 solved problem, the penalty time equals 10
The table shows that the second place is shared by the teams that solved 4 problems with penalty time 10. There are 3 such teams.

The final table for the second sample is:

1 place — 5 solved problems, the penalty time equals 3
2-5 places — 3 solved problems, the penalty time equals 1
The table shows that the fourth place is shared by the teams that solved 3 problems with penalty time 1. There are 4 such teams

SYÖTE
n,k testitapausten ja halutun sijan joukkuemäärä
n määrä tupleja


KOMPAKTI
Kuinka monta joukkuetta on k sijalla kun meillä on tuloslista tupleja, jossa
ensimmäinen arvo on ratkaistut tehtävät, toinen arvo sakkominuutit.
Lajittelu: tehtävien määrä ratkaisee, jos sama määrä ratkaistuja, pienempi sakkominuuttimäärä on keskinäinen voittaja


RATKAISU
Haasteena on tuplen lajittelu halutusti. Tässä meitä auttaa lambda. 
Lajittelun jälkeen lasketaan k-1 indeksiä vastaavat arvoesiintymät. 


GPT 4.0 TARJOAA

n, k = map(int, input().split())
teams = [tuple(map(int, input().split())) for _ in range(n)]

# Järjestetään paremmuusjärjestykseen: ensin eniten tehtäviä, sitten pienin aikarangaistus
teams.sort(key=lambda x: (-x[0], x[1]))

# Otetaan k-1 indeksiltä oleva tiimi (koska indeksit alkaa 0)
target_team = teams[k - 1]

# Lasketaan kuinka monta tiimiä sai saman tuloksen (samat tehtävät ja sama aika)
result = sum(1 for team in teams if team == target_team)

print(result)

GPT käyttää lähes samaa lähestymistapaa. Tulosten laskentatavassa on ero ja todennäköisesti suorituskykyero syntyy tässä. 


SUORITUS STATISTIIKKA
GPT 218 ms	200 KB
OMA 186 ms	200 KB

LINKKI
https://codeforces.com/problemset/problem/166/A

'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):

        k,case=self.cases
        final_results=sorted(case, key=lambda t:(-t[0],t[1]))
        ref_team=final_results[k-1]#Voitaisiin tehdä myös ilman muuttujamuotoilua
        

        return final_results.count(ref_team)#lasketaan osumavastaavuudet. 

if __name__ =='__main__':
    case=[]
    n,k=map(int,input().split())
    

    for _ in range(n):
        case.append((tuple(map(int, input().split()))))
    cases=[k,case]

    test_class=XXX2(cases)
    print(test_class.XXX())
