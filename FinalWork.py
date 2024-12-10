from tkinter import *
from tkinter import messagebox as mb
import requests
from tkinter import ttk

 # Получаем полное название криптовалюты из словаря и обновляем метку
def update_b_label(event):
    code=b_combobox.get()
    name=b_cur[code]
    b_label.config(text=name)

 # Получаем полное название целевой валюты из словаря и обновляем метку
def update_t_label(event):
    code=t_combobox.get()
    name = t_cur[code]
    t_label.config(text=name)

 # Словарь кодов криптовалют и их полных названий
b_cur = {
        "bitcoin":"BTC (Bitcoin)",
        "ethereum":"ЕТН (Ethereum)",
        "tether":"USDT (Tether)",
        "solana":"SOL (Solana)",
        "ripple":"XRP (Ripple)",
        "binancecoin":"BNB (Binance Coin)",
        "dogecoin":"DOGE (Dogecoin)",
        "cardano":"ADA (Cardano)",
        "litecoin":" LTC (Litecoin)",
        "chainlink":"LINK (Chainlink)"
}
 # Словарь кодов валют и их полных названий
t_cur = {
        "USD": "USD (Американский доллар)",
        "RUB": "RUB (Российский рубль)",
        "EUR": "EUR (Евро)",
        "CNY": "CNY (Китайский юань)",
        "JPY": "JPY (Японская йена)"
}


def exchange():
    b_code = b_combobox.get().lower()
    t_code = t_combobox.get().lower()
    if t_code and b_code:
        try:
            # Обработка запроса на сайт и преобразование его в формат json
            response=requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={b_code}&vs_currencies={t_code}")
            response.raise_for_status()
            data=response.json()
            if b_code in data:
                exchange_rate=data[b_code][t_code]
                t_name = t_cur[t_code.upper()]
                b_name = b_cur[b_code]
                # Вывод и форматирование метки с полученным результатом
                i_label.config(text=f"Текущий курс:\n {exchange_rate:_} {t_name} за 1 {b_name}".
                               format(exchange_rate).replace('_', ' '),
                               background="#B3E5FC", foreground="#01579B")
            # Обработка возможных ошибок
            else:
                mb.showerror("Ошибка", f"Криптовалюта {b_code} не найдена")
        except requests.RequestException as err:
            mb.showerror("Ошибка", f"Произошла ошибка запроса {err}")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка {e}")
    else:
        mb.showwarning("Внимание!", "Вы не ввели код валюты")
# Создание графического интерфейса
window = Tk()
window.title("Курсы обмена криптовалют")
window.geometry("400x400")

Label(text="Выберите криптовалюту").pack(padx=10,pady=10)
b_combobox=ttk.Combobox(values=list(b_cur.keys()))
b_combobox.pack(padx=10,pady=10)
b_combobox.bind("<<ComboboxSelected>>",update_b_label)
b_label=ttk.Label()
b_label.pack(padx=5,pady=5)

Label(text="Выберите целевую валюту").pack(padx=10,pady=10)
t_combobox=ttk.Combobox(values=list(t_cur.keys()))
t_combobox.pack(padx=10,pady=10)
t_combobox.bind("<<ComboboxSelected>>",update_t_label)
t_label=ttk.Label()
t_label.pack()

Button(text="Получить курс обмена", command=exchange).pack(padx=30,pady=30)

i_label=ttk.Label()
i_label.pack(padx=10,pady=10)

window.mainloop()