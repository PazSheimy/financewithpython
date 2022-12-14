import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datatime(2000,1,1)
end = dt.datatime(2016,12,31)

df = web.DataReader('TSLA', 'yahoo', start, end)
print(df.head()) #gets the frist 5 rows printed
print(df.tail) #gets the last 5 printed
