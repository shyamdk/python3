def warmorcold(temp):
    if temp > 25:
        return "HOT"
    elif temp <= 25 and temp >=15:
        return "WARM"
    elif temp < 15:
        return "Cold"
        

user_input = float(input("Please provide the current temprature:")) 
print(warmorcold(user_input))