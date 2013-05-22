IPL
===

Basic analysis of IPL stats

Assumptions:
---

Wasn't able to find an API for IPL stats, so downloaded the web page and scrapped the table that contains
the player stats. 

Current implementation:
---

Right now wrote a script that can read this table and display the stats. But the intent is to clean up and 
move these stats to a datastructure that can be queried easily to figure out things like which player is the
best bet. 

Future plans:
---

Sample Outputs :

```
 TEAMS SORTED BY POINTS 
------------------------
{u'chennai-super-kings': 1919.0,
 u'delhi-daredevils': 1544.5,
 u'kings-xi-punjab': 1714.5,
 u'kolkata-knight-riders': 1709.5,
 u'mumbai-indians': 1881.0,
 u'pune-warriors-india': 1489.5,
 u'rajasthan-royals': 1583.0,
 u'royal-challengers-bangalore': 1795.0,
 u'sunrisers-hyderabad': 1761.5}
#########################
 TEAMS SORTED BY WICKETS 
------------------------
{u'chennai-super-kings': 91,
 u'delhi-daredevils': 62,
 u'kings-xi-punjab': 69,
 u'kolkata-knight-riders': 82,
 u'mumbai-indians': 89,
 u'pune-warriors-india': 65,
 u'rajasthan-royals': 69,
 u'royal-challengers-bangalore': 84,
 u'sunrisers-hyderabad': 92}
```
