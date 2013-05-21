"""
 Assumes a specific format of the input HTML file and will read the stats from specific tags
"""

from bs4 import BeautifulSoup


def parseStatsFile(statsFileLocation='data/IPLStats.html'):
    """
    Parses the stats file and returns the parser
    """
    with open(statsFileLocation) as statsFile:
        statsFileAsString = statsFile.read()
    soup = BeautifulSoup(statsFileAsString)
    return soup


def getPlayerStats(soup):
    """

    Takes the parser and fetches all the requires stats.
    Converts each row into a data model and then appends them to a list

    Data model used by PlayerModel
    playerModel = {'position': 0, 'name': '', 'matches': 0, 'wickets': 0, 'dots': 0, 'fours': 0,
                   'sixes': 0, 'catches': 0, 'stumpings': 0, 'points': 0}
    """
    players = []
    rowsOfPlayer = soup.find_all('tr')

    for i in range(1, len(rowsOfPlayer)):
        row = rowsOfPlayer[i]
        columns = row.find_all('td')
        playerModel = dict()
        playerModel['position'] = columns[0].text.strip()
        playerModel['name'] = columns[1].text.strip()
        playerModel['matches'] = columns[2].text.strip()
        playerModel['wickets'] = columns[3].text.strip()
        playerModel['dots'] = columns[4].text.strip()
        playerModel['fours'] = columns[5].text.strip()
        playerModel['sixes'] = columns[6].text.strip()
        playerModel['catches'] = columns[7].text.strip()
        playerModel['stumpings'] = columns[8].text.strip()
        playerModel['points'] = columns[9].text.strip()

        players.append(playerModel)

    return players


if __name__ == '__main__':

    soup = parseStatsFile()
    players = getPlayerStats(soup)

    for player in players:
        print player


