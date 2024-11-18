# Stock Alert Script

This is a Python script that monitors stock prices and sends an SMS alert if the stock price changes by a defined percentage threshold.

## Features
- Monitors stock prices for multiple tickers.
- Sends SMS alerts when the price change exceeds a specified threshold.
- Built with Yahoo Finance for stock data and Twilio for SMS notifications.

## Requirements

- yfinance library for stock data
- twilio API for sending SMS
- time
- datetime


## Create Twilio Account 

- Visit Twilio website for creating account.
- Select SMS option under Notification.
- Get your required twilio credentials as follows 
  1.twilio_account_sid = # Updated Account SID
  2.twilio_auth_token =  # Updated Auth Token
  3.from_phone_number = # Updated Twilio phone number
  4.to_phone_number = # your Registered Phone Number with twilio (Regiter with # The recipient phone number)
  

## How to Run

1. Install dependencies:
   pip install yfinance   
   pip install twilio

2. Ticker 
  -A ticker is a unique symbol used to identify a specific stock or financial asset on a stock exchange.
  -Replace the ticker with the company you desire to know the stock alert and also replace the threshold value of    your requirement.

3.Run The Script
