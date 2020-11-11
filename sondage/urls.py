"""sondage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

from appli import urls, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('liste_sondages', views.liste_sondages, name='liste_sondages'),
    path('repondre_sondage/<int:id_sondage>/<int:id_question>', views.repondre_sondage, name='repondre_sondage'),
    path('enregister_reponse', views.enregistrer_reponse, name='enregistrer_reponse'),
    path('connexion_get', views.connexion_get, name='connexion_get'),
    path('connexion_post', views.connexion_post, name='connexion_post'),
    path('inscription_get', views.inscription_get, name='inscription_get'),
    path('inscription_post', views.inscription_post, name='inscription_post'),
    path('logout', views.deconnexion, name='deconnexion'),
    path('', views.homepage, name='homepage'),
    path('modifier_mdp_get', views.modifier_mdp_get , name='modifier_mdp_get'),
    path('modifier_mdp_post', views.modifier_mdp_post, name='modifier_mdp_post'),
    path('mes_reponses/<int:id_sondage>', views.mes_reponses, name='mes_reponses'),
]
