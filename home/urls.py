from django.urls import path

from home.views import ( homeView,
servicesView,
contactusView,
aboutusView,
blogDetailView,
blogListView,
quoteView
)
urlpatterns = [
    path('',homeView.as_view(),name= 'home'),
    path('services',servicesView.as_view(),name= 'services'),
    path('contactus',contactusView.as_view(),name= 'contactus'),
    path('aboutus',aboutusView.as_view(),name= 'aboutus'),
    path('detail/<int:pk>/', blogDetailView.as_view(), name='blog_detail'),
    path('bloglist',blogListView.as_view(),name= 'blog_list'),
    path('getquote',quoteView.as_view(),name= 'quote'),
    
    

    
    
    
]
