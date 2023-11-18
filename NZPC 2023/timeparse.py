minutes = 2
seconds = 0

s = f'Longest through time was {minutes} {"minute" if minutes == 1 else "minutes"} and {seconds} {"second" if seconds == 1 else "seconds"}.'
print(s)
# if minutes == 1:
#     minute_text = "1 minute"
# elif minutes == 0:
#     minute_text = ""
# else:
#     minute_text = f"{minutes} minutes"

# if seconds == 1:
#     second_text = "1 second."
# # elif seconds == 0:
#     # second_text = "."
# else: 
#     second_text = f"{seconds} seconds."

# print("Longest through time was " + minute_text + ("" if minutes == 0 else " and ") + second_text)