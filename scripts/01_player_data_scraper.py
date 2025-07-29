from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv
import time
import random

#function to scrape website
def web_scrape_1year(url, season, team_name):
    
    #custom user agent to fake identity so site doesn't block scraper
    request_headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'
    }
    
    #source
    source = requests.get(url, headers=request_headers).text
    soup = BeautifulSoup(source, 'html.parser')
    
    #league of the team
    league = soup.find('div', class_='clubs')
    league1 = league.find('span', class_='header_end')
    finalleague = league1.text.replace('(', '').replace(')', '')
    
    if finalleague != 'Premier League':
        print('Not Premier League Season')
        return None

    #table
    table = soup.find('table', class_='stats_table sortable min_width')

    #scraping the titles of columns
    instance = []
    for header in table.find_all('thead'):
        for row in header.find_all('th'):
            if 'over_header' in row.get('class', []):
                continue
            if '' in row:
                continue
            instance.append(row.text.strip())
    instance = list(filter(None, instance))
        
    #list stats of every team of first table
    modest = []
    arsenal = soup.find('tbody')
    for arsenal2 in arsenal.find_all('tr'):
        for lister in arsenal2.find_all(['th', 'td']):
            modest.append(lister.text.strip())


    # function that changes the modest list from being flat to a 2d table
    def flat_to_df(flatlist, num_columns, column_names=None):
        table_rows = [flatlist[i:i + num_columns] for i in range(0, len(flatlist), num_columns)]
        
        df = pd.DataFrame(table_rows, columns=column_names)
        return df
    
    #if statement to handle if data is incomplete
    if len(modest) % len(instance) != 0:
        print(f'DATA MISMATCH for {team_name} in {season}')
        return None
    
    #using flat to df function
    num_cols = len(instance)
    col_names = instance
    df_data = flat_to_df(modest, num_cols, col_names)
    df_data.insert(0, 'Season', season)
    df_data.insert(3, 'Team', team_name)
    return df_data

#team dictionary name+urlcode for looping through urls for teams
teams = {
    'Arsenal': '18bb7c10',
    'Aston-Villa': '8602292d',
    'Bournemouth': '4ba7cbea',
    'Brentford': 'cd051869',
    'Brighton-and-Hove-Albion': 'd07537b9',
    'Cardiff-City': '75fae011',
    'Chelsea': 'cff3d9bb',
    'Crystal-Palace': '47c64c55',
    'Everton': 'd3fd31cc',
    'Fulham': 'fd962109',
    'Huddersfield-Town': 'f5922ca5',
    'Ipswich-Town': 'b74092de',
    'Leeds-United': '5bfb9659',
    'Leicester-City': 'a2d435b3',
    'Liverpool': '822bd0ba',
    'Manchester-City': 'b8fd03ef',
    'Manchester-United': '19538871',
    'Newcastle-United': 'b2b47a98',
    'Norwich-City': '1c781004',
    'Nottingham-Forest': 'e4a775cb',
    'Southampton': '33c895d4',
    'Sheffield-United': '1df6b87e',
    'Stoke-City': '17892952',
    'Swansea-City': 'fb10988f',
    'Tottenham-Hotspur': '361ca564',
    'Watford': '2abfe087',
    'West-Bromwich-Albion': '60c6b05f',
    'West-Ham-United': '7c21e445',
    'Wolverhampton-Wanderers': '8cec06e1'
}

#most recent season swish to go through
year1 = 2023
year2 = 2024

#setting to compare to outputted columns, if wrong can continue loop and skip
expected_columns = 36

#period length: how many years back want to go
perlength = 6

confin = []
for i in range(perlength):
    for team_name, team_code in teams.items():
        url = f'https://fbref.com/en/squads/{team_code}/{year1}-{year2}/{team_name}-Stats'
        print(f"--- Scraping: {team_name} for season {year1}-{year2} ---")
        con = web_scrape_1year(url, f'{year1}-{year2}', f'{team_name}')
        sleep_duration = random.uniform(5, 15)
        time.sleep(sleep_duration)
        if con is None:
            print('Skipping, None!')
            continue
        if expected_columns != con.shape[1]:
            print('Skipping, columns dont align')
            continue
        else:
            confin.append(con)
    sleep_duration = random.uniform(20, 40)
    time.sleep(sleep_duration)
    year1 -= 1
    year2 -= 1
    

result = pd.concat(confin, ignore_index=True)
print(result)
    
result.to_csv('PremierFull2018-2024.csv', encoding='utf-8-sig', index=False)
