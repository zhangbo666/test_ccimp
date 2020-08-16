import requests


def post_registerinfo(mobile,password,recommen_mobile):

    request = requests.Session()

    headers = {

        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '136',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie':'PHPSESSID=gugsrib7gl37fkcdamfdpfue11; uuid=6f2b2cc2-83b5-4180-aa44-b7cc68c4f16a; servChkFlag=sso; SpMLdaPx_poid=1; SpMLdaPx_pvid=1592007587997; SpMLdaPx_uuid=8205672434; SpMLdaPx_sid=8221223284; Hm_lvt_cd5cd03181b14b3269f31c9cc8fe277f=1592007588; Hm_lpvt_cd5cd03181b14b3269f31c9cc8fe277f=1592007588; Hm_lvt_12bb113d16ba4f5e8689b4a441a1d6a2=1592007588; Hm_lpvt_12bb113d16ba4f5e8689b4a441a1d6a2=1592007588',
        'Host': 'login.51talk.com',
        'Origin': 'http://login.51talk.com',
        'Referer': 'http://login.51talk.com/web/register',
        'Upgrade-Insecure-Requests': '1',
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
    }


    #mobileCheck_url = 'http://www.51talk.com/Ajax/homeMobilEvalidate'
    #check_mobile = {"mobile": mobile}


    register_url = 'http://login.51talk.com/ajax/register'
    ajax_data = {

        'mobile': mobile,
        'password': password,
        'nick_name': '',
        'recommen_mobile': recommen_mobile,
        'privacy': '1',
        'client': '1',
        'user_type': '0',
        'ufu':'',
        'from_url':'',
        'register_from':'3',
        'parent_id':'0'
    }

    res = request.post(url=register_url,data=ajax_data,headers=headers)

    # res_cookiese = requests.utils.dict_from_cookiejar(res.cookies)
    # print (res_cookiese)

    #重定向页面1
    trial_reserve_url = 'http://trial.51talk.com/trial/reserv'
    res = request.get(url=trial_reserve_url)

    #重定向页面2
    url = 'http://trial.51talk.com/api/trialConfig'
    res = request.get(url=url)

    #存储request请求和状态
    listDate = {"statue":res.reason,"requestSession":request}

    return listDate


if __name__ == '__main__':

    mobile = '18911666703'
    password = '123456'
    recommen_mobile = '18611221275'

    # 用户登录，查询该手机的账户与密码内容
    post_registerinfo(mobile,password,recommen_mobile)