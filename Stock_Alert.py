import yfinance as yf
from twilio.rest import Client
import time

# Define your Twilio credentials and phone numbers
twilio_account_sid = '[Your twilio account_Sid]'  # Updated Account SID
twilio_auth_token = '[Your twilio auth_token]'  # Updated Auth Token
from_phone_number = '[Twilio Phone No]'  # Updated Twilio phone number
to_phone_number = '[Recipient Phone No]'  # The recipient phone number

# Define the stock tickers and percentage change threshold
tickers = ['AMZN']  # List of tickers to monitor
percentage_threshold = 2.0  # Set your desired percentage threshold

# Create a Twilio client
client = Client(twilio_account_sid, twilio_auth_token)

# Flag to track if an alert has already been sent
alert_sent = False

while True:
    if not alert_sent:  # Check if an alert has already been sent
        for ticker in tickers:
            # Get the stock information for each ticker
            stock = yf.Ticker(ticker)
            stock_info = stock.info

            # Get the current market price and previous close price
            current_price = stock_info.get('regularMarketPrice')  # Fallback approach
            if current_price is None:
                current_price = stock_info.get('ask', 'N/A')

            if current_price == 'N/A':
                print(f"Could not retrieve price for {ticker}")
                continue
            
            previous_close_price = stock_info.get('previousClose', 0)

            # Calculate the percentage change
            percentage_change = ((current_price - previous_close_price) / previous_close_price) * 100 if previous_close_price else 0

            # Check if the percentage change is above the threshold
            if abs(percentage_change) >= percentage_threshold:
                # Send an SMS alert
                message = client.messages.create(
                    to=to_phone_number,
                    from_=from_phone_number,
                    body=f'{ticker} stock price has changed by {percentage_change:.2f}%. Current price: {current_price}')
                print(f"SMS alert sent for {ticker} with SID: {message.sid}")
                alert_sent = True  # Set flag to True after sending the alert
                break  # Exit the loop after sending one alert

    # Wait for a specified interval before checking again (e.g., 60 seconds)
    time.sleep(60)
