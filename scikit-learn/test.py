import pandas as pd
import matplotlib.pyplot as plt

from collections import OrderedDict

examDict = {
    '学习时间': [0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00, 3.25, 3.50, 3.75, 4.00, 4.25, 4.50,
                 4.75, 5.00],
    '分数': [10, 22, 13, 43, 20, 22, 33, 50, 62, 48, 55, 75, 62, 73, 81, 64, 82, 90, 93]
}

examOrderDict = OrderedDict(examDict)
examDf = pd.DataFrame(examOrderDict)

exam_X = examDf.loc[:, '学习时间']
exam_y = examDf.loc[:, '分数']

print(examDf.head())

# 散点图 scatter， 其中习惯用大写X表示特征，小写y表示标签
plt.scatter(exam_X, exam_y, color='b', label='exam data')
# 然后在lable中展示，增加散点图标签
plt.xlabel('Hours')
plt.ylabel('Score')

# 显示散点图
plt.show()
