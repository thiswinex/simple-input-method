# simple-input-method
base on bigram model

## Dependency
推荐使用python3。

## Usage

直接测试：

```
python main.py
```

用data.py来解析任何自定义的语料库，文件路径在代码里改（懒得重写了）：

```
python data.py
```

## About Model

语言模型是用来求解某个句子（序列）的概率：

![1](http://latex.codecogs.com/svg.latex?p(w_1,w_2,\cdots,w_n))



用条件概率改写：
![2](http://latex.codecogs.com/svg.latex?p(w_1,w_2,\cdots,w_n)=p(w_1)\cdot{}p(w_2|w_1)\cdot{}p(w_3|w_1,w_2)\cdots{}p(w_n|w_1,\cdots,w_{n-1}))

马尔科夫假设认为语言序列是马尔科夫链，满足一定的无记忆性，即一个词出现的概率只与其之前的m-1个词有关。若m=2即为二元模型（Bigram model）：
![3](http://latex.codecogs.com/svg.latex?p(w_1,w_2,\cdots,w_n)=p(w_1)\cdot{}p(w_2|w_1)\cdot{}p(w_3|w_2)\cdots{}p(w_n|w_{n-1}))

从语料库中可以求得所有的条件概率 p(x|y) 以及概率 p(x) ，解析后记录在文件内，这些文件即为我们的模型。只要使用模型输出最大概率的序列即可。我使用的是简单的贪心，可以使用DP继续改写此方法。
