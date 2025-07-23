import tushare as ts

pro = ts.pro_api('6db51e15d818a75903d5783dce689ced2140014188e7feb21c5c4f04')

df = pro.daily(ts_code='600111.SH', start_date='20200101', end_date='20250723')
# df = pro.daily(trade_date='20250723')
df.to_excel("./600111_daily_20250723.xlsx", index=False)
