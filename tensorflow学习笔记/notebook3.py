from sklearn import datasets
import tensorflow as tf
import numpy as np
# lris数据集提供了150组鸢尾花的数据集
# 每组包括花萼长宽、花瓣长宽4个输入特征
# 同时给出了对应的鸢尾花类别，0：狗尾草鸢尾 1：杂色鸢尾 2：弗吉尼亚鸢尾
# 通过sklearn datasets可下载数据集
from sklearn.datasets import load_iris
x_data=datasets.load_iris().data# 返回所有输入特征
y_data=datasets.load_iris().target# 返回所有类别
# 详细代码见class1\p43
# 在终端TF2.1环境中输入pip install sklearn后可得sklearn数据集
# 同样的输入pip install pandas后安装pandas包
# pandas在p43中用于列对齐
# 鸢尾花数据集训练步骤
# 数据的读入
x_data=datasets.load_iris().data# 返回输入特征
y_data=datasets.load_iris().target# 返回标签
# 数据集乱序
np.random.seed(116)# seed的值相同，这样保证了随机后原特征和原标签对应
np.random.shuffle(x_data)
np.random.seed(116)
np.random.shuffle(y_data)
tf.random.set_seed(116)# 不明意义
# 分割训练集和测试集
x_train=x_data[:-30]# 在150个数据中取前120个数据作为训练集
y_train=y_data[:-30]
x_test=x_data[-30:]# 取后30个数据作为测试集
y_test=y_data[-30:]
# 配成[特征,标签]对，以batch为单位喂入
train_db=tf.data.Dataset.from_tensor_slices((x_train,y_train)).batch(32)
test_db=tf.data.Dataset.from_tensor_slices((x_test,y_test)).batch(32)
# 定义可训练参数
w1=tf.Variable(tf.random.truncated_normal([4,3],stddev=0.1,seed=1))# 均值默认为0，seed=1保证了每次运行结果一样
b1=tf.Variable(tf.random.truncated_normal([3],stddev=0.1,seed=1))
# with结构更新参数(略)
# 前向传播检测准确度(略)
# 绘制曲线(可略)
# 详情见class1\P45