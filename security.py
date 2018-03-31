import pandas_datareader as web
import pandas as pd

class SecurityData(object):
    
    def __init__(self, download_path = "data/", \
                 data_source = "quandl", start_date = '2005-01-01', \
                 end_date = '2018-03-31', verbose = False):
        
        self.data_source = data_source
        self.start_date = start_date
        self.end_date = end_date
        self.download_path = download_path
        self.verbose= verbose
        
    def fetch_timeseries_data(self, ticker_universe):
        
        """download the time series data from external source"""
        
        "loop for downloading the data"
        for i in range(0,len(ticker_universe)):
            ticker = ticker_universe.iloc[i,0].strip()
            
            "loop to try 5 times for downloading the data"
            retry_flag = 0
            
            while (retry_flag < 5):
                try:
                    data = web.DataReader(ticker, self.data_source, self.start_date, self.end_date)
                    data = data.fillna(method="ffill")
                    data = data.fillna(method="backfill")                    
                    data.to_csv(self.download_path+ticker+".csv")
                    if (self.verbose):
                        print(f"try {i}: flag : {retry_flag} : ticker : {ticker}")
                    break
                except Exception as e:
                    if (self.verbose):
                        print(f"except {i}: flag : {retry_flag} : ticker : {ticker}")
                    retry_flag = retry_flag +1
                    if (retry_flag  > 4):
                        if (self.verbose):
                            print (str(e))
                        continue
    """end of function"""
        
if __name__ == "__main__":
    tickers = pd.read_csv("tickers.csv")
    security_data = SecurityData(verbose=True)
    security_data.fetch_timeseries_data(tickers)
    