import requests
import json
from tkinter import Tk, ttk
from tkinter import *
import winsound
from PIL import Image, ImageTk

# Colors
WHITE = "#FFFFFF"  # white
BLACK = "#333333"  # black
NAVY = "#000080"  # navy

# Create the main window
window = Tk()
window.geometry('300x300')
window.title('Converter')
window.configure(bg=WHITE)
window.resizable(height=False, width=False)

# Create frames
top_frame = Frame(window, width=300, height=70, bg=NAVY)  
top_frame.grid(row=0, column=0)

main = Frame(window, width=300, height=260, bg=WHITE)  
main.grid(row=1, column=0)

# Currency names to be used in the dropdown menus
currency_names = [
    'AED', 'ARS', 'AUD', 'BGN', 'BHD', 'BRL', 'CAD', 'CHF', 'CLP', 'CNY', 'COP',
    'CZK', 'DKK', 'EUR', 'GBP', 'HKD', 'HUF', 'IDR', 'ILS', 'INR', 'JPY', 'KRW',
    'MXN', 'MYR', 'NOK', 'NZD', 'PEN', 'PHP', 'PLN', 'RON', 'RUB', 'SAR', 'SEK',
    'SGD', 'THB', 'TRY', 'TWD', 'USD', 'ZAR'
]

# Function to convert currency
def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    # Get the selected currencies and amount
    currency_1 = combo1.get()
    currency_2 = combo2.get()
    amount = value.get()

    # Create the query string
    querystring = {"from": currency_1, "to": currency_2, "amount": amount}

    # Create the headers
    headers = {
        'x-rapidapi-host': "currency-converter18.p.rapidapi.com",
        'x-rapidapi-key': "90c59d6c9fmsh4599f814e2ffc92p17fc6djsndeaa0265ac61"
    }

    # Send the request and get the response
    response = requests.request("GET", url, headers=headers, params=querystring)

    # Parse the response
    data = json.loads(response.text)
    converted_amount = data["result"]["convertedAmount"]

    # Get the symbol for the currency
    symbol = get_currency_symbol(currency_2)

    # Format the result
    formatted = f"{symbol} {converted_amount:,.4f}"

    # Display the result
    result['text'] = formatted
    winsound.PlaySound('coin-drop-39914.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)

    print(converted_amount, formatted)

# Function to get the symbol for a currency
def get_currency_symbol(currency):
    symbols = {
        'AED': 'د.إ',
        'ARS': 'ARG$',
        'AUD': 'A$',
        'BGN': 'BGN',
        'BHD': '.د.ب',
        'BRL': 'R$',
        'CAD': 'CA $',
        'CHF': 'CHF',
        'CLP': 'CLP$',
        'CNY': '¥',
        'COP': 'COL$',
        'CZK': 'Kč',
        'DKK': 'kr',
        'EUR': '€',
        'GBP': '£',
        'HKD': 'HK$',
        'HUF': 'Ft',
        'IDR': 'Rp',
        'ILS': '₪',
        'INR': '₹',
        'JPY': '¥',
        'KRW': '₩',
        'MXN': 'MX$',
        'MYR': 'RM',
        'NOK': 'kr',
        'NZD': 'NZ$',
        'PEN': 'S/',
        'PHP': '₱',
        'PLN': 'zł',
        'RON': 'L',
        'RUB': '₽',
        'SAR': '﷼',
        'SEK': 'kr',
        'SGD': 'S$',
        'THB': '฿',
        'TRY': '₺',
        'TWD': 'NT$',
        'USD': 'US$',
        'ZAR': 'R'
    }
    return symbols.get(currency, '')

# Top frame
text_label = Label(top_frame, text="Currency Converter", font=("Arial", 12), bg=NAVY, fg=WHITE) 
text_label.pack()

# Main frame
result = Label(main, text=" ", width=16, height=2, pady=7, relief="solid", anchor=CENTER, font=('Ivy 15 bold'), bg=WHITE, fg=BLACK)
result.place(x=50, y=10)

from_label = Label(main, text="From", width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=WHITE, fg=BLACK)
from_label.place(x=48, y=90)
combo1 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo1['values'] = tuple(currency_names)
combo1.place(x=50, y=115)

to_label = Label(main, text="To", width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=WHITE, fg=BLACK)
to_label.place(x=158, y=90)
combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo2['values'] = tuple(currency_names)
combo2.place(x=160, y=115)

to_label = Label(main, text="Enter the amount", width=16, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=WHITE, fg=BLACK)
to_label.place(x=48, y=140)
value = Entry(main, width=22, justify=CENTER, font=("Ivy 12 bold"), relief=SOLID)
value.place(x=50, y=160)

button = Button(main, text="Convert", width=19, padx=5, height=1, bg=NAVY, fg=WHITE, font=("Ivy 12 bold"), command=convert)
button.place(x=50, y=210)

window.mainloop()
