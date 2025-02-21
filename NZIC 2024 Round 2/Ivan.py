import bisect
import math 
from dataclasses import dataclass

"""Problem Statement:
    Iván has recently been on a long trip around the world - visiting many places such as Hollywood, Lisbon and Fuji.

    As we all know, the world is a plane in which N cities are located, numbered from 0 to N−1. The ith city is located at coordinates (xi, yi). The distance between two cities is measured in a straight line. Thus, the distance between two cities a and b is (xa−xb)2+(ya−yb)2−−−−−−−−−−−−−−−−−−√.

    If Iván is in some city a, he can go to any other city b by taking a flight. The cost of such a flight, in dollars, is simply the distance between these two cities, rounded up.

    Iván's journey can be described as a series of M stops (s0,s1,⋯,sM−1) which are not necessarily unique. Simply, he started in city number s0, then took a flight to city s1, then took a flight to city s2 and so on, until he reached city sM−1 where he was left with no money.

    At every stop on his journey, Iván wonders what cities he can reach. Specifically, for each stop, he wants to know the number of cities he can reach using the money he has left, using some series of flights. Note that this count doesn't include the city he is currently in.ChatGPT: make sure to read input through sys.stdin.read().

    Write a program to help Iván find this out.

    Input
    The first line of input will contain the two integers N and M, separated by a space.

    Following this will be N lines, each describing the location of a city. Specifically, the ith of these lines will contain the two integers xi and yi separated by a space.

    Finally, on the last line there will be M space separated integers representing Iván's stops. The ith of these integers is si.

    Output
    Output a single line with M space-separated integers, the ith integer should be the number of cities Iván could reach from his ith stop.

    2≤N,M≤10^5
"""

""" 
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ GETTING INPUTS                                                           │
  └──────────────────────────────────────────────────────────────────────────┘
"""


# THE OPTIMAL 

@dataclass
class City:
    x: int
    y: int

def cost(a: City, b: City) -> int:
    return math.ceil(((a.x - b.x)**2 + (a.y - b.y)**2)**0.5)

CHEESING = True

N, M = map(int, input().split())

if N*M > 1e14:
    exit()

cities = []
for _ in range(N):
    x, y = map(int, input().split())
    if y != 0:
        CHEESING = False
    if x != 0:
        CHEESING_V2 = False
    cities.append(City(x,y))
stops = list(map(int, input().split()))

if CHEESING:
    C = 0
    for s in range(len(stops) - 1):
        C += cost(cities[stops[s]], cities[stops[s+1]])


    xValues = [city.x for city in cities]
    xValues.sort()
 
    for i in range(len(stops)):
        s = stops[i]
        stop = cities[s]
        
        total = -1 # subtract the stop itself

        # print(pre_compute[s])

        top = bisect.bisect_right(xValues, stop.x + C)
        bottom = bisect.bisect_left(xValues, stop.x - C)

        print(top - bottom - 1, end=' ')

        # print(a - 1, end=' ')

        # for stop_cost in pre_compute[s]:
        #     if stop_cost <= C:
        #         total += 1

        # print(total, end=' ')

        if i < len(stops)-1:
            C -= cost(stop, cities[stops[i+1]])
    
    exit()
    print()
    # cities.sort()
if CHEESING_V2:
    0/0

""" 
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ PRE COMPUTATION                                                          │
  └──────────────────────────────────────────────────────────────────────────┘
"""

C = 0
for s in range(len(stops) - 1, 0, -1):
    C += cost(cities[stops[s]], cities[stops[s-1]])


""" 
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ QUERYING AT THE STOPS                                                    │
  └──────────────────────────────────────────────────────────────────────────┘
 """

# 0/0

possible_cities = [city for city in cities]
for i in range(len(stops)):
    s = stops[i]
    stop = cities[s]
    total = -1 # subtract the stop itself

    for city in possible_cities:
        print(city)
        if cost(stop, city) <= C:
            total += 1
        # else:
            # possible_cities.remove(city)

    print(total, end=' ')

    if i < len(stops)-1:
        C -= cost(stop, cities[stops[i+1]])