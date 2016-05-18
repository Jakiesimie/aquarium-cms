from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^backup/$', views.BackupView.as_view()),
    url(r'(?P<model>.+)/list/', views.CustomList.as_view()),
    url(r'(?P<model>.+)/(?P<pk>[0-9]+)/', views.CustomDetail.as_view()),

    # url(r'map/list/', views.MapList.as_view()),
    # url(r'map/(?P<pk>[0-9]+)/', views.MapDetail.as_view()),
    # url(r'tank/list/?', views.TankList.as_view()),
    # url(r'tank/(?P<pk>[0-9]+)/', views.TankDetail.as_view()),
    # url(r'habitat/list/', views.HabitatList.as_view()),
    # url(r'habitat/(?P<pk>[0-9]+)/', views.HabitatDetail.as_view()),
    # url(r'species/list/', views.SpeciesList.as_view()),
    # url(r'species/(?P<pk>[0-9]+)/', views.SpeciesDetail.as_view()),
    #
    # url(r'grade/list/', views.GradeList.as_view()),
    # url(r'grade/(?P<pk>[0-9]+)/', views.GradeDetail.as_view()),

    # url(r'quiz/list/', views.QuizList.as_view()),
    # url(r'Quiz/(?P<pk>[0-9]+)/', views.QuizDetail.as_view()),
    # url(r'quiztext/list/', views.QuizTextList.as_view()),
    # url(r'quiztext/(?P<pk>[0-9]+)/', views.QuizTextDetail.as_view()),
    # url(r'image/list/', views.ImageList.as_view()),
    # url(r'image/(?P<pk>[0-9]+)/', views.ImageDetail.as_view()),
]




