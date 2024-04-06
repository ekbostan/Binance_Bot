# Simple Binance Bot

## Overview
This repository contains a simple trading bot that explores trading opportunities on the Binance cryptocurrency exchange. The bot is designed to automate trading based on predefined strategies and perform backtesting to evaluate these strategies over historical data.

## Files Description

- `Bot.py`: The main entry point for the trading bot. It handles interactions with the Binance API for executing trades and managing orders.
- `Trader.py`: Implements the trading logic and strategy. It makes decisions based on market data and executes trades through the Binance API.
- `BackTesting.py`: Provides functionality for backtesting trading strategies with historical market data to assess their effectiveness before deploying in live markets.

## Requirements

- Python 3.x
- Binance API key and secret (for live trading)
- Additional Python packages: `binance`, `pandas`, `numpy` (see `requirements.txt` for a complete list)

## Setup

1. Clone this repository to your local machine.
2. Install the necessary Python packages:
