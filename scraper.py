import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrape_race_data(url):
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")

        dog_rows = soup.select(".race-form-table tbody tr")

        if not dog_rows:
            return pd.DataFrame()

        data = []
        for row in dog_rows:
            cols = row.find_all("td")
            if len(cols) < 4:
                continue

            box = cols[0].get_text(strip=True)
            name = cols[1].get_text(strip=True)
            form = cols[2].get_text(strip=True)
            time = cols[3].get_text(strip=True)

            data.append({
                "Box": box,
                "Name": name,
                "Form": form,
                "Time": time
            })

        return pd.DataFrame(data)

    except Exception as e:
        return pd.DataFrame()
