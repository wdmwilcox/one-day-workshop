def get_fx_rate():
    '''get user input of exchange rate from  USD to LIR'''
    exchange_rate = input("Input exchange rate for  USD to LIR: ")
    exchange_rate = float(exchange_rate)
    return exchange_rate


def get_us_amount():
    '''get user input of USD amount'''
    us_dollars = input("Enter the amount of U.S. money in dollars: ")
    us_dollars = float(us_dollars)
    return us_dollars


def convert_to_lira(us_amount, exchange_rate):
    '''oonvert usd amount to lira
    requires USD amount and exchange rate'''
    lira_amount = us_amount * exchange_rate
    return lira_amount


def main():
    exchange_rate = get_fx_rate()
    us_amount  = get_us_amount()
    lira = convert_to_lira(us_amount, exchange_rate)
    print("You have " + str(lira) + " to spend in Turkey!")


main()