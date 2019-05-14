from django.urls import path
from .import views

urlpatterns=[

        path('',views.index,name='index'),
        path('about/',views.about,name='about'),
        path('contact/',views.contact,name='contact'),
        path('pyp/',views.pyp,name='pyp'),
        path('discussionforum/',views.discussionforum,name='discussionforum'),
        path('help/',views.help,name='help'),
        path('company/',views.company,name='company'),
        path('team/',views.team,name='team'),
        #path('offers/',views.offers,name='offers'),
        path('partners/',views.partners,name='partners'),
        path('settings/',views.settings,name='settings'),
        path('courses/',views.courses,name='courses'),
        path('subjects/quantitativeapti',views.quantitativeapti,name='subjects/quantitativeapti'),
        path('subjects/reasoning',views.reasoning,name='subjects/reasoning'),



]
