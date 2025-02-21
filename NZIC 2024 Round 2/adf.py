# We are given N cities which are represented as a point on the x,y plane, the cost of travelling between 2 points is the euclidean distance rounded up.
# We are given a path of M cities, and we start off with just enough money for the entire trip.

# For each city we stop at along the trip. Print the number of cities we can reach from that city with our remaining money.

# The first line of input contains 2 integers N and M (2≤N,M≤10^5) - the number of cities and the length of the path.
# The next N lines will contain 2 integers x and y (0≤x,y≤10^9) - the coordinates of the cities.
# The last line will contain M integers si (0≤si<N) - the cities we stop at.

# Output M integers, the number of cities we can reach from each stop.

# 