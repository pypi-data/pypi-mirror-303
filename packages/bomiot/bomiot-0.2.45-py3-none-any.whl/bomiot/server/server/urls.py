import os
from os import getcwd, listdir
from os.path import join, isdir

from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from django.contrib.staticfiles.views import serve
from django.views.static import serve as static_serve
from django.conf import settings
from . import views
import pkg_resources
from .pkgcheck import pkg_check
import importlib
import importlib.util
from configparser import ConfigParser, RawConfigParser
from pathlib import Path


def return_static(request, path, insecure=True, **kwargs):
    return serve(request, path, insecure, **kwargs)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.logins, name='login'),
    path('logout/', views.logouts, name='logout'),
    path('register/', views.registers, name='register'),
    path('checktoken/', views.check_token, name='check_token'),
    path('', include('bomiot.server.core.urls')),
]


urlpatterns += [
    path('favicon.ico', views.favicon, name='favicon'),
    re_path('^css/.*$', views.statics, name='css'),
    re_path('^js/.*$', views.statics, name='js'),
    re_path('^assets/.*$', views.statics, name='assets'),
    re_path('^statics/.*$', views.statics, name='statics'),
    re_path('^fonts/.*$', views.statics, name='fonts'),
    re_path('^icons/.*$', views.statics, name='icons'),
    re_path(r'^static/(?P<path>.*)$', return_static, name='static'),
    re_path(r'^media/(?P<path>.*)$', static_serve, {'document_root': settings.MEDIA_ROOT}),
]

CONFIG = ConfigParser()
CONFIG.read(join(os.getcwd(), 'setup.ini'), encoding='utf-8')
project_name = CONFIG.get('project', 'name', fallback='bomiot')


for module in [pkg.key for pkg in pkg_resources.working_set]:
    try:
        settings_name = 'bomiotconf'
        exists = pkg_check(module, settings_name)
        if exists:
            module_import = importlib.import_module(f'{module}.{settings_name}')
            app_mode = module_import.mode_return()
            if app_mode == 'plugins':
                has_urls = pkg_check(module, 'urls')
                if has_urls:
                    urlpatterns += [
                        path(f'{module}/', include(f'{module}.urls'))
                    ]
            elif app_mode == 'project':
                if module == project_name:
                    project_path = importlib.util.find_spec(project_name).origin
                    list_project_path = Path(project_path).resolve().parent
                    urlpatterns += [
                        path('', TemplateView.as_view(
                        template_name='dist/spa/index.html'))
                    ]
                    find_urls = [u for u in os.listdir(list_project_path) if isdir(u)]
                    for url in find_urls:
                        if importlib.util.find_spec(f'{project_name}.{url}.urls') is not None:
                            urlpatterns += [
                                path(f'{project_name}/{url}/', include(f'{project_name}.{url}.urls'))
                            ]
        else:
            continue
    except:
        continue
    finally:
        pass

current_path = [p for p in listdir(getcwd()) if isdir(p)]

for module_name in current_path:
    try:
        settings_name = 'bomiotconf'
        exists = pkg_check(module_name, settings_name)
        if exists:
            module_import = importlib.import_module(f'{module_name}.{settings_name}')
            app_mode = getattr(module_import, 'mode_return')
            if app_mode == 'plugins':
                has_urls = pkg_check(module_name, 'urls')
                if has_urls:
                    urlpatterns += [
                        path(f'{module_name}/', include(f'{module_name}.urls')),
                    ]
            elif app_mode == 'project':
                if module_name == project_name:
                    project_path = os.path.join(os.getcwd(), project_name)
                    urlpatterns += [
                        path('', TemplateView.as_view(
                            template_name='dist/spa/index.html'))
                    ]
                    find_urls = [u for u in os.listdir(project_path) if os.path.isdir(u)]
                    for url in find_urls:
                        if importlib.util.find_spec(f'{project_name}.{url}.urls') is not None:
                            urlpatterns += [
                                path(f'{project_name}/{url}/', include(f'{project_name}.{url}.urls')),
                            ]
        else:
            continue
    except:
        continue
    finally:
        pass

print(1, os.environ.get('RUN_MAIN'))