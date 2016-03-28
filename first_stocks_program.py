from yahoo_finance import Share
import time
import datetime

Ticker = "TSLA"
x = Share(Ticker)
start = datetime.time(14, 30, 00)
end = datetime.time(21, 00, 00)

with open("prices.txt", "a") as prices:
    while True:
        t1 = datetime.datetime.now().time()
        prices.write("Time: {}Ticker: {} Price: {} \n".format(Share.get_trade_datetime(x).strip("UTC+0000"), Ticker,
                                                              Share.get_price(x)))
        time.sleep(10)
        if not start <= t1 <= end:
            p = datetime.datetime.today()
            y = p.replace(hour=start.hour, minute=start.minute, second=start.second)
            delta_t = y - p
            h, m, s = str(delta_t).split(":")
            new_delta = int(datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s)).total_seconds())
            time.sleep(new_delta)
