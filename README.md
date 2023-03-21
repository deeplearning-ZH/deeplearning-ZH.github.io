# InSAR对流层延迟线性改正方法python实现
## 1.说明：为什么我要写这个博客或是分享这个代码呢。原因有二。
### 首先，分享自己在学习期间学到的东西。自己深知这个摸索过程的困难。
### 其次，锻炼自己的表达能力

## 2.linear_correction为主程序，实现InSAR对流层延迟改正（垂直分层对流层延迟改正），read_data为数据读取代码（我这里使用的数据是sarscape生成的数据，各类数据其实都一样）
## 3.注意：行列号一定要对应正确，否则导致数据读取失败。如果行列号写反了，可以交换一下。在linear_correction中有经纬度的读取，可以不用管，这里我是为了后续的处理。数据的路径要正确，相对路径，绝对路径需要正确。

## 4.注：代码有什么问题，或是有优化的地方请大家直接指出，接受建议，感谢！
## ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## InSAR delayed linear correction method for troposphere python implementation
## 1. Description: Why I want to write this blog or share this code. There are two reasons.
### First, to share what I have learned during my study. I know how difficult it is to figure out this process.
### Secondly, to exercise my expression skills

## 2. linear_correction is the main program to achieve InSAR delayed correction of troposphere (vertical stratification of troposphere delayed correction), read_data is the data reading code (I use the data here is sarscape generated data, all kinds of data are actually the same)
## 3. Note: the row number must correspond to the correct, otherwise it leads to data reading failure. If the row number is written backwards, you can swap it. In linear_correction there is the reading of latitude and longitude, can be ignored, here I am for the subsequent processing. The path of data should be correct, relative path, absolute path need to be correct.

## 4. Note: What is wrong with the code, or there are optimizations please point out directly, accept suggestions, thanks!

