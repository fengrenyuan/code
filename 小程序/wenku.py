#coding:utf-8
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import requests
import re
from collections import defaultdict

def driver_open(key_word):
    url = "http://xueshu.baidu.com/"
#     driver = webdriver.PhantomJS("D:/phantomjs-2.1.1-windows/bin/phantomjs.exe")    
    driver = webdriver.Chrome('./chromedriver')
    driver.get(url)
    time.sleep(10)
    driver.find_element_by_class_name('s_ipt').send_keys(key_word)
    time.sleep(2)
    driver.find_element_by_class_name('s_btn_wr').click()
    time.sleep(2)

    content = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(content, 'lxml')
    check = soup.select('div.con_reference')
    if check != []:
        res = soup.select('div.con_reference')[0].select('p.request_situ')[0]
        while res.text != '加载中'.decode('utf-8'):

        	driver.find_element_by_class_name('con_reference').find_element_by_class_name('dl_more').click()
        	time.sleep(5)

        	content = driver.page_source.encode('utf-8')
        	soup = BeautifulSoup(content, 'lxml')
        	res = soup.select('div.con_reference')[0].select('p.request_situ')[0]

        driver.close()
        res = soup.select('ul.reference_lists')[0].select('a.relative_title')
        # res = soup.select('div.con_reference')[0].select('p.request_situ')[0]
        return res
    else:
        driver.find_element_by_class_name('sc_content').find_element_by_tag_name('a').click()
        time.sleep(5)
        handles = driver.window_handles
        for handle in handles:
            if handle != driver.current_window_handle:
                driver.switch_to_window(handle)
                break

        content = driver.page_source.encode('utf-8')
        soup = BeautifulSoup(content, 'lxml')
        res = soup.select('div.con_reference')[0].select('p.request_situ')
        if res != []:
            res = soup.select('div.con_reference')[0].select('p.request_situ')[0]
            while res.text != '加载中'.decode('utf-8'):

                driver.find_element_by_class_name('con_reference').find_element_by_class_name('dl_more').click()
                time.sleep(5)

                content = driver.page_source.encode('utf-8')
                soup = BeautifulSoup(content, 'lxml')
                res = soup.select('div.con_reference')[0].select('p.request_situ')[0]

        driver.close()
        res = soup.select('ul.reference_lists')[0].select('a.relative_title')
        return res


res = driver_open('there')
for i in res:
	print i.text