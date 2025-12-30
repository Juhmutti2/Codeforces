'''
A. Password Check
time limit per test1 second
memory limit per test256 megabytes
You have probably registered on Internet sites many times. And each time you should enter your invented password. Usually the registration form automatically checks the password's crypt resistance. If the user's password isn't complex enough, a message is displayed. Today your task is to implement such an automatic check.

Web-developers of the company Q assume that a password is complex enough, if it meets all of the following conditions:

the password length is at least 5 characters;
the password contains at least one large English letter;
the password contains at least one small English letter;
the password contains at least one digit.
You are given a password. Please implement the automatic check of its complexity for company Q.

Input
The first line contains a non-empty sequence of characters (at most 100 characters). Each character is either a large English letter, or a small English letter, or a digit, or one of characters: "!", "?", ".", ",", "_".

Output
If the password is complex enough, print message "Correct" (without the quotes), otherwise print message "Too weak" (without the quotes).

Examples
InputCopy
abacaba
OutputCopy
Too weak
InputCopy
X12345
OutputCopy
Too weak
InputCopy
CONTEST_is_STARTED!!11
OutputCopy
Correct


SYÖTE
yksi rivi salasanaa. 
KOMPAKTI
Tarkistetaan täyttyykö ehdot:
the password length is at least 5 characters;
the password contains at least one large English letter;
the password contains at least one small English letter;
the password contains at least one digit.

RATKAISU
Ehtolauseella mennään. 

GPT 4.0 TARJOAA

password = input()

has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)

if len(password) >= 5 and has_upper and has_lower and has_digit:
    print("Correct")
else:
    print("Too weak")

Käytännössä sama koodi, hiukan lukijaystävällisemmin esitettynä. 


SUORITUS STATISTIIKKA
GPT 109 ms	200 KB
OMA 109 ms	200 KB

LINKKI
https://codeforces.com/problemset/problem/411/A

'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):

        if len(cases)>=5 and any(char.isupper() for char in cases) and any(char.islower() for char in cases) and any(char.isdigit() for char in cases):
            return 'Correct'
        return 'Too weak'

if __name__ =='__main__':
    cases=input()

    test_class=XXX2(cases)
    print(test_class.XXX())
