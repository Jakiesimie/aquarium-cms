from django.conf.urls import url
from views import (
    # index,

    map_list,
    map_create,
    map_update,
    map_delete,

    tank_list,
    tank_create,
    tank_update,
    tank_delete,
    tank_delete_safe, # only redirects to page with real deleter

    tank_quiz_detail,
    tank_custom_quiz_create,
    tank_custom_quiz_update,
    tank_quiz_delete,

    tank_quizimage_create,
    tank_quizimage_update,
    tank_quizimage_delete,

    tank_species_detail,
    tank_species_create,
    tank_species_update,
    tank_species_delete,

    habitat_list,
    habitat_detail,
    habitat_create,
    habitat_update,
    habitat_delete,
    habitat_delete_safe, # like in tanks - only redirects to page with warning and question about confirmation

    trivia_create,
    trivia_update,
    trivia_delete,
    )


urlpatterns = [
    url(r'^map/list/', map_list, name='mlist'),
    url(r'^map/create/$', map_create, name='mcreate'),
    url(r'^map/edit/(?P<id>[\d]+)/$', map_update, name='mupdate'),
    url(r'^map/(?P<id>[\d]+)/delete/$', map_delete, name='mdelete'),

    url(r'^tank/list/', tank_list, name='tlist'),
    url(r'^tank/create/$', tank_create, name='tcreate'),
    url(r'^tank/(?P<tank_id>[\d]+)/edit/$', tank_update, name='tupdate'),
    url(r'^tank/(?P<tank_id>[\d]+)/$', tank_quiz_detail, name='tdetail'),
    url(r'^tank/(?P<tank_id>[\d]+)/delete/done/$', tank_delete, name='tdelete'),
    url(r'^tank/(?P<tank_id>[\d]+)/delete/$', tank_delete_safe, name='tdelete_safe'),

    url(r'^tank/(?P<tank_id>[\d]+)/create/quiz/(?P<arg>[\w]+)/$', tank_custom_quiz_create, name='tcreate_cq'), # !!! or quiztype
    url(r'^tank/(?P<tank_id>[\d]+)/edit/quiz/(?P<id>[\d]+)/(?P<arg>[\w]+)/$', tank_custom_quiz_update, name='tupdate_q'),
    url(r'^tank/(?P<tank_id>[\d]+)/delete/quiz/(?P<id>[\d]+)/$', tank_quiz_delete, name='tdelete_q'),

    url(r'^tank/(?P<tank_id>[\d]+)/create/quizimage/(?P<id>[\d]+)/$', tank_quizimage_create, name='tcreate_q_im'),
    url(r'^tank/(?P<tank_id>[\d]+)/edit/quizimage/(?P<id>[\d]+)/$', tank_quizimage_update, name='tupdate_q_im'),
    url(r'^tank/(?P<tank_id>[\d]+)/delete/quizimage/(?P<id>[\d]+)/$', tank_quizimage_delete, name='tdelete_q_im'),


    url(r'^tank/(?P<tank_id>[\d]+)/spcies/$', tank_species_detail, name='tdetail_s'),
    url(r'^tank/(?P<tank_id>[\d]+)/spcies/create$', tank_species_create, name='tcreate_s'),
    url(r'^tank/(?P<tank_id>[\d]+)/spcies/(?P<id>[\d]+)/edit/$', tank_species_update, name='tupdate_s'),
    url(r'^tank/(?P<tank_id>[\d]+)/spcies/(?P<id>[\d]+)/delete$', tank_species_delete, name='tdelete_s'),

    url(r'^habitat/list/', habitat_list, name='hlist'),
    url(r'^habitat/create/$', habitat_create, name='hcreate'),
    url(r'^habitat/(?P<id>[\d]+)/$', habitat_detail, name='hdetail'),
    url(r'^habitat/(?P<id>[\d]+)/edit/$', habitat_update, name='hupdate'),
    url(r'^habitat/(?P<id>[\d]+)/delete/$', habitat_delete_safe, name='hdelete_safe'),
    url(r'^habitat/(?P<id>[\d]+)/delete/done/$', habitat_delete, name='hdelete'),

    url(r'^habitat/(?P<id>[\d]+)/create-trivia/$', trivia_create, name='hcreate_tr'),
    url(r'^habitat/(?P<id>[\d]+)/trivia/edit/(?P<trid>[\d]+)/$', trivia_update, name='hupdate_tr'),
    url(r'^habitat/(?P<hid>[\d]+)/trivia/delete/(?P<id>[\d]+)$', trivia_delete, name='hdelete_tr'),
]
