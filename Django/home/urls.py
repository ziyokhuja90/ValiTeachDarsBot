from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage , name="HomePage"),
    path('search/', views.search, name='search'),
    path("login/" , views.login_view , name="login"),
    path("logout/" , views.sign_out , name="logout"),
    # path("addLesson/" , views.create_view , name="createLesson"),

    # Front-end
    path("Front-endAddlesson/" , views.createFrontEnd_view , name="CreateFrontEnd"),
    path("Front-end/" , views.FrontEnd_view , name="FronEnd_view" ),
    path("<id>/updateFrontend/" , views.update_Frontend, name="UpdateFrontend"),
    path('<id>/deleteFrontend/', views.delete_Frontend  , name="deleteFrontend"),
    #  Back-end
    path("Back-endAddlesson/" , views.createBackEnd_view , name="CreateBackEnd"),
    path("Back-end/" , views.BackEnd_view , name="BackEnd_view" ),
    path('<id>/deleteBackend/', views.delete_Backend  , name="deleteBackend"),
    path("<id>/updateBackend/" , views.update_Backend, name="UpdateBackend"),
    # Photoshop 
    path("PhotoshopAddlesson/" , views.createPhotoshop_view , name="CreatePhotoshop"),
    path("Photoshop/" , views.Photoshop_view , name="Photoshop_view" ),
    path("<id>/PhotoshopUpdate/" , views.update_Photoshop , name="UpdatePhotoshop"),
    path('<id>/PhotoshopDelete/', views.delete_Photoshop  , name="Photoshopdelete"),
    # illustrator
    path("IllustratorAddlesson/" , views.createIllustrator_view , name="CreateIllustrator"),
    path("Illustrator/" , views.Illustrator_view , name="Illustrator" ),
    path("<id>/IllustratorUpdate/" , views.update_Illustrator , name="UpdateIllustrator"),
    path('<id>/IllustratorDelete/', views.delete_Illustrator  , name="Illustratordelete"),
    # coral Draw
    path("CoraldrawAddlesson/" , views.createCoraldraw_view , name="CreateCoraldraw"),
    path("Coraldraw/" , views.Coraldraw_view , name="Coraldraw" ),
    path("<id>/CoraldrawUpdate/" , views.update_Coraldraw , name="UpdateCoraldraw"),
    path('<id>/CoraldrawDelete/', views.delete_Coraldraw , name="Coraldrawdelete"),
    # Kompyuter savodxonligi
    path("KompyuterAddlesson/" , views.createKompyuter_view , name="CreateKompyuter"),
    path("Kompyuter/" , views.Kompyuter_view , name="Kompyuter" ),
    path("<id>/KompyuterUpdate/" , views.update_Kompyuter , name="UpdateKompyuter"),
    path('<id>/KompyuterDelete/', views.delete_Kompyuter , name="Kompyuterdelete"),

    path("<id>/update/" , views.update_view , name="Update"),
    path('<id>/delete/', views.delete_view  , name="delete"),
]
