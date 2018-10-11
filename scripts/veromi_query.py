import pandas as pd
import requests
from bs4 import BeautifulSoup
import unidecode

def query(inputs):
    '''
    inputs = [jobs, ind, k]
    job: Job ID (number between 0 and number of necessary jobs to run)
    ind: dataframe of individuals (required columns are 'first_name', 'middle_name', 'last_name', city', 'state')
    k: number of names queries in every hit
    out: how ofter do you want to see an output file created to track progress?
    '''

    job = inputs[0]
    ind = inputs[1]
    k = inputs[2]
    out = inputs[3]

    ids = []
    names_ages = []
    cities = []

    for i in range(k*job, k*(job+1)):

        # Print progress indicator if necessary
        if i%out==0:
            print(i)

        if i>=ind.shape[0]:
            continue

        # Construct Query URL
        url = "http://www.veromi.net/Summary.asp?"
        url += "fn={}".format(ind['first_name'][i].replace(' ', '+'))
        url += "&mn={}".format(ind['middle_name'][i].replace(' ', '+'))
        url += "&ln={}".format(ind['last_name'][i].replace(' ', '+'))
        url += "&age="
        url += "&city={}".format(ind['city'][i].replace(' ', '+'))
        url += "&state={}".format(ind['state'][i])
        url += "&vw="
        url += "&Search=&Input=&x=0&y=0"

        # Request URL
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            print("\nError on Individual {}".format(i))
            print(e)
            continue

        soup_multiple = BeautifulSoup(response.text, 'html.parser')

        # Parse out name
        teaser = soup_multiple.find(class_ = 'Teaser')
        if teaser is not None:

            for elem in teaser.find_all(valign='top'):

                name_age = None
                city_list = None

                # Parse out name:
                name_age = elem.find_all('td')[1].find('a').get_text()
                name_age = unidecode.unidecode(name_age)

                # Parse out cities:
                city_info_flag = elem.find_all('td')[4].find('small')
                if city_info_flag is not None:
                    city_list = city_info_flag.get_text(strip=True, separator="; ").replace(',;', ',').replace('; ,', ',')
                    city_list = unidecode.unidecode(city_list)

                ids.append(ind['id'][i])
                names_ages.append(name_age)
                cities.append(city_list)

    profiles = pd.DataFrame({'id': ids, 'name_age': names_ages, 'cities': cities})

    profiles.to_csv('../output/scraper_output/intermediate/profiles_{}.csv'.format(job), index=False)

    return profiles
