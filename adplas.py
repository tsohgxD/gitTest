import requests
from bs4 import BeautifulSoup

Websites = ["https://linux1st.com/images/free_lpic1_book_and_videos_jadi.pdf"]

for url in Websites:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    text = soup.get_text()

    print("\n--- WEBSITE ---")
    print(url)
    print(text[:500])

 
