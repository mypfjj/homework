from django.urls import path

from . import views
#由于根本没有用到view.month view.article 所以先注释掉
urlpatterns = [
    path('hw/create',views.HomeworkCreate.as_view())
    #path('articles/<int:year>/', views.year_archive),
    #path('articles/<int:year>/<int:month>/', views.month_archive),
    #path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
]