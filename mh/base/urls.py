from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path('profile/<str:pk>/',views.profile,name="profile"),
    path('create-profile/', views.createProfile,name="create-profile"),
    path('edit-profile/<str:pk>', views.editProfile,name="edit-profile"),
    path('delete-profile/<str:pk>', views.deleteProfile,name="delete-profile"),
    path('workshops/', views.workshops,name="workshops"),
    path('workshop/<str:pk>/', views.workshop,name="workshop"),
    path('createWorkshop/', views.createWorkshop,name="workshopForm"),
    path('edit-workshop/<str:pk>', views.EditWorkshopParticipants,name="edit-workshop-participants"),
    path('add-profile-workshop/<str:pk>', views.addProfiletoWorkshop,name="addProfileWorkshop"),
    path('confirm-add/<str:profileId>/<str:workshopId>', views.confirmAdd,name="confirmAdd"),
    path('delete-workshop/<str:pk>', views.deleteWorkshop,name="delete-workshop"),
    path('add-followup/<str:pk>',views.addFollowUp,name="add-followup"),
    path('add-referral/<str:pk>',views.addReferall,name='add-referral'),
    path('data-analysis/', views.dataAnalysis,name="data-analysis"),
    path('data-transfer/', views.dataTransfer, name="data-transfer"),
    path('data-output/',views.data_output, name="data-output"),
    path('pdf-output/<str:pk>',views.pdf_output, name="pdf-output"),
    path('likes-dislikes/<str:pk>',views.addlikesdislikes,name='likes-dislikes'),
    path('concernLevel/<str:pk>/', views.addConcernLevel,name='concernLevel'),
    path('happiness/<str:profileId>/<str:workshopId>/', views.editHappiness, name='editHappiness'),
    path('personalPlan/<str:pk>/',views.personalPlan,name='personalPlan'),
    path('addencrypted', views.add_encrypted, name="add_encrypted"),
    path('upload/', views.document_upload, name='upload'),
]