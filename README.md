## ProxyPool

### 1.配置

#### 安装依赖

```
pip3 install pymysql
pip3 install requests
pip3 install bs4
pip3 install lxml
pip3 install sqlalchemy
```

#### 数据库配置

在`conf/setting.py`中配置数据库

```
DATABASE_URI = 'mysql+pymysql://root:xxx@ip:3306/proxypool?charset=utf8'
```

初始化数据库

```
python3 init.py
```

### 2.运行

抓取代理IP

```
python3 proxypool.py 
```

定时验证IP

```
python3 verify.py
```

#### 3 文件系统

```python
ProxyPool
	conf
    	init.py
        settings.py  #数据库的相关配置
    log_files        #日志信息,打印成功与错误日志信息
    	error_log.log   
        info_log.log   
    logger     
    	init.py
        error_log.py  #错误日志处理模块
        info_log.py  #信息处理模块
    logic
    	init.py
        logic_common.py  #通用模块, 获取headers  创建request 时间处理
        logic_proxypool.py   #检验IP是否可用 , 代理池中插入ip ,验证ip信息, 加载未通过验证的ip
    models
    	init.py
        models.py     # id ,ip ,port , utime(修改时间) , ctime(创建时间), 类方法
        proxypool.py  # 插入代理IP , 更新代理IP, 删除代理IP, 获取所有IP 的方法
    proxy_spiders
    	init.py
        spider_66ip.py          #http://www.66ip.cn/  66免费代理
        spider_89ip.py          #http://www.89ip.cn/   89免费代理
        spider_conderbusy.py    #https://proxy.coderbusy.com/   码农代理
        spider_data5u.py        #http://www.data5u.com   无忧代理(好几种)
        spider_kuaidaili.py     #https://www.kuaidaili.com   快代理
        spider_xicidaili.py     #http://www.xicidaili.com   西刺代理
	init.py        #数据库的初始化,并进行建表
    proxypool.py   #抓取ip启动文件
    server.py      #服务器
    verify.py      #定时验证ip进行更新
```



