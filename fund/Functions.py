import pandas as pd
import matplotlib.pyplot as plt

# 绘制策略曲线
def draw_equity_curve_mat(df):
    """
    绘制策略曲线
    :param df: 包含净值数据的df
    :return:
    """
    # 复制数据
    draw_df = df.copy()
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.figure()
    # 绘制左轴数据
    plt.plot(draw_df['交易日期'], draw_df['累积净值'], linewidth=2, label='累积净值')
    # 设置坐标轴信息等
    plt.ylabel('净值')
    plt.show()

def strategy_evaluate(select_stock):
    """
    :param select_stock: 每周期选出的股票
    :return:
    """
    results = pd.DataFrame()
    # ===计算累积净值
    results.loc[0, '累积净值'] = round(select_stock['累积净值'].iloc[-1], 2)
    # ===计算年化收益
    annual_return = (select_stock['累积净值'].iloc[-1]) ** (
            '1 days 00:00:00' / (select_stock['交易日期'].iloc[-1] - select_stock['交易日期'].iloc[0]) * 365) - 1
    results.loc[0, '年化收益'] = str(round(annual_return * 100, 2)) + '%'

    return results.T