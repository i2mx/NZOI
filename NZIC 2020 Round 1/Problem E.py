N = int(input())
trail_ratings = list(map(int, input().split()))
ratings = []

S = sum(trail_ratings)

trail_one = sum([(N-i) * trail_rating for i, trail_rating in enumerate(trail_ratings)])
ratings.append(trail_one)

for trail_rating in trail_ratings[::-1]:
    ratings.append(ratings[-1] - S + N*trail_rating)

print(min(min(ratings), (N+1)*S - max(ratings)))