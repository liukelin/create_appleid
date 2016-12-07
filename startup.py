# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: liukelin  314566990@qq.com
# import urllib3
import sys
# import urllib
# from urllib.request import Request, urlopen
import string
import re
import os
import time
import threading
import requests
import base64
import json
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait as UI_WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
# import selenium.webdriver.support.ui as ui

from PIL import Image,ImageEnhance,ImageFilter
import get_mail
# import StringIO
# import pycurl
# import http.cookiejar
# urllib3.disable_warnings() # 解决访问https报错
dir_ = os.getcwd()

webdriverDir = 'driver/chrome/chromedriver-mac32' # 使用浏览器驱动
home_url = 'https://appleid.apple.com/account/'
captcha_url = 'https://appleid.apple.com/captcha' # 获取验证码
# captcha_url = 'https://baidu.com' #获取验证码


def set_logs(msg, file):
    f = open('%s/%s' % (dir_,file),'a')
    f.write(msg)
    f.close()


# def headerCookie(buf):
#     print buf
'''
def get_home():
	# http = urllib3.PoolManager()
	# r = http.request('get', home_url，, headers={'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0','Cookie':"s_fid=07327DCFDD357531-3C549EF760063CDA; s_vnum_n2_us=4%7C3%2C3%7C2%2C0%7C1; s_vi=[CS]v1|2B054D5305013471-600001370003839D[CE]; s_vnum_n2_cn=30%7C1%2C97%7C1%2C11%7C1; xp_ci=3z400KbNzEtnz4ibzA1cz1IlUpybOQ; dssid2=a0d8a6cd-bd35-4010-8573-0b14eb15dd9d; dssf=1; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE=; optimizelySegments=%7B%22341793217%22%3A%22direct%22%2C%22341824156%22%3A%22ff%22%2C%22341794206%22%3A%22false%22%2C%22341932127%22%3A%22none%22%7D; optimizelyBuckets=%7B%223734690121%22%3A%223706702516%22%2C%223741255204%22%3A%223728942279%22%7D; optimizelyEndUserId=oeu1448972661575r0.766254609078395; pxro=2; geo=CN; ccl=nLfl1gUa3wVx30hy+oVGSA==; s_cc=true; s_orientation=%5B%5BB%5D%5D; s_sq=%5B%5BB%5D%5D; s_orientationHeight=637; aid=B2210B87B9D2E7120A45F47CA7D3E0049415F0FE4122371C104AD04DA8F0361E7F699679B1F89A1E258B6C6492F5D166B6BEE2C13086D20BF479120145C3D11914F6A892836FC73C02E2BCE71FE6FB6A17F9CD8A6EEB89832BC52CB5097C7D2032F8F72BEA22E768B4A943E9DE9DB04D5D6E0944C649D787F123F33F20589270012AE5E893C6D385BE436490627F578E4AB88D8EC5DAE4A59A73064F3F8BFE9180C45AA4AB4AB62CD5953B3FA3AD94F5C348589CD82B3ECFF96BB01323DF4911400A40107DB0DB0DA38CAE55542111034684176B52B7011BA544A64FD84329068E0CED395F0962401D3A1CDD9D5C5EB1528EDDA963ABB2ECE631A36A2FD292F4; idclient=web; dslang=CN-ZH; site=CHN"})
	# m = r.data
	# print(r)
	
	url='http://tieba.baidu.com/p/3226000463'
	user_agents=['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
	             'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 BIDUBrowser/6.x Safari/537.31',
	             'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.44 Safari/537.36 OPR/24.0.1558.25 (Edition Next)',
	             'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36 OPR/23.0.1522.60 (Edition Campaign 54)'
	             ]
	user_agent=random.choice(user_agents)
	print(user_agent)
	myheader={'User_Agent':user_agent,'Referer':'http://tieba.baidu.com/p/3226000463','Host':'cpro.baidu.com','GET':url}
	print(myheader)
	req=urllib.request.Request(url,headers=myheader)
	html=urllib.request.urlopen(req)
	
	# url = home_url
	# header_dict={'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0','scnt':12312313}
	# req=urllib.request.Request(url,headers=header_dict)
	# html=urllib.request.urlopen(req)
	# htmlCode = html.read()
	# print(htmlCode)

	
	ghost = Ghost()
	page, extra_resources = ghost.open(url)
	if page.http_status==200 and 'accountName' in ghost1.content :
		set_logs(htmlCode,'html.html')
	print(age.http_status)
	
	# ghost = Ghost()
	# with ghost.start() as session:
	# 	page, extra_resources = session.open(url)
	# 	if page.http_status == 200 and 'accountName' in page.content:
	#     		print(page.content)
'''
'''
def get_captcha():
	
	# http = urllib3.PoolManager()
	# r = http.request('post', captcha_url, body=‘{"type":"IMAGE"}’,headers={'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0','Cookie':"s_fid=07327DCFDD357531-3C549EF760063CDA; s_vnum_n2_us=4%7C3%2C3%7C2%2C0%7C1; s_vi=[CS]v1|2B054D5305013471-600001370003839D[CE]; s_vnum_n2_cn=30%7C1%2C97%7C1%2C11%7C1; xp_ci=3z400KbNzEtnz4ibzA1cz1IlUpybOQ; dssid2=a0d8a6cd-bd35-4010-8573-0b14eb15dd9d; dssf=1; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE=; optimizelySegments=%7B%22341793217%22%3A%22direct%22%2C%22341824156%22%3A%22ff%22%2C%22341794206%22%3A%22false%22%2C%22341932127%22%3A%22none%22%7D; optimizelyBuckets=%7B%223734690121%22%3A%223706702516%22%2C%223741255204%22%3A%223728942279%22%7D; optimizelyEndUserId=oeu1448972661575r0.766254609078395; pxro=2; geo=CN; ccl=nLfl1gUa3wVx30hy+oVGSA==; s_cc=true; s_orientation=%5B%5BB%5D%5D; s_sq=%5B%5BB%5D%5D; s_orientationHeight=637; aid=B2210B87B9D2E7120A45F47CA7D3E0049415F0FE4122371C104AD04DA8F0361E7F699679B1F89A1E258B6C6492F5D166B6BEE2C13086D20BF479120145C3D11914F6A892836FC73C02E2BCE71FE6FB6A17F9CD8A6EEB89832BC52CB5097C7D2032F8F72BEA22E768B4A943E9DE9DB04D5D6E0944C649D787F123F33F20589270012AE5E893C6D385BE436490627F578E4AB88D8EC5DAE4A59A73064F3F8BFE9180C45AA4AB4AB62CD5953B3FA3AD94F5C348589CD82B3ECFF96BB01323DF4911400A40107DB0DB0DA38CAE55542111034684176B52B7011BA544A64FD84329068E0CED395F0962401D3A1CDD9D5C5EB1528EDDA963ABB2ECE631A36A2FD292F4; idclient=web; dslang=CN-ZH;site=CHN"})
	# m = r.data
	# r.headers
	url = captcha_url
	pdata = {"type":"IMAGE"}
	header_dict={'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0','Cookie':'s_fid=07327DCFDD357531-3C549EF760063CDA; s_vnum_n2_us=4%7C3%2C3%7C2%2C0%7C1; s_vi=[CS]v1|2B054D5305013471-600001370003839D[CE]; s_vnum_n2_cn=30%7C1%2C97%7C1%2C11%7C1; xp_ci=3z400KbNzEtnz4ibzA1cz1IlUpybOQ; dssid2=a0d8a6cd-bd35-4010-8573-0b14eb15dd9d; dssf=1; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE=; optimizelySegments=%7B%22341793217%22%3A%22direct%22%2C%22341824156%22%3A%22ff%22%2C%22341794206%22%3A%22false%22%2C%22341932127%22%3A%22none%22%7D; optimizelyBuckets=%7B%223734690121%22%3A%223706702516%22%2C%223741255204%22%3A%223728942279%22%7D; optimizelyEndUserId=oeu1448972661575r0.766254609078395; pxro=2; geo=CN; ccl=nLfl1gUa3wVx30hy+oVGSA==; s_cc=true; s_orientation=%5B%5BB%5D%5D; s_sq=%5B%5BB%5D%5D; s_orientationHeight=637; aid=B2210B87B9D2E7120A45F47CA7D3E0049415F0FE4122371C104AD04DA8F0361E7F699679B1F89A1E258B6C6492F5D166B6BEE2C13086D20BF479120145C3D11914F6A892836FC73C02E2BCE71FE6FB6A17F9CD8A6EEB89832BC52CB5097C7D2032F8F72BEA22E768B4A943E9DE9DB04D5D6E0944C649D787F123F33F20589270012AE5E893C6D385BE436490627F578E4AB88D8EC5DAE4A59A73064F3F8BFE9180C45AA4AB4AB62CD5953B3FA3AD94F5C348589CD82B3ECFF96BB01323DF4911400A40107DB0DB0DA38CAE55542111034684176B52B7011BA544A64FD84329068E0CED395F0962401D3A1CDD9D5C5EB1528EDDA963ABB2ECE631A36A2FD292F4; idclient=web; dslang=CN-ZH;site=CHN'}

	tmp_pdata = urllib.parse.urlencode(pdata)
	req = Request(url=url,
		data=tmp_pdata.encode(encoding="utf-8",errors="ignore"),
		headers=header_dict,method='POST')
	f = urlopen(req,timeout=120)
	htmlCode = f.read()

	set_logs(str(htmlCode),'get_captcha.html')
	print(htmlCode)
'''

