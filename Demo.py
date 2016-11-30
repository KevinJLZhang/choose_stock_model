import tushare as ts
import pandas


#print(ts.__version__)

#***********************************************************
#about quote
#***********************************************************
#Demo of inferface get_k_data
#获取历史数据--局部
#jfkj = ts.get_k_data('002202', start='2016-11-29', end='2016-11-30', ktype='D', autype='qfq', index=False)
#print(jfkj)
#print("-------------------------------------------------")
#获取历史行情--全
#jfkj = ts.get_hist_data('002202', start='2016-11-27', end='2016-11-28')
#print(jfkj)
#print("-------------------------------------------------")
#获取实时行情
#jfkj = ts.get_today_all()
#print(jfkj)
#获取历史分笔
#jfkj = ts.get_tick_data('002202', date='2016-11-30')
#获取实时分笔,请求多个股票时，使用['','',''# ]
#jfkj = ts.get_realtime_quotes('002202')
#sh = ts.get_realtime_quotes('sh')
#大盘指数
#df = ts.get_index()

#*********************************************************
#
#*********************************************************
print(df)