__author__ = 'zhangbo'



#手机号效验
def mobileNumberFormatValidity(user_mobile):

    if user_mobile == "":

        return 1

    elif len(user_mobile) < 11 or len(user_mobile) > 11:

        return 2

    elif user_mobile.isdigit() == False:

        return 3

    elif user_mobile.isdigit():

        return 4