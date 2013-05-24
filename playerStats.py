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


def getBatsmenStats(soup):
    """
        Takes the parser which was created for batsmen and creates a record for all the stats mentioned
        Reason certain attributes are kept as string vs float or int is that these fields can have - , *  , ''
    """
    #TODO Need to abstract out the common code from the player and batsman function

    batsmen = []
    rowOfBatsmen = soup.find_all('tr')

    for i in range(1, len(rowOfBatsmen)):
        row = rowOfBatsmen[i]
        columns = row.find_all('td')
        batsmanModel = dict()
        batsmanModel['position'] = int(columns[0].text.strip())
        batsmanModel['name'] = columns[1].text.strip()

        #Can be defined as a lambda function
        batsmenDetails = columns[1].a.get('href').split("/")
        batsmanModel['playerID'] = int(batsmenDetails[-3])
        batsmanModel['team'] = batsmenDetails[-5]

        batsmanModel['matches'] = int(columns[2].text.strip())
        batsmanModel['innings'] = int(columns[3].text.strip())
        batsmanModel['notOuts'] = int(columns[4].text.strip())
        batsmanModel['runs'] = int(columns[5].text.strip())
        batsmanModel['highScore'] = (columns[6].text.strip())
        batsmanModel['average'] = (columns[7].text.strip())
        batsmanModel['bf'] = (columns[8].text.strip())
        batsmanModel['strikeRate'] = (columns[9].text.strip())
        batsmanModel['100s'] = int(columns[10].text.strip())
        batsmanModel['50s'] = int(columns[11].text.strip())
        batsmanModel['4s'] = int(columns[12].text.strip())
        batsmanModel['6s'] = int(columns[13].text.strip())

        batsmen.append(batsmanModel)

    return batsmen


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
            #TODO This function to do addition or any other calculation should be configurable
            #by making it as a variable
            teamDict[team] = teamDict[team] + points
        else:
            teamDict[team] = points

    pprint.pprint(teamDict)


if __name__ == '__main__':
    playerSoup = parseStatsFile()
    players = getPlayerStats(playerSoup)

    batsmenSoup = parseStatsFile('data/IPLRuns.html')
    batsmen = getBatsmenStats(batsmenSoup)

    #for bastsman in batsmen:
    #    print bastsman

    # for player in players:
    #     print(player)

    print(' TEAMS SORTED BY POINTS ')
    print('------------------------')
    mostValuedTeam(players, 'points')
    print('#########################')
    print(' TEAMS SORTED BY WICKETS ')
    print('------------------------')
    mostValuedTeam(players, 'wickets')


    print('#########################')
    print(' TEAMS SORTED BY Runs ')
    print('------------------------')
    mostValuedTeam(batsmen, 'runs')
    print('#########################')
    print(' TEAMS SORTED BY 6s ')
    print('------------------------')
    mostValuedTeam(batsmen, '6s')
    print('#########################')
    print(' TEAMS SORTED BY 4s ')
    print('------------------------')
    mostValuedTeam(batsmen, '4s')
