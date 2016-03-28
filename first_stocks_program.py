from yahoo_finance import Share
import time
import datetime

Ticker = "CHRT.L"
x = Share(Ticker)
start = datetime.time(8, 00, 00)
end = datetime.time(19, 30, 00)

with open("prices.txt", "a") as prices:
    while True:
        t1 = datetime.datetime.now().time()
        if not start <= t1 <= end:
            # This finds the current time and waits until the market should next open (does not account for weekends)
            p = datetime.datetime.today()
            y = p.replace(hour=start.hour, minute=start.minute, second=start.second)
            delta_t = y - p
            if "-1" in str(delta_t):
                y = p.replace(day=p.day + 1, hour=start.hour, minute=start.minute, second=start.second)
                delta_t = y - p
            h, m, s = str(delta_t).split(":")
            new_delta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s)).total_seconds()
            print new_delta
            time.sleep(new_delta)
        prices.write("Time: {}Ticker: {} Price: {} \n".format(Share.get_trade_datetime(x).strip("UTC+0000"), Ticker,
                                                              Share.get_price(x)))
        prices.write("ping")
        print "Ping"
        time.sleep(5)