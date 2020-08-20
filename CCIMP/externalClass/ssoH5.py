import requests
from externalClass.adminLogin import adminLogin


def ssoH5_query(uid):

	getH5_url = 'http://www.51talk.com/Admin/Sso/geth5?uid=' + str(uid)

	#调取后台登录接口
	admin_login  = adminLogin()

	sso_query_h5 = admin_login.get(url=getH5_url)

	return sso_query_h5

def ssoH5_modify(uid,value):

	postH5_url = 'http://www.51talk.com/Admin/Sso/seth5'

	data_h5 = {}

	if value == "0":

		data_h5 = {

			"uid":uid,
			"value":value
		}

	elif value == "1":

		data_h5 = {

			"uid":uid,
			"value":value
		}

	#调取后台登录接口
	admin_login  = adminLogin()

	sso_query_h5 = admin_login.post(url=postH5_url,data=data_h5)

	return sso_query_h5


if __name__ == '__main__':

	uid = '800021389'

	value = 0

	# sso_query_h5 = ssoH5_query(uid)
	# print (sso_query_h5.json())

	# if sso_query_h5.json()['data'] == '没查到数据':

	# print("该用户不是H5标签用户")

	# elif sso_query_h5.json()['data'] == '是':

	# print("该用户是H5标签用户")


	sso_modify_h5 = ssoH5_modify(uid, value)
	# print (sso_modify_h5.json())
	# print(sso_modify_h5.json()['data'][10:11])

	if sso_modify_h5.json()['data'][10:11] == '是':

		print("修改完成,当前值为:是")

	elif sso_modify_h5.json()['data'][10:11] == '否':

		print("修改完成,当前值为:否")