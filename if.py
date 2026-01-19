# 1) write a program to convert 24 hours time into 12 hours format time and display it with AM PM message. 

def convert_24_to_12(hour):
    if hour < 0 or hour > 23:
        return "invalid input"
    elif hour == 0:
        return "12 AM"
    elif hour < 12:
        return f"{hour} AM"
    elif hour == 12:
        return "12 PM"
    else:
        return f"{hour - 12} PM"

while True:
    user_input = input("Enter hours (0–23) or type exit: ")

    if user_input.lower() == "exit":
        break

    hour = int(user_input)
    print("output:", convert_24_to_12(hour))




