# README

此项目计划上线至GitHub：

[WorkflowWan (github.com)](https://github.com/WorkflowWan)

号是刚建的，因为好早以前有号，我给忘了。以后就用这个账号。



本项目需严格按照相关依赖环境配置。详见requirements.txt



python解释器版本要求

```
python >= 3.9
```



按照要求配好环境和解释器后，需要连接自己的数据库。点开 `Config.py`，把数据库密码改成自己的。原先是我本地MySQL的密码1023.另外在SQL管理平台操作SQL，SQL文件 `computer college.sql`。将文件导入对应平台。



为运行代码，在终端输入

```
python -m flask run --host=0.0.0.0
```

即可运行。