"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from accounts import views as accounts_views
from boards import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls'), name='flatpages'),
    path('', views.home, name='home'),
    path('boards/create/<str:page>/', views.board_create, name='board_create'),
    path('boards/<int:pk>/update/<str:page>/', views.board_update, name='board_update'),
    path('boards/<int:pk>/delete/<str:page>/', views.board_delete, name='board_delete'),
    path('boards/<int:pk>/', views.TopicListView.as_view(), name='board_topics'),
    path('boards/<int:pk>/new/', views.new_topic, name='new_topic'),
    path('signup/', accounts_views.signup, name='signup'),
    path('signup/blogger/', accounts_views.BloggerSignUpView.as_view(), name='blogger_signup'),
    path('signup/reader/', accounts_views.ReaderSignUpView.as_view(), name='reader_signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', accounts_views.LoginViewCustom.as_view(), name='login'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('reset/', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt'
    ), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'),
         name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            auth_views.PasswordResetConfirmView.as_view(
                template_name='password_reset_confirm.html'
            ),
            name='password_reset_confirm'),
    path('reset/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'),
         name='password_reset_complete'),
    path('settings/password/', auth_views.PasswordChangeView.as_view(
        template_name='password_change.html'),
         name='password_change'),
    path('settings/password/done', auth_views.PasswordChangeDoneView.as_view(
        template_name='password_change_done.html'),
         name='password_change_done'),
    path('boards/<int:pk>/topics/<int:topic_pk>/', views.PostListView.as_view(), name='topic_posts'),
    path('boards/<int:pk>/topics/<int:topic_pk>/reply/', views.reply_topic, name='reply_topic'),
    path('boards/<int:pk>/topics/<int:topic_pk>/<int:post_pk>/edit/', views.PostUpdateView.as_view(), name='edit_post'),
    path('settings/account/', views.UserUpdateView.as_view(), name='my_account'),
    path('ajax/validate_username/', accounts_views.validate_username, name='validate_username'),
    path('boards/<int:pk>/topics/<int:topic_pk>/to_pdf/', views.html_to_pdf_view, name="to_pdf"),
    path('boards/<int:pk>/topics/<int:topic_pk>/to_csv/', views.export_users_csv, name="to_csv"),
    path('settings/account/delete-photo', views.delete_photo, name='delete_photo'),
    path('boards/<int:pk>/topics/<int:topic_pk>/gallery/',
         views.gallery_images, name="gallery_images"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
