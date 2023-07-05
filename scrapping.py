import requests
from bs4 import BeautifulSoup
import csv

result_file = open("result.csv", "w", encoding="utf-8")
writer = csv.writer(result_file, delimiter=",")
header = ['Name', 'Year', 'Wins', 'Losses', 'OT Losses', 'Percentage', 'GF', 'GA', 'Difference']

writer.writerow(header)

for i in range(10):
    url = f"https://www.scrapethissite.com/pages/forms/?page_num={i}"
    s = requests.Session()
    response = s.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    rows = soup.find_all("tr", class_="team")

    for row in rows[1:]:

        data = [td.text.strip() for td in row.find_all("td")]

        goals_against = int(data[7].replace(".", ""))

        diff = int(data[8].replace(".", ""))

        if diff > 0 and goals_against < 300:

            writer.writerow(data)

result_file.close()