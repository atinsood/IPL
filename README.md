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
TBD

Sample Outputs :
---

```
 TEAMS SORTED BY POINTS 
------------------------
[(u'chennai-super-kings', 1919.0),
 (u'mumbai-indians', 1881.0),
 (u'royal-challengers-bangalore', 1795.0),
 (u'sunrisers-hyderabad', 1761.5),
 (u'kings-xi-punjab', 1714.5),
 (u'kolkata-knight-riders', 1709.5),
 (u'rajasthan-royals', 1583.0),
 (u'delhi-daredevils', 1544.5),
 (u'pune-warriors-india', 1489.5)]
#########################
 TEAMS SORTED BY WICKETS 
------------------------
[(u'sunrisers-hyderabad', 92),
 (u'chennai-super-kings', 91),
 (u'mumbai-indians', 89),
 (u'royal-challengers-bangalore', 84),
 (u'kolkata-knight-riders', 82),
 (u'rajasthan-royals', 69),
 (u'kings-xi-punjab', 69),
 (u'pune-warriors-india', 65),
 (u'delhi-daredevils', 62)]
#########################
 TEAMS SORTED BY Runs 
------------------------
[(u'chennai-super-kings', 2555),
 (u'mumbai-indians', 2543),
 (u'royal-challengers-bangalore', 2430),
 (u'rajasthan-royals', 2415),
 (u'kings-xi-punjab', 2312),
 (u'pune-warriors-india', 2183),
 (u'sunrisers-hyderabad', 2178),
 (u'kolkata-knight-riders', 2134),
 (u'delhi-daredevils', 2103)]
#########################
 TEAMS SORTED BY 6s 
------------------------
[(u'mumbai-indians', 108),
 (u'royal-challengers-bangalore', 103),
 (u'chennai-super-kings', 78),
 (u'pune-warriors-india', 76),
 (u'rajasthan-royals', 69),
 (u'kings-xi-punjab', 65),
 (u'kolkata-knight-riders', 56),
 (u'sunrisers-hyderabad', 52),
 (u'delhi-daredevils', 51)]
#########################
 TEAMS SORTED BY 4s 
------------------------
[(u'rajasthan-royals', 245),
 (u'kings-xi-punjab', 244),
 (u'chennai-super-kings', 233),
 (u'royal-challengers-bangalore', 229),
 (u'kolkata-knight-riders', 222),
 (u'mumbai-indians', 219),
 (u'delhi-daredevils', 210),
 (u'sunrisers-hyderabad', 196),
 (u'pune-warriors-india', 190)]
```
