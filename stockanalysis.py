import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, Checkbutton, IntVar

def plot_stock_data():
    stock_symbol = stock_symbol_entry.get()
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()

    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

    stock_data['MA50'] = stock_data['Close'].rolling(window=50).mean()
    stock_data['MA200'] = stock_data['Close'].rolling(window=200).mean()
    
    if show_rsi.get():
        stock_data['RSI'] = calculate_rsi(stock_data['Close'])
    
    if show_macd.get():
        stock_data['MACD'] = calculate_macd(stock_data['Close'])

    plt.figure(figsize=(12, 8))
    plt.title(f'{stock_symbol} Stock Analysis')
    plt.subplot(2, 1, 1)
    plt.plot(stock_data.index, stock_data['Close'], label='Stock Price')
    plt.plot(stock_data.index, stock_data['MA50'], label='50-day MA')
    plt.plot(stock_data.index, stock_data['MA200'], label='200-day MA')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()

    if show_rsi.get():
        plt.subplot(2, 1, 2)
        plt.plot(stock_data.index, stock_data['RSI'], label='RSI')
        plt.xlabel('Date')
        plt.ylabel('RSI')
        plt.legend()

    if show_macd.get():
        plt.subplot(2, 1, 2 if show_rsi.get() else 1)
        plt.plot(stock_data.index, stock_data['MACD'], label='MACD')
        plt.xlabel('Date')
        plt.ylabel('MACD')
        plt.legend()

    plt.tight_layout()
    plt.show()

def calculate_rsi(close_prices, window=14):
    # Calculate Relative Strength Index (RSI)
    diff = close_prices.diff()
    gain = diff.where(diff > 0, 0)
    loss = -diff.where(diff < 0, 0)
    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_macd(close_prices, short_window=12, long_window=26, signal_window=9):
    # Calculate Moving Average Convergence Divergence (MACD)
    short_ema = close_prices.ewm(span=short_window, min_periods=1, adjust=False).mean()
    long_ema = close_prices.ewm(span=long_window, min_periods=1, adjust=False).mean()
    macd = short_ema - long_ema
    signal_line = macd.ewm(span=signal_window, min_periods=1, adjust=False).mean()
    return macd - signal_line

# Create a more advanced UI window
window = Tk()
window.title('Advanced Stock Analysis and Visualization')

Label(window, text='Stock Symbol:').pack()
stock_symbol_entry = Entry(window)
stock_symbol_entry.pack()

Label(window, text='Start Date (YYYY-MM-DD):').pack()
start_date_entry = Entry(window)
start_date_entry.pack()

Label(window, text='End Date (YYYY-MM-DD):').pack()
end_date_entry = Entry(window)
end_date_entry.pack()

# Add checkboxes for technical indicators
show_rsi = IntVar()
rsi_checkbox = Checkbutton(window, text='Show RSI', variable=show_rsi)
rsi_checkbox.pack()

show_macd = IntVar()
macd_checkbox = Checkbutton(window, text='Show MACD', variable=show_macd)
macd_checkbox.pack()

plot_button = Button(window, text='Plot', command=plot_stock_data)
plot_button.pack()

window.mainloop()
