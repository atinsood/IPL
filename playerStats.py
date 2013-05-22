"""
 Assumes a specific format of the input HTML file and will read the stats from specific tags
"""

from bs4 import BeautifulSoup
import pprint


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
    playerModel = {'position': 0, 'name': '','playerID': 0, 'team': '', 'matches': 0, 'wickets': 0, 'dots': 0, 'fours': 0,
                   'sixes': 0, 'catches': 0, 'stumpings': 0, 'points': 0}
    """
    players = []
    rowsOfPlayer = soup.find_all('tr')

    for i in range(1, len(rowsOfPlayer)):
        row = rowsOfPlayer[i]
        columns = row.find_all('td')
        playerModel = dict()
        playerModel['position'] = int(columns[0].text.strip())
        playerModel['name'] = columns[1].text.strip()

        #Can be defined as a lambda function
        playerDetails = columns[1].a.get('href').split("/")
        playerModel['playerID'] = int(playerDetails[-3])
        playerModel['team'] = playerDetails[-5]

        playerModel['matches'] = int(columns[2].text.strip())
        playerModel['wickets'] = int(columns[3].text.strip())
        playerModel['dots'] = int(columns[4].text.strip())
        playerModel['fours'] = int(columns[5].text.strip())
        playerModel['sixes'] = int(columns[6].text.strip())
        playerModel['catches'] = int(columns[7].text.strip())
        playerModel['stumpings'] = int(columns[8].text.strip())
        playerModel['points'] = float(columns[9].text.strip())

        players.append(playerModel)

    return players


def mostValuedTeam(players, variableToInspect='points'):
    #TODO Can add kwargs here to get a table of totals of wickets, runs etc by team
    """
        Iterates through all the players, figures out their teams and sums <variableToInspect> for players belonging to
        the same team
        team1 : total<variableToInspect>
        team2 : total<variableToInspect>
    """
    teamDict = dict()
    for player in players:
        team = player['team']
        points = player[variableToInspect]
        if team in teamDict.keys():
            teamDict[team] = teamDict[team] + points
        else:
            teamDict[team] = points

    pprint.pprint(teamDict)


if __name__ == '__main__':
    soup = parseStatsFile()
    players = getPlayerStats(soup)

    # for player in players:
    #     print(player)

    print(' TEAMS SORTED BY POINTS ')
    print('------------------------')
    mostValuedTeam(players, 'points')
    print('#########################')
    print(' TEAMS SORTED BY WICKETS ')
    print('------------------------')
    mostValuedTeam(players, 'wickets')
