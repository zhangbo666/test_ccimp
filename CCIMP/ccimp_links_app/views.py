from django.shortcuts import render

# Create your views here.

from ccimp_user_app.views import auth

from ccimp_user_app.models.userModels import User



'''###############################################################################'''
# 友情链接
@auth
def links_manage(request):

    if request.method == "GET":

        get_username = request.session.get('user','')

        users = User.objects.all()

        for user in users:

            if user.user_name == get_username:

                if user.permission_options == 1:

                    return render(request,"links.html",
                                  {"username":get_username,
                                   "type_option_admin":"permission_sap"})

