stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300
}

total_value = 0

while True:
    stock_name = input("Enter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stocks:
        quantity = int(input("Enter quantity: "))
        total_value += stocks[stock_name] * quantity
    else:
        print("Stock not found!")

print("Total Investment Value: $", total_value)

file = open("portfolio.txt", "w")
file.write("Total Investment Value: $" + str(total_value))
file.close()
