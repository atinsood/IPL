"""
 Assumes a specific format of the input HTML file and will read the stats from specific tags
"""

from bs4 import BeautifulSoup

if __name__ == '__main__':
    statsFileAsString = ''
    with open('data/IPLStats.html') as statsFile:
        statsFileAsString = statsFile.read()

    soup = BeautifulSoup(statsFileAsString)
    for row in soup.find_all('tr'):
        rowData = ''
        for column in row.find_all('td'):
            rowData = rowData + "\t" + column.text.strip()

        print rowData
