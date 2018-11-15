# 记录自己用Python完成编写JVM的过程

项目完全参考张秀宏大神的《自己动手写Java虚拟机》代码结构，在此向本书作者表示感谢。

## 运行环境 ##
Python 版本：3.7.2  
PyCharm 版本：PyCharm 2017.3.3 (Professional Edition)

## 代码结构 ##

## 代码编写与运行结果 ##
<font color=red >项目的所有运行都是采用Run的方式传参，并执行，请读者运行时注意</font>

### 第一章-命令行工具 ###
完成一个简易的命令行工具，使用各种参数执行JVM命令  
传入参数：<pre>--cp foo/bar MyApp arg1 arg2</pre>

![](https://i.imgur.com/i9Xfu5c.png)
采用OptionParser作为命令行解析器，具体处理的打印输入留给Cmd类去处理。

### 第二章-搜索class文件 ###
