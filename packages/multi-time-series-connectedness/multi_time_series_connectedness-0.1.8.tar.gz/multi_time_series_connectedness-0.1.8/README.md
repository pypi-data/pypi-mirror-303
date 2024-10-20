## Project title
Multi Time Series Connectedness

## Motivation
This project is motivated by Financial and Macroeconomics Connectedness created by Diebold and Ylimaz. I want to use this algorithm not only in finance and macroeconomics area but other area, so I start to build this project.

## Installation
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Feature & Example Code
* calculate volatility
  ```
  python3 volatilities.py --path docs/market_prices --start_at 2024-09-06T00:00:00+01:00 --end_at 2024-09-06T22:27:00+01:00
  ```
* calculate connectedness of all volatility
  ```
  python3 conn.py
  ```
* calculate rolling connectedness
  ```
  python3 rolling_connectedness.py
  ```

## How to use?
* Put a folder with multiple Panel data into docs folder
* Run the commands in feature section

## Credits
http://financialconnectedness.org/

## License
MIT License