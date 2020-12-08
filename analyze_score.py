from bs4 import BeautifulSoup
import score_html
soup = BeautifulSoup(score_html.score,"lxml")
table = soup.find_all('tr')
tmp = []
for row in table:
    for item in row.find_all("td"):
        string = item.get_text()
        print(f"len(string) = {len(string)}")
        if not(len(string) == 78):
            print
        print(string.split())
        tmp.append(string.split())
#print(tmp)
