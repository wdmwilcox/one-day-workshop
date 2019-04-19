EXCHANGE_RATE = 5.29

def main():
    us_dollars = input("Enter the amount of U.S. money in dollars: ")
    float_us_dollars = float(us_dollars)
    lira = float_us_dollars * EXCHANGE_RATE
    print("You have " + str(lira) + " to spend in Turkey!")

main()