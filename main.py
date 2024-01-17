import requests

def main():
    from_curr = input("enter currency from: ")
    to_curr = input("enter currency to: ")
    amount = input("enter amount: ")
    url = f"https://api.apilayer.com/fixer/convert?to={to_curr}&from={from_curr}&amount={amount}"

    payload = {}
    headers= {
    "apikey": "KzZhNBVZjjfCndOUdbjTxhKu5FgAI9rp"
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    status_code = response.status_code
    result = response.text
    print(result)

if __name__ == "__main__":
    main()