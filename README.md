
## Stock Analysis and Visualization

This Python script enables the analysis and visualization of stock market data using the Yahoo Finance API and a user-friendly graphical user interface (GUI) built with the Tkinter library. The script fetches stock market data, calculates various technical indicators, and presents the data using interactive charts.

### Libraries Used

- **yfinance**: A library that provides an easy-to-use interface to fetch historical stock market data from Yahoo Finance.
- **pandas**: A data manipulation library used to store, manipulate, and analyze the fetched stock data.
- **matplotlib**: A versatile plotting library for creating static, interactive, and animated visualizations.
- **tkinter**: The standard GUI library for creating graphical user interfaces.
- **mplfinance**: A library for plotting financial data, including candlestick charts.

### Functions

1. **calculate_rsi(close_prices, window=14)**:
   Calculates the Relative Strength Index (RSI) of the provided stock's closing prices using the specified window size (default: 14 days). RSI is a momentum oscillator that measures the speed and change of price movements.
   
2. **calculate_macd(close_prices, short_window=12, long_window=26, signal_window=9)**:
   Calculates the Moving Average Convergence Divergence (MACD) of the provided stock's closing prices using the specified window sizes (short, long, and signal). MACD is a trend-following momentum indicator.
   
3. **plot_stock_data()**:
   Fetches stock market data based on user input (stock symbol, start date, and end date) using the Yahoo Finance API. It then calculates the 50-day and 200-day moving averages, RSI, and MACD of the stock's closing prices. The data is visualized in two subplots: the top subplot displays the stock price and moving averages, while the bottom subplot displays the RSI. The user can interactively select whether to show the RSI and MACD lines via checkboxes in the GUI.
   
4. **plot_advanced_stock_data(stock_symbol, start_date, end_date, show_rsi, show_macd)**:
   Similar to `plot_stock_data()`, but more advanced. Additionally, it calculates Bollinger Bands for the stock's closing prices and presents the data in a candlestick chart along with the Bollinger Bands. The Bollinger Bands show the stock's price volatility relative to the moving averages.

### Graphical User Interface (GUI)

- The GUI is built using the Tkinter library and provides an interface for the user to input the stock symbol, start date, and end date for the analysis.
- Checkboxes allow the user to decide whether to show the RSI and MACD lines in the plot.
- A "Plot" button triggers the analysis and visualization of the stock data based on the provided inputs.

### Usage

1. Make sure you have the required libraries (`yfinance`, `pandas`, `matplotlib`, `tkinter`, and `mplfinance`) installed.
2. Run the script.
3. Enter the stock symbol, start date, and end date in the GUI.
4. Optionally, select the checkboxes to display RSI and MACD.
5. Click the "Plot" button to view the analysis and visualization of the stock data.

Note: Ensure that the script is run in an environment that supports GUI interfaces, such as a standalone Python script or IDE.

