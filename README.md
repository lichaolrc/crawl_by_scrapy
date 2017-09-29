# 使用scrapy用来抓取示例
## 准备工作
scrapy安装，请参考相关教程
简单安装方法：pip install scrapy

## 启动方法
cd crawl_by_scrapy/crawl_by_scrapy

scrapy crawl common -a init_ip=127.0.0.1 -a init_user=root -a init_passwd=123456 -a init_db=db_common -a init_tb_name=tb_url_common -a init_output_dir=output_html_common

### 参数说明（数据库使用mysql）
## init_ip
数据库对应的ip
## init_user
数据库用户名
## init_passwd
数据库密码
## init_db
数据库名字
## init_tb_name
数据库表名
## init_output_dir
抓取结果输出路径

### 功能说明
## 数据库中存放待抓取的url
具体需要包含两列
url：带抓取的url
status：抓取状态，初始值为0



