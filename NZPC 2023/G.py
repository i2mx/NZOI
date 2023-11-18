cards = [tuple(input()) for _ in range(12)]

for i, c1 in enumerate(cards):
    for j, c2 in enumerate(cards):
        for k, c3 in enumerate(cards):
            if k > j and j > i:
                if all([len(set([c1[L], c2[L], c3[L]])) in [1,3] for L in range(4) ]):
                    print(i+1,j+1,k+1)



# def generate_new(card1, card2):

#     colors = ['R', 'G', 'B']
#     if card1[0] == card2[2]:
#         color = card1[0]
#     else: 
#         colors.remove(card1[0])
#         colors.remove(card2[0])
#         color = colors[0]

#     numbers = ['1', '2', '3']
#     if card1[2] == card2[2]:
#         number = card1[2]
#     else: 
#         numbers.remove(card1[2])
#         numbers.remove(card2[2])
#         number = numbers[0]

#     shapes = ['D', 'O', 'S']
#     if card1[1] == card2[1]:
#         shape = card1[1]
#     else: 
#         shapes.remove(card1[1])
#         shapes.remove(card2[1])
#         shape = shapes[0]

#     fills = ['F', 'S', 'E']
#     if card1[3] == card2[3]:
#         fill = card1[3]
#     else: 
#         fills.remove(card1[3])
#         fills.remove(card2[3])
#         fill = fills[0]

#     return(color, shape, number , fill)

# print(generate_new(("R", "D", "1", "F"),("G", "O", "2", "S")))

# for i, card1 in enumerate(cards):
#     for j, card2 in enumerate(cards):
#         if i == j:
#             continue
#         new_card = generate_new(card2, card1)
#         if new_card in cards:
#             print(i,j, cards.index(new_card))