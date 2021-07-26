import tensorflow as tf
import numpy as np
#求梯度
with tf.GradientTape() as tape:
    a=tf.Variable(tf.constant([[1.0,2.0],[3.0,4.0]]))
    loss=tf.pow(a,2)
grad=tape.gradient(loss,a)
print(grad)
#枚举函数enumerate
b=['one','two','three']
for i,element in enumerate(b):
    print(i,element)
#独热码:在分类:(0猫 1狗 2羊)中，标签1对应独热码为(0. 1. 0.)
classes=3
labels=tf.constant([1,0,2])
output=tf.one_hot(labels,depth=classes)
print(output)
#使前向传播的值符合概率分布，公式:e^yi/sumj(e^yj)，对应tf.nn.softmax(y)函数
c=tf.constant([1.01,2.01,-0.66])
d=tf.nn.softmax(c)
print(d)
#可训练变量的自更新
e=tf.Variable(4)
e.assign_sub(1)
print(e)
#返回某一数据的维度方向的最大值的索引
g=np.array([[1,2,3],[2,3,4],[5,4,3],[8,7,2]])
print(g)
print(tf.argmax(g,axis=0))
print(tf.argmax(g,axis=1))