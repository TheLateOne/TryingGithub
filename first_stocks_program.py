from yahoo_finance import Share
import time
import datetime

Stock_Ticker = "CHRT.L"
x = Share(Stock_Ticker)
start = datetime.time(8, 00, 00)
end = datetime.time(16, 30, 00)
file = "Cohort_PLC.txt"


def get_market_times(Market_Name):
    # Cleaner to make this a function - add any relevant market time zones here (In UTC). Check wikipedia for list
    if Market_Name.lower() == "lse":
        start2 = datetime.time(8, 00, 00)
        end2 = datetime.time(16, 30, 00)
    elif Market_Name.lower() == "nyse":
        start2 = datetime.time(14, 30, 00)
        end2 = datetime.time(21, 00, 00)
    elif Market_Name.lower() == "tse":
        start2 = datetime.time(00, 00, 00)
        end2 = datetime.time(6, 00, 00)
    elif Market_Name.lower() == "krx":
        start2 = datetime.time(00, 00, 00)
        end2 = datetime.time(6, 00, 00)
    else:
        return "Market_Error: Market unsupported, enter times in code"
    return start2, end2


def inter_minute_data_get(Ticker, Market, Target_File):
    start, end = get_market_times(Market)
    while True:
        prices = open(Target_File, "a")
        # concerning this "open" "close" within the loop; this means that regardless of how the program exits we still
        # write to the file (as opposed to what we were doing which was saving only temporarily
        t1 = datetime.datetime.utcnow().time()
        if not start <= t1 <= end:
            # This finds the current time and waits until the market should next open (does not account for weekends)
            p = datetime.datetime.utcnow()
            y = p.replace(hour=start.hour, minute=start.minute, second=start.second)
            delta_t = y - p
            if "-1" in str(delta_t):
                # in case of the "start" time being before the current time we shift to the next day
                y = p.replace(day=p.day + 1, hour=start.hour, minute=start.minute, second=start.second)
                delta_t = y - p
            h, m, s = str(delta_t).split(":")
            new_delta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s)).total_seconds()
            time.sleep(new_delta)
        prices.write("Time: {}Ticker: {} Price: {} \n".format(Share.get_trade_datetime(x).strip("UTC+0000"), Ticker,
                                                              Share.get_price(x)))
        time.sleep(3)
        prices.close()


inter_minute_data_get(Stock_Ticker, "nyse", file)