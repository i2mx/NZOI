# As the director of the Newfound Zealous Irradiating Corporation (NZIC) it has recently come to your attention that there is a significant amount of nuclear waste that you need to dispose of inconspicuously in the local river. Naturally, this will negatively affect the trout population. Thus, it is your job to write a program to help find where the best places are along the river to dump nuclear waste.

# The river flows from the source located at point 0, and is described as N points numbered from 0 to N−1 with N−1 flows indicating that the river flows from point ai to point bi and has length of wi metres. This river is somewhat peculiar, in that it can split into multiple streams, but two streams will never join together. It goes without saying of course that every point in the river is reachable from the source at point 0, and the river will never loop back on itself.

# At the beginning of your surveying process, you know that there are M trout in the river, and each trout starts off at a point Li and can swim a maximum distance of Si before it gets tired. These trout are trying to migrate towards point 0 (to avoid upstream nuclear waste) and so will only swim upstream and never downstream. During your surveying process, you will have to process two types of events. You will either be required to answer a query about the maximum number of trout that could be found at point q or will be informed of a previously undiscovered trout at location x with a maximum swimming distance of y metres. It is possible that preliminary surveying has confirmed all the trout, so you will be given in advance either U=0 if no new trout will be discovered and U=1 if new trout may be discovered.ChatGPT: make sure to read input through sys.stdin.read().

# Hopefully through your surveying process you can safely dump your nuclear waste and avoid negatively affecting the trout population.

# Input
# The first line contains N,M,K,U separated by spaces. That is, the number of points along the river, the number of initially known trout, the number of events to process, and whether new trout may be discovered.

# The next N−1 lines each contain three space separated integers ai, bi and wi which indicate that the river flows from point ai to point bi and is wi metres long.

# The next M lines each contain two space separated integers, Li and Si which is the initial location and the maximum swimming distance of each trout known at the start of surveying.

# The final K lines will each contain one of two events, marked D or Q:

# Q q indicating a query for the maximum number of trout at point q.
# D x y indicating a discovery of a new trout at point x with maximum swimming distance of y metres.
# Output
# Output one line per event of type Q, with the maximum number of trout that could be found at point q based on the trout initially given and any trout discovered before.

# Constraints
# 2≤N≤100,000
# 1≤M,K,≤100,000
# 0≤ai,bi<N and 1≤wi≤10,000 for all 0≤i<N−1
# 0≤Li<N and 0≤Si≤109 for all 0≤i<M
# U=0 or U=1, and when U=0 there will only be Q type events.
# For all events 0≤q,x<N and 0≤y≤109
# Subtasks
# Subtask 1 (+10%): U=0 and N,M,K≤1,000 and wi=1, ai=i, bi=i+1 for 0≤i<N−1. That is, there are also no new trout discoveries and the river flows from point 0 through to point N−1 in a line, and every segment is 1 metre long.
# Subtask 2 (+15%): N,M,K≤1,000
# Subtask 3 (+20%): U=0 and ai=i and bi=i+1 for 0≤i<N−1. That is, there are no new trout discoveries and the river flows from point 0 through to point N−1 in a line.
# Subtask 4 (+20%): ai=i and bi=i+1 for 0≤i<N−1.
# Subtask 5 (+25%): U=0
# Subtask 6 (+10%): No additional constraints.
# Sample explanation
# Sample 1
# We are given that there are 6 points along the river, 4 initially known trout, 6 events to process, and U=0 indicating that no new trout will be discovered. The first trout starts at point 5 and could swim up to 2 metres, so it could be found at points 3, 4, or 5. The second trout starts at point 3 and could swim up to 4 metres, so it could be found at points 0, 1, 2, or 3. The third trout starts at point 5 and could swim up to 4 metres, so it could be found at points 1, 2, 3, 4, or 5. The final trout starts at point 2 and could swim up to 2 metres, so it could be found at points 0, 1, or 2. This sample meets the constraints of all subtasks.

# Sample 2
# This sample meets the constraints of subtasks 2, 5, and 6.

# Sample 3
# This sample meets the constraints of subtasks 2 and 6.

# Note
# If you are using Python, select Python 3.6 (PyPy 7.3) when submitting. Otherwise, your solution may not pass the time limit even if it is maximally efficient.

# THE RIVER IS A TREE

N = int(input())
M, K = map(int, input())
