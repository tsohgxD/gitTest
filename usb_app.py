import requests
from bs4 import BeautifulSoup

Websites = []


print("\nDober dan Wilkommen kod moj program gje je sehr speziallisiert.\n")

x = input("Hoces anleitung kako programm ide?\nDa = 1 Ne = 2\nInput:  ")
    

if x == "1":
    print("\nEgal koja Website, ti moses uset Link i onda hinzufügen Link, i on ce tebi sa tvoje keyworte sve aktuelle nachrichten anzeigen.")
    print("Ali sto je to nutzvoll mozes schnell selber gledat ili search per google, aliiiii ti moses ako hoces sa moj programm 10 verschiedene seiten")
    print("Imat i svi oni per knopfdruck cu tebi schicken sve infomation zb Ukraine krieg, A sto google to nemose, sato sto ti moses egal koju webseite")
    print("Stavit i tvoje links bleiben permanenet ti moses imat 50+ seiten/artikel i stalno odma sve infomationen dobit od egal koji thema to")
    print("tebi manuell isto sa KI treba minimum 10-20minuten, sa moj programm 1 knopfdruck.\n\n")
    input("Pritisni 'Enter' ako si gotov: \n")
    


while True: 
    user_input = input("Molimte copy-paste tvoj link (da exit programm napisite '-9'): ")
    if user_input == "-9":
            break
    Websites.append(user_input)


for index, site in enumerate(Websites):
    print(f"{index + 1}. {site}")
    
for url in Websites:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    text = soup.get_text()

    print("\n--- WEBSITE ---")
    print(url)
    print(text[:500])
 