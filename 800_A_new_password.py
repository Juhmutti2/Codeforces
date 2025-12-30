'''

A. New Password
time limit per test1 second
memory limit per test256 megabytes
Innokentiy decides to change the password in the social net "Contact!", but he is too lazy to invent a new password by himself. That is why he needs your help.

Innokentiy decides that new password should satisfy the following conditions:

the length of the password must be equal to n,
the password should consist only of lowercase Latin letters,
the number of distinct symbols in the password must be equal to k,
any two consecutive symbols in the password must be distinct.
Your task is to help Innokentiy and to invent a new password which will satisfy all given conditions.

Input
The first line contains two positive integers n and k (2 ≤ n ≤ 100, 2 ≤ k ≤ min(n, 26)) — the length of the password and the number of distinct symbols in it.

Pay attention that a desired new password always exists.

Output
Print any password which satisfies all conditions given by Innokentiy.

Examples
InputCopy
4 3
OutputCopy
java
InputCopy
6 6
OutputCopy
python
InputCopy
5 2
OutputCopy
phphp
Note
In the first test there is one of the appropriate new passwords — java, because its length is equal to 4 and 3 distinct lowercase letters a, j and v are used in it.

In the second test there is one of the appropriate new passwords — python, because its length is equal to 6 and it consists of 6 distinct lowercase letters.

In the third test there is one of the appropriate new passwords — phphp, because its length is equal to 5 and 2 distinct lowercase letters p and h are used in it.

Pay attention the condition that no two identical symbols are consecutive is correct for all appropriate passwords in tests.



SYÖTE
n,m

n=pituus 
m=eri merkkien määrä

KOMPAKTI

Luo uusi salasana ehdoilla:

the length of the password must be equal to n,
the password should consist only of lowercase Latin letters,
the number of distinct symbols in the password must be equal to k,
any two consecutive symbols in the password must be distinct.



RATKAISU
Tehdään toistopätkä, jota toistetaan tarvittava määrä

GPT 4.0 TARJOAA

def generate_password(n, k):
    from string import ascii_lowercase
    chars = ascii_lowercase[:k]  # esim. 'abcde' jos k=5

    password = []
    i = 0
    while len(password) < n:
        password.append(chars[i % k])
        i += 1
        # Varmistetaan, ettei tule kahta samaa peräkkäin:
        while len(password) >= 2 and password[-1] == password[-2]:
            i += 1
            password[-1] = chars[i % k]

    print(''.join(password))

# Lue syöte ja suorita
n, k = map(int, input().split())
generate_password(n, k)

GPT toteuttaa suhteellisen muistisyöpön ja hitaamman ratkaisun, joka lähtee erikseen tarkistamaan etteivät merkit ole samoja.
Tämä voidaan kuitenkin ohittaa annetuilla ehdoilla. 
On huomattava, että ratkaisuni EI OLE salasanageneraattori, se toimii tässä tehtävässä. 

SUORITUS STATISTIIKKA
GPT 124 ms	2800 KB
OMA 93 ms	200 KB

LINKKI
https://codeforces.com/problemset/problem/770/A


'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):

        n,k=cases
        ref = list(set('abcdefghijklmnopqrstuvwxyz'))#set ei säilytä järjestystä. 
        result=''
        repetition=''
        for i in range(k):#Tehdään toistokierros
            repetition=repetition+ref[i]

        times=divmod(n,k)
        result=repetition*max(1, times[0])#ei kerrota nollalla. 

        for i in range(times[1]):#Maksimissaan k-1 eli nopea
            result=result+repetition[i]#Täydentää salasanan vajaan toistokierroksen verran. 

        return result

if __name__ =='__main__':
    cases=list(map(int,input().split()))

    test_class=XXX2(cases)
    print(test_class.XXX())
