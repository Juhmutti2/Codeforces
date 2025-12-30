'''

A. Restoring Password
time limit per test2 seconds
memory limit per test256 megabytes
Igor K. always used to trust his favorite Kashpirovsky Antivirus. That is why he didn't hesitate to download the link one of his groupmates sent him via QIP Infinium. The link was said to contain "some real funny stuff about swine influenza". The antivirus had no objections and Igor K. run the flash application he had downloaded. Immediately his QIP Infinium said: "invalid login/password".

Igor K. entered the ISQ from his additional account and looked at the info of his main one. His name and surname changed to "H1N1" and "Infected" correspondingly, and the "Additional Information" field contained a strange-looking binary code 80 characters in length, consisting of zeroes and ones. "I've been hacked" — thought Igor K. and run the Internet Exploiter browser to quickly type his favourite search engine's address.

Soon he learned that it really was a virus that changed ISQ users' passwords. Fortunately, he soon found out that the binary code was actually the encrypted password where each group of 10 characters stood for one decimal digit. Accordingly, the original password consisted of 8 decimal digits.

Help Igor K. restore his ISQ account by the encrypted password and encryption specification.

Input
The input data contains 11 lines. The first line represents the binary code 80 characters in length. That is the code written in Igor K.'s ISQ account's info. Next 10 lines contain pairwise distinct binary codes 10 characters in length, corresponding to numbers 0, 1, ..., 9.

Output
Print one line containing 8 characters — The password to Igor K.'s ISQ account. It is guaranteed that the solution exists.

Examples
InputCopy
01001100100101100000010110001001011001000101100110010110100001011010100101101100
0100110000
0100110010
0101100000
0101100010
0101100100
0101100110
0101101000
0101101010
0101101100
0101101110
OutputCopy
12345678
InputCopy
10101101111001000010100100011010101101110010110111011000100011011110010110001000
1001000010
1101111001
1001000110
1010110111
0010110111
1101001101
1011000001
1110010101
1011011000
0110001000
OutputCopy
30234919


SYÖTE
80 merkkiä, jotka kuvaavat kryptattua salasanaa
merkit 0-9 kryptattuna

KOMPAKTI
Mikä oli alkuperäinen salasana kun se koostuu merkeistä 0-9.

RATKAISU
käydään kryptattu jono 10 askelissa läpi ja verrataan mihin numbers alkioon askelväli osuu.
Askelvälin indeksi = numero

GPT 4.0 TARJOAA

# Lue binäärinen salasana (80 merkkiä)
encrypted = input().strip()

# Lue 10 binäärikoodia, jotka vastaavat numeroita 0-9
code_map = {}
for i in range(10):
    binary_code = input().strip()
    code_map[binary_code] = str(i)  # esim. "0100110010": "1"

# Puretaan salasana 10 merkin paloissa
password = ""
for i in range(0, 80, 10):
    chunk = encrypted[i:i+10]
    password += code_map[chunk]

print(password)

GPT tarjoaa aavistuksen hitaampaa versiota, joka tekee sanakirjan jokaisesta numero - numerojono yhdistelmästä.
Ajatus on hyvä, mutta tässä tehtävässä täysin tarpeeton. 


SUORITUS STATISTIIKKA
GPT 186 ms	200 KB
OMA 156 ms	200 KB

LINKKI
https://codeforces.com/problemset/problem/94/A

'''




class XXX2:
    def __init__(self,cases):
        self.cases=cases

    def XXX(self):
        s,numbers=self.cases
        result=''

        for i in range(0,80,10):#tarvittava alku, loppu, askel
            current=s[i:i+10]#Nykyinen lohko
            for j in range(10):
                    if current==numbers[j]:#mitä indeksiä lohko vastaa
                        result=result+str(j)
                        break
        return result

if __name__ =='__main__':
    numbers=[]
    s=input()
    for _ in range(10):
        numbers.append(input())
    cases=[s,numbers]
    test_class=XXX2(cases)
    print(test_class.XXX())