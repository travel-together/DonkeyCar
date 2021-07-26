import tensorflow as tf
import numpy as np
# tf.where(条件,A,B)，条件为真返回A，为假返回B
a=tf.constant([1,2,3,1,1])
b=tf.constant([0,1,3,4,5])
c=tf.where(tf.greater(a,b),a,b)# greater按位比ab较大者的位置，返回1、0
print(c.numpy())
# 返回0-1之间的随机数
rdm = np.random.RandomState(seed=1)# 设置种子
d = rdm.rand()# 返回随机标量
e = rdm.rand(2, 3)# 返回2*3的随机矩阵
print("d:", d)
print("e:", e)
# 数组的纵向叠加
f = np.array([1, 2, 3])
g = np.array([4, 5, 6])
h = np.vstack((f, g))
print("h:\n", h)
# 生成等间隔数值点，[起始:终止:步长,...]，为前闭后开区间，输出维度相同，第一个数按0维增长，第二个数按1维增长
i, j = np.mgrid[1:3:1, 2:4:0.5]
print(i)
print(j)
# .ravel()使数降至1维(拉直)，.c_()使一数组相同位置配对
k = np.c_[i.ravel(), j.ravel()]
print("j.ravel():\n", i.ravel())
print("i.ravel():\n", j.ravel())
print('grid:\n', k)
# 神经网络复杂度
# 输入层和输出层之间的加隐藏层
# 设第i层的结点数为ai
# 空间复杂度:
# 层数=输出层+隐藏层
# 总参数=总w+总b=a0*a1+a1*a2+...+a1+a2+...
# 时间复杂度:
# 乘加运算=a0*a1+a1*a2+...
# 学习率设置
# lr过大则不收敛，过小则收敛过慢
# 可以设置较大学习率，再逐渐减小
# 指数衰减学习率=初始学习率*学习率衰减率^(当前轮数/多少轮衰减一次)
# 激活函数
# Sigmoid函数:f(x)=1/(1-e^-x),tf.nn.sigmoid(x)
# Tanh函数:f(x)=(1-e^-2x)/(1+e^-2x),tf.math.tanh(x)
# Relu函数:f(x)=max(0,x),tf.nn.relu(x)
# Lealy Relu函数:f(x)=max(ax,x),tf.nn.leaky_relu(x)
# 初学者建议
# 首选relu函数
# 学习率设为较小值
# 输入特征标准化:使输入特征为以0为均值，以1为标准差的正态分布
# 初始参数中心化:让随机生成的参数满足以0为均值，sqrt(2/当前层输入特征个数)为标准差的正太分布
# 损失函数
# 均方误差:MSE(y_,y)=mean((y-y_)^2),tf.reduce_mean(tf.square(y_-y))
# 自定义，例:预测商品销量，预测多了，损失成本;预测少了，损失利润
# loss=sum(f(y_,y))
# f(y_,y)=|PROFIT*(y_-y),y<y_
#         |COST*(y-y_),y>=y_
# tf.reduce_sum(tf.where(tf.greater(y,y_),COST(y-y_),PROFIT(y_-y)))
# 交叉熵:H(y_,y)=-sum(y_*lny)
# tf.losses.categorical_crossentropy(y_,y)
# 上式y为独热码，y_为符合概率的值，下式能计算不符合概率的y_
# tf.nn.softmax_cross_entropy_with_logits(y_,y)
# 正则化缓解过拟合
# loss=loss(y_,y)+REGULARIZER*loss(w)
# REGULARIZER给出loss(w)在总loss中的比例
# loss的选择通常有两种:loss_l1=sum(|wi|);loss_l2=sum(wi^2)
# l1正则化大概率使一些参数变为0，l2正则化大概率使一些参数变为很小的值