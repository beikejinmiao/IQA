## Usage
 - test   
`python iqa.py --mode=test`
 - 启动Web服务     
`python iqa.py --mode=server`             
然后访问 http://127.0.0.1:8080/  查看使用说明    

【注意】
 - 运行test/server模式之前需要下载[model.zip](https://pan.baidu.com/s/1SPlhgofybq7tgjy2SeisEg)(提取码:yeec)，解压后将内容拷贝至`resources`目录下。   
 - 也可以将`accountant_qa_dataset.csv`(model.zip中已包含该文件)拷贝至`resources`目录下，执行`python iqa.py --mode=train`重新训练所有模型。
 

## 项目结构介绍

### conf
配置文件目录

### libs
核心库         
 - logger.py         
实现打印日志功能         
 - resource.py
实现读取系统资源功能，主要读取字典和停顿词
 - score.py         
实现bleu和cosine计算
 - segment.py         
实现数据清洗和分词功能
 - singleton.py         
单例父类，主要保证系统资源单例
 - util.py         
实现基础工具函数，比如排序、读取文件
 - wrapper.py         
系统常用装饰器实现

### model
实现相似度计算模型，即Embedding部分，包括
 - tfidf
 - lsi
 - word2vec
   - 文本向量为把所有词向量加和后取平均值，然后使用KDTree查找最相似文本
 - doc2vec

后续可以持续补充。

### resources
存放系统资源文件，包括字典、停顿词和原始的问答数据

### server
 - socket.py         
系统socket接口(未实现)
 - webserver.py         
系统Web API

### iqa.py
系统主文件，用于解析参数、启动系统

### mode.py
负责系统流程和执行具体的任务

