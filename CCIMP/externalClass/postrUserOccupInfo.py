

from externalClass.postRegisterinfo import post_registerinfo


def UpUserOccupInfo(levelRoleData,request):


    register_url = 'http://trial.51talk.com/api/upUserOccupInfo'

    resInfo = request.post(url=register_url,data=levelRoleData)

    print(resInfo.ok)

    return resInfo


if __name__ == '__main__':

    occup = '2'
    grade = '0'
    purpose = '21'

    # 修改用户身份
    mobile = '17011220063'
    password = '111111'
    recommen_mobile = '18611221275'

    # 用户登录，查询该手机的账户与密码内容
    res = post_registerinfo(mobile,password,recommen_mobile)

    levelRoleData = {
      'occup' : '2',
      'grade' : '0',
      'purpose' : '21'
    }

    UpUserOccupInfo(levelRoleData,res['requestSession'])