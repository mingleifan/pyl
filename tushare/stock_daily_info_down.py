import tushare as ts

pro = ts.pro_api('')

df = pro.daily(ts_code='600111.SH', start_date='20200101', end_date='20250723')
# df = pro.daily(trade_date='20250723')
df.to_excel("./600111_daily_20250723.xlsx", index=False)
