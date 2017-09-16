## cryptocurrency-price-alert

I use looking for a tool in order to inform me regularly about the prices of three currencies BTC ETH and LTC but in euro instead of dollars, so I changed all the variables accordingly from the original script.
I found out bofinbabu/cryptocurrency-price-alert project and forked it.
This python script is doing Ubuntu desktop notification alerts for Bitcoin, Etherium and Litecoin prices.

### Requirements
So if you are not an Ubuntu user it means that you need to install this OS and the following packages.
1. `requests` (pip install -U requests)
2. `schedule` (pip install -U schedule)
Once done unzip cryptocurrency-price-alert.
Then make the python script executable
Then use the shell to fire the Python script.

### Usage
Change the global variable `ALERT_INTERVAL` to a desired value (default 30 minutes) and run `price-alert.py`

### Thanks
Thanks to bofinbabu. Your script did exactly what I was looking for
