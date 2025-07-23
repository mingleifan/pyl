import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd
import matplotlib.font_manager

time_k = 365

# 查找支持中文的字体
fonts = sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])
chinese_fonts = [f for f in fonts if 'Sim' in f or 'Hei' in f or 'Ping' in f or 'Microsoft' in f or 'ST' in f]
print('chinese_fonts: ', chinese_fonts)

# 设置中文字体（解决中文显示问题）
plt.rcParams['font.sans-serif'] = ['SimSong']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 读取 Excel 数据
df = pd.read_excel("./k/600111_daily_20250723.xlsx")

# 转换日期格式并设置为索引
df['trade_date'] = pd.to_datetime(df['trade_date'], format='%Y%m%d')
df.set_index('trade_date', inplace=True)

# 按日期排序
df = df.sort_index()

# 取最近 30 天的数据
end_date = df.index.max()
start_date = end_date - pd.Timedelta(days=time_k)
df_recent = df[(df.index >= start_date) & (df.index <= end_date)]

# 重命名列名
df_recent = df_recent.rename(columns={
    'open': 'Open',
    'high': 'High',
    'low': 'Low',
    'close': 'Close',
    'vol': 'Volume'
})

# 添加均线
df_recent['MA5'] = df_recent['Close'].rolling(window=5).mean()
df_recent['MA10'] = df_recent['Close'].rolling(window=10).mean()
df_recent['MA20'] = df_recent['Close'].rolling(window=20).mean()

# 绘图
apds = [
    mpf.make_addplot(df_recent['MA5'], color='blue', label='5日均线'),
    mpf.make_addplot(df_recent['MA10'], color='orange', label='10日均线'),
    mpf.make_addplot(df_recent['MA20'], color='orange', label='20日均线'),
]

mpf.plot(df_recent,
         type='candle',
         style='yahoo',
         title='600111.SH 最近%s天K线走势' % time_k,
         ylabel='价格',
         addplot=apds,
         volume=True,
         volume_panel=1,
         panel_ratios=(4, 1),
         figratio=(16, 9),
         figscale=1.2,
         datetime_format='%m-%d',
         xrotation=45,
         )

plt.show()
