from django.conf.urls import url

from microservico import views

#melhoria trazer mensagem somente do usuario logado
urlpatterns = [
    url('mine/', views.mine),]
