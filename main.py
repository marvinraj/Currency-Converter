import requests

# display title & instruction
def intro():
    print("\n===================")
    print("CURRENCY CONVERTER")
    print("===================\n")

# requests for data and receives response, then call display_currecy()
def get_currency(payload, headers, from_curr, to_curr, amount):
    url = f"https://api.apilayer.com/fixer/convert?to={to_curr}&from={from_curr}&amount={amount}"
    response = requests.request("GET", url, headers=headers, data = payload)

    status_code = response.status_code
    if status_code == 200:
        data = response.json()
        display_currency(data)
    else:
        print("Invalid currency detected.")

# chooses what to display from the entire dataset
def display_currency(data):
    curr_from = data["query"]["from"]
    curr_to = data["query"]["to"]
    exchange_rate = data["info"]["rate"]
    amount_input = data["query"]["amount"]
    amount_output = data["result"]

    print(f"\n{amount_input} {curr_from} = {amount_output} {curr_to}")
    print("exchange rate: ", exchange_rate)

def main():
    intro()

    payload = {}
    headers= {
    "apikey": "KzZhNBVZjjfCndOUdbjTxhKu5FgAI9rp"
    }

    from_curr = input("1. Currency to convert from (myr,usd,etc): ")
    to_curr = input("2. Currency to convert to (myr,usd,etc): ")
    amount = input("3. Enter amount: ")

    get_currency(payload, headers, from_curr, to_curr, amount)


if __name__ == "__main__":
    main()