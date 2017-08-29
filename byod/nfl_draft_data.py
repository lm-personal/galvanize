#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

from bs4 import BeautifulSoup
import requests
import csv



#<--------------------------[Cleaner Functions]------------------------------>



def normalize_vert(data):
    data = data.split()

    if len(data) > 1:
        data = int(data[0]) + .5
    else:
        data = float(data[0])

    return data



def normalize_broad(data):
    data = data.strip().strip('"').split('\'')

    data = int(data[0]) * 12 + int(data[1])

    return data



def normalize(data_type, data):
    if data_type == 'vert':
        return normalize_vert(data)
    if data_type == 'broad':
        return normalize_broad(data)


def get_cleaner():
    cleaner =       {   'name'    : lambda x: x.strip('*'),
                        'school'  : None,
                        'none'    : None,
                        'height'  : lambda x: (int(x.split('-')[0]) * 12) + int(x.split('-')[1]),
                        'weight'  : lambda x: int(x.strip()),
                        '40time'  : lambda x: float(x.strip()),
                        'bench'   : lambda x: int(x.strip()),
                        'vert'    : lambda x: normalize('vert', x),
                        'broad'   : lambda x: normalize('broad', x),
                        'shuttle' :lambda x: float(x.strip()),
                        '3cone'   :lambda x: float(x.strip())
                    }

    return cleaner

#<---------------------------------------------------------------------------------------------------->


def make_html(position, year, itemnum):
    # Craft url of page to scrape
    base_url = 'http://www.nfldraftscout.com/ratings/players.php'
    payload = { 'genpos':position,
                'draftyear':year,
                'sortby':'tsxpos',
                'order':'ASC',
                'startspot':itemnum}

    r = requests.get(base_url, params=payload)
    #print(r.url)

    page_html = BeautifulSoup(r.text, 'lxml')
    #print(page_html.prettify())

    return page_html



def get_player(player, cleaner):

    # Get and normalize players data
    player_data = []
    for index, element in enumerate(player.find_all("font", color = "#000000")):

        if element.string == ' ':
             player_data.append(None)
             continue

        if index == 1: player_data.append(cleaner['name'](element.string))
        if index == 2: player_data.append(element.string)
        if index == 4: player_data.append(cleaner['height'](element.string))
        if index == 5: player_data.append(cleaner['weight'](element.string))
        if index == 6: player_data.append(cleaner['40time'](element.string))
        if index == 7: player_data.append(cleaner['bench'](element.string))
        if index == 8: player_data.append(cleaner['vert'](element.string))
        if index == 9: player_data.append(cleaner['broad'](element.string))
        if index == 10: player_data.append(cleaner['shuttle'](element.string))
        if index == 11: player_data.append(cleaner['3cone'](element.string))

    return player_data



def add_data(data, dictionary, position):
    # Build a dictionary entry for the player and add it to the player dictionary
    items = zip(['height', 'weight', '40time', 'bench', 'vert', 'broad', 'shuttle', '3cone'],
                data[2:])

    key = ( data[0].split()[0],
            data[0].split()[1],
            data[1],
            position)

    dictionary[position][key] = dict(items)

    return dictionary



def main():
    # Dictionary the scraper will fill out
    player_dict =   {   'QB' : {},
                        'RB' : {},
                        'FB' : {},
                        'TE' : {},
                        'WR' : {},
                        'C' : {},
                        'OT' : {},
                        'OG' : {},
                        'K' : {},
                        'DE' : {},
                        'DT' : {},
                        'ILB' : {},
                        'OLB' : {},
                        'CB' : {},
                        'FS' : {},
                        'SS' : {},
                        'P' : {}
                    }

    year = '2017'

    cleaner = get_cleaner()

    for position in player_dict:
        for itemnum in range(0,41,10):

            html = make_html(position, year, itemnum)

            # Get a player
            for player in html.find_all("tr",  bgcolor = ["#D7D7D7", "#EEEEEE"]):
                player_data = get_player(player, cleaner)
                player_dict = add_data(player_data, player_dict, position)

    return player_dict





if __name__=="__main__":
    final_player_dict = main()

    fieldnames = ['first_name', 'last_name', 'school', 'position', 'height', 'weight', '40time', 'bench', 'vert', 'broad', 'shuttle', '3cone']
    with open('data.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for position in final_player_dict:
            for player in final_player_dict[position]:

                key_dict = dict(zip(('first_name', 'last_name', 'school'), player))

                value_dict = final_player_dict[position][player]

                out_dict = {}
                out_dict.update(key_dict)
                out_dict.update({'position':position})
                out_dict.update(value_dict)

                writer.writerow(out_dict)
