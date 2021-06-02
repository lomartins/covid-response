import requests
import pandas as pd

# url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv'


def update():
    r = requests.get(url, allow_redirects=True)
    open('./data/covid-data.csv', 'wb').write(r.content)


def manipulate():
    df = pd.read_csv(r'./data/covid-data.csv')
    print(df)


if __name__ == '__main__':
    manipulate()
