# _*_ coding: utf-8 _*_
__author__ = 'LennonChin'
__date__ = '2017/09/16 下午 10:03'

from django.conf.urls import url

from .views import UserInfoView, UploadImageView, UpdatePasswordView, SendEmailCodeView, UpdateEmailView, MyCourseView, MyFavoriteOrgView, MyFavoriteTeacherView, MyFavoriteCourseView, MyMessageView, LogoutView

urlpatterns = [

    url(r'^info/$', UserInfoView.as_view(), name='info'),
    url(r'^image/upload/$', UploadImageView.as_view(), name='image_upload'),
    url(r'^update/password/$', UpdatePasswordView.as_view(), name='update_password'),
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name='sendemail_code'),
    url(r'^update_email/$', UpdateEmailView.as_view(), name='update_email'),


    url(r'^mycourse/$', MyCourseView.as_view(), name='mycourse'),
    url(r'^myfav/org$', MyFavoriteOrgView.as_view(), name='myfav_org'),
    url(r'^myfav/teacher$', MyFavoriteTeacherView.as_view(), name='myfav_teacher'),
    url(r'^myfav/course', MyFavoriteCourseView.as_view(), name='myfav_course'),
    url(r'^mymessage/', MyMessageView.as_view(), name='mymessage'),

    url(r'^logout/', LogoutView.as_view(), name='logout'),
]