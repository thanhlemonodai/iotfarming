from django.urls import path
from . import views

urlpatterns = [
    ######## nonAPI #############
    path('farmstatus/viewall/', views.farm_status_view_all,
         name='farm-status-view-all'),
    path('farminfo/viewall/', views.farm_information_view,
             name='farm-info-view'),
    path('vegetablestatus/viewall/', views.vegetable_status_view,
             name='vegetable-status-view'),
    path('vegetable/viewall/', views.vegetable_view,
             name='vegetable-view'),


    #########  API ###############
    #--------  Farm status ------#
    path('api/farm-status/view/',
         views.api_farm_status_list,
         name='api-farm-status-list-view'),
    path('api/farm-status/view/last/',
         views.api_farm_status_lastdata,
         name='api-farm-status-lastdata'),
    path('api/farm-status/view/<str:pk>/',
         views.api_farm_status_detail,
         name='api-farm-status-detail-view'),
    path('api/farm-status/create/',
         views.api_farm_status_create,
         name='api-farm-status-create'),
    path('api/farm-status/update/<str:pk>',
         views.api_farm_status_update,
         name='api-farm-status-update'),

    #########  API ###############
    #--------  Farm info   ------#

    path('api/farm-info/view/',
         views.api_farm_info_list,
         name='api-farm-info-list'),
    path('api/farm-info/view/<str:pk>/',
         views.api_farm_info_detail,
         name='api-farm-info-detail-view'),
    path('api/farm-info/create/',
         views.api_farm_info_create,
         name='api-farm-info-create'),
    path('api/farm-info/update/<str:pk>',
         views.api_farm_info_update,
         name='api-farm-info-update'),

    ############# API #####################
    #-----------  Vegetable info ---------#
    path('api/veget-info/view/',
         views.api_vegetable_list,
         name='api-vegetable-list-view'),
    path('api/veget-info/view/<str:pk>/',
         views.api_vegetable_detail,
         name='api-vegetable-detail-view'),
    path('api/veget-info/create/',
         views.api_vegetable_post,
         name='api-vegetable-create'),
    path('api/veget-info/update/<str:pk>',
         views.api_vegetable_update,
         name='api-vegetable-update'),

############# API #####################
    #-----------  Vegetable info ---------#
    path('api/veget-status/view/',
         views.api_vegetable_status_list,
         name='api-vegetable-status-list-view'),
    path('api/veget-status/view/<str:pk>/',
         views.api_vegetable_status_detail,
         name='api-vegetable-status-detail-view'),
    path('api/veget-status/create/',
         views.api_vegetable_status_post,
         name='api-vegetable-status-create'),
    path('api/veget-status/update/<str:pk>/',
         views.api_vegetable_status_update,
         name='api-vegetable-status-update'),

###########################################
    path('farm/', views.farm_view, name='farm_view'),

###########################################
    path('api/test-cam/create/',
         views.cam_model_crate,
         name='api-test-cam-create'),

    path('api/test-cam/viewall/<str:flt>/',
         views.cam_model_view_filter,
         name='api-test-cam-view-all'),

###########################################
    path('api/button/view/<str:pk>/',
         views.control_button_farm_view,
         name='control-button-farm-viewdetail'),
    

    path('api/button/update/<str:pk>/',
         views.control_button_farm_update,
         name='control-button-farm-update'),
]

