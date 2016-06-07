# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
import urllib3
# import urllib
# from urllib.request import Request, urlopen
import string
import re
import os
import time
import threading
# import StringIO
# import pycurl
# import http.cookiejar
from ghost import Ghost
import ghost

# urllib3.disable_warnings() # 解决访问https报错
dir_ = os.getcwd()


home_url = 'https://appleid.apple.com/account/'
captcha_url = 'https://appleid.apple.com/captcha' #获取验证码
# captcha_url = 'https://baidu.com' #获取验证码


def set_logs(msg, file):
    f = open('%s/%s' % (dir_,file),'a')
    f.write(msg)
    f.close()


# def headerCookie(buf):
#     print buf
def get_home():
	# http = urllib3.PoolManager()
	# r = http.request('get', home_url，, headers={'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0','Cookie':"s_fid=07327DCFDD357531-3C549EF760063CDA; s_vnum_n2_us=4%7C3%2C3%7C2%2C0%7C1; s_vi=[CS]v1|2B054D5305013471-600001370003839D[CE]; s_vnum_n2_cn=30%7C1%2C97%7C1%2C11%7C1; xp_ci=3z400KbNzEtnz4ibzA1cz1IlUpybOQ; dssid2=a0d8a6cd-bd35-4010-8573-0b14eb15dd9d; dssf=1; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE=; optimizelySegments=%7B%22341793217%22%3A%22direct%22%2C%22341824156%22%3A%22ff%22%2C%22341794206%22%3A%22false%22%2C%22341932127%22%3A%22none%22%7D; optimizelyBuckets=%7B%223734690121%22%3A%223706702516%22%2C%223741255204%22%3A%223728942279%22%7D; optimizelyEndUserId=oeu1448972661575r0.766254609078395; pxro=2; geo=CN; ccl=nLfl1gUa3wVx30hy+oVGSA==; s_cc=true; s_orientation=%5B%5BB%5D%5D; s_sq=%5B%5BB%5D%5D; s_orientationHeight=637; aid=B2210B87B9D2E7120A45F47CA7D3E0049415F0FE4122371C104AD04DA8F0361E7F699679B1F89A1E258B6C6492F5D166B6BEE2C13086D20BF479120145C3D11914F6A892836FC73C02E2BCE71FE6FB6A17F9CD8A6EEB89832BC52CB5097C7D2032F8F72BEA22E768B4A943E9DE9DB04D5D6E0944C649D787F123F33F20589270012AE5E893C6D385BE436490627F578E4AB88D8EC5DAE4A59A73064F3F8BFE9180C45AA4AB4AB62CD5953B3FA3AD94F5C348589CD82B3ECFF96BB01323DF4911400A40107DB0DB0DA38CAE55542111034684176B52B7011BA544A64FD84329068E0CED395F0962401D3A1CDD9D5C5EB1528EDDA963ABB2ECE631A36A2FD292F4; idclient=web; dslang=CN-ZH; site=CHN"})
	# m = r.data
	# print(r)
	'''
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
	'''
	url = home_url
	# header_dict={'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0','scnt':12312313}
	# req=urllib.request.Request(url,headers=header_dict)
	# html=urllib.request.urlopen(req)
	# htmlCode = html.read()
	# print(htmlCode)

	'''
	ghost = Ghost()
	page, extra_resources = ghost.open(url)
	if page.http_status==200 and 'accountName' in ghost1.content :
		set_logs(htmlCode,'html.html')
	print(age.http_status)
	'''
	ghost = Ghost()
	with ghost.start() as session:
		page, extra_resources = session.open(url)
		if page.http_status == 200 and 'accountName' in page.content:
	    		print(page.content)




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


if __name__ == "__main__":
	# get_captcha()
	get_home()
