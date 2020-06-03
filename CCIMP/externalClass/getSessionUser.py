__author__ = 'zhangbo'

def getSessionUser(request):

    get_username = request.session.get('user','')

    return get_username