# 一直等待某元素可见，默认超时10秒 locator 为XPATH 选择器
def is_visible(driver, locator, timeout=10):
    try:
        UI_WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        return True
    except TimeoutException:
        return False

# 一直等待某个元素消失，默认超时10秒 locator 为XPATH 选择器
def is_not_visible(driver, locator, timeout=10):
    try:
        UI_WebDriverWait(driver, timeout).until_not(EC.visibility_of_element_located((By.XPATH, locator)))
        return True
    except TimeoutException:
        return False

'''
	body={
		'email':'liukelin_4@163.com',
		'emailPassword': '0734', 	# 邮箱登录密码
		'password':'Liu1234567',		# 注册密码
		'last_name':'liu',
		'first_name':'kelin',
		'birthday_field':'1990-11-22',
		'answer1':'问题答案1',
		'answer2':'问题答案2',
		'answer3':'问题答案3',
	}
'''
def create_apple(body={}):
	# 使用内核打开浏览器
	browser = webdriver.Chrome(executable_path = webdriverDir)

	browser.get(home_url)

	nowhandle = browser.current_window_handle # 得到当前窗口句柄

	# 获取网页cookie
	cookie = [item["name"] + "=" + item["value"] for item in browser.get_cookies()]
	cookiestr = ';'.join(item for item in cookie)


	browser.find_element_by_css_selector("input[type=\"email\"]").send_keys(body['email'])
	browser.find_element_by_id("password").send_keys(body['password'])
	browser.find_element_by_css_selector("input[placeholder=\"确认密码\"]").send_keys(body['password'])

	browser.find_element_by_class_name("last-name").send_keys(body['last_name'])
	browser.find_element_by_class_name("first-name").send_keys(body['first_name'])
	browser.find_element_by_class_name("birthday-field").send_keys(body['birthday_field'])

	browser.implicitly_wait(2)

	# 选择问题答案
	# browser.find_element_by_xpath("//div[@id='widget']/div[1]/div[1]/div[3]/security-questions-answers[1]")
	Select(browser.find_element_by_xpath("//div[@id='widget']/div[1]/div[1]/div[3]/security-questions-answers[1]/div[1]/div[1]/security-question[1]/div[1]/div[1]/select[1]")).select_by_index(1)
	Select(browser.find_element_by_xpath("//div[@id='widget']/div[1]/div[1]/div[3]/security-questions-answers[1]/div[1]/div[2]/security-question[1]/div[1]/div[1]/select[1]")).select_by_index(1)
	Select(browser.find_element_by_xpath("//div[@id='widget']/div[1]/div[1]/div[3]/security-questions-answers[1]/div[1]/div[3]/security-question[1]/div[1]/div[1]/select[1]")).select_by_index(1)


	# 填入问题答案
	# answers = browser.find_element_by_css_selector("input[placeholder=\"答案\"]") 
	browser.find_element_by_xpath("//security-answer[@answer-number=\"1\"]/div[1]/input[1]").send_keys(body['answer1'])
	browser.find_element_by_xpath("//security-answer[@answer-number=\"2\"]/div[1]/input[1]").send_keys(body['answer2'])
	browser.find_element_by_xpath("//security-answer[@answer-number=\"3\"]/div[1]/input[1]").send_keys(body['answer3'])

	browser.implicitly_wait(2)

	# 获取验证码图片
	# ss = browser.find_element_by_xpath("//div[@class=\"idms-captcha-wrapper\"]/img[0]").get_attribute('src')
	# browser.find_element_by_css_selector("img[width=\"120\"]").clear()
	checkImgCode = is_visible(browser, "//img[@width=\"120\"]")
	if checkImgCode==False:
		print("===加载图片验证码失败！")
		return False
	ss = browser.find_element_by_css_selector("img[width=\"120\"]").get_attribute('src')
	imgdata = ss.replace('data:image/jpeg;base64,', '')
	imgdata = base64.b64decode(imgdata)
	
	filename = 'code/%s.jpeg' %str(int(time.time()))
	file=open(filename,'wb')
	file.write(imgdata)
	file.close()
	try:
		imgdata = Image.open(filename)
		imgdata.show() # 预览图
		imgdata.close()
	except:
		pass

	# 输入验证码
	Code = input("请输入图片验证码 :")
	browser.find_element_by_id("captchaInput").send_keys(Code)

	time.sleep(1)
		
	# 继续
	browser.find_element_by_class_name("continue").click()

	time.sleep(5)

	# aalhandles = browser.window_handles # 获取所有窗口句柄
	# for handle in aalhandles: # 在所有窗口中查找弹出窗口
	# 	print("===", handle)
	# 	if handle != nowhandle:
	# 		print("===进入窗口！")
	# 		browser.switch_to_window(handle) # 这两步是在弹出窗口中进行的操作，证明我们确实进入了

	# 判断是否进入邮箱输入验证码 弹窗
	checkMailWin = is_visible(browser, "//input[@id=\"char0\"]")
	if checkMailWin==False:
		print('===未检测到邮件验证码输入框！')
		return False
	print('===进入邮件验证码输入框ok!')

	'''
	此处调用get_mail.py 代码 登录邮箱获取内容验证码
	'''
	time.sleep(10)
	print('===获取邮件验证码中...')
	mailCode = get_mail.get_apple_code(body['email'], body['emailPassword'], 2)
	if len(mailCode)==0: 
		print('===重试获取邮件验证码...')
		# 重试
		time.sleep(10)
		mailCode = get_mail.get_apple_code(body['email'], body['emailPassword'], 2)
	if len(mailCode)==0:
		print('===获取邮件验证码失败！')
		return False
	print('===成功获取邮件验证码:',mailCode[0])

	char = []
	for i in str(mailCode[0]):
		char.append(i)

    # 填入邮件验证码
	browser.find_element_by_id("char0").send_keys(char[0])
	browser.find_element_by_id("char1").send_keys(char[1])
	browser.find_element_by_id("char2").send_keys(char[2])
	browser.find_element_by_id("char3").send_keys(char[3])
	browser.find_element_by_id("char4").send_keys(char[4])
	browser.find_element_by_id("char5").send_keys(char[5])
	# browser.find_element_by_class_name("continue").click()
	browser.find_element_by_xpath("//div[@class=\"idms-modal-dialog\"]/div[1]/verify-email[1]/div[2]/div[2]/button[2]").click()
	# browser.find_element_by_partial_link_text("验证").click()

	time.sleep(10)
	browser.implicitly_wait(10)

	# browser.switch_to_window(nowhandle) # 返回到主窗口页面

	# browser.quit() # 关闭浏览器
	# display.stop() # 关闭GUI


if __name__ == "__main__":
	# get_captcha()
	# get_home()
	# fy3096257641@sina.com&Ffyqv712
	# t71388500@sina.com&bpdox917
	# jg1244533@sina.com&rmus320
	body = {
			'email':'liukelin_4@163.com',
			'emailPassword': '0734', 	# 邮箱登录密码

			'password':'Liu1234567',		# 注册密码
			'last_name':'liu',
			'first_name':'kelin',
			'birthday_field':'1990-11-22',
			'answer1':'问题答案1',
			'answer2':'问题答案2',
			'answer3':'问题答案3',
		}
	open_apple(body)





