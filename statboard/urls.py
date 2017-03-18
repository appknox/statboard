"""statboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from statboard.core.views import github_prs
from statboard.core.views import github_issues
from statboard.core.views import twitter_widgets

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^%s$' % settings.VIEW_GITHUB_PRS, github_prs),
    url(r'^%s$' % settings.VIEW_GITHUB_ISSUES, github_issues),
    url(r'^twitter_widgets$', twitter_widgets),
]
