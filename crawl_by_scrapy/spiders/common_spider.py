#! /usr/bin/python 
# encoding=gb18030
############################################
#
# E-Mail: lic.jiacl@gmail.com
# version 1.1
#
############################################

import scrapy
from scrapy.selector import HtmlXPathSelector
import re
from lxml import etree
import MySQLdb
import hashlib
import logging

logging.basicConfig(level=logging.DEBUG, 
		format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', 
		datefmt='%a, %d %b %Y %H:%M:%S', filename='myapp.log', filemode='w')

class CommonSpider(scrapy.Spider):
	name = "common"
	start_urls = []
	url_num = 0
	dic_url_have = {}
	db_name = "db_url_common"
	table_name = "tb_url_common"

	db_ip = "127.0.0.1"
	db_user = "root"
	db_passwd = "123456"

	output_dir = "output_html_common"

	def __init__(self, init_ip=None, init_user=None, init_passwd=None, init_db=None, init_tb_name=None, init_output_dir=None, *args, **kwargs):

		super(CommonSpider, self).__init__(*args, **kwargs)

		self.db_ip = init_ip
		self.db_user = init_user
		self.db_passwd = init_passwd

		self.db_name = init_db
		self.table_name = init_tb_name
		self.output_dir = init_output_dir

		conn = MySQLdb.connect(host=self.db_ip, user=self.db_user, passwd=self.db_passwd, db=self.db_name, charset="utf8")
		cursor = conn.cursor()
		if cursor:
			cursor = conn.cursor()
			if cursor:
				sql_str = 'select ' + self.table_name + '.url from ' + self.table_name + ' where status=0'
				cursor.execute(sql_str)
				rows = cursor.fetchall()
				for row in rows:
					if len(row) < 1:
						continue
					url = unicode(row[0])
					url = url.encode("utf8")
					print url
					self.start_urls.append(url)
			else:
				logging.error("connnect mysql error!")

	def parse(self, response):
		conn = MySQLdb.connect(host=self.db_ip, user=self.db_user, passwd=self.db_passwd, db=self.db_name, charset="utf8")
		logging.info("real_crawl:" + response.url)

		cursor = conn.cursor()
		if cursor:
			sql_str = 'update ' + self.table_name + ' set status=1 where url="' + response.url + '"'
			cursor.execute(sql_str)
			cursor.close()
			conn.commit()
		else:
			logging.error("connnect mysql error!")

		m2 = hashlib.md5()
		m2.update(response.url)
		with open(self.output_dir + "/%s" % (m2.hexdigest()) + ".html", 'wb') as f:
			f.write(response.url)
			f.write("\n")
			f.write(response.body)
		f.close()
		self.url_num += 1
		items = []
		return items
		



