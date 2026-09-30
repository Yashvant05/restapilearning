from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeeViewSet, basename='employee')

urlpatterns = [
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentDetailView),

    #path('employees/', views.Employees.as_view()),
    #path('employees/<int:pk>/', views.EmployeeDetail.as_view()), #in class based views, we need to use .as_view() method to convert the class into a view function that can be used in the URL patterns.

    path('', include(router.urls)), # Register the router URLs

    path('blogs/', views.BlogView.as_view()),
    path('comments/', views.CommentView.as_view()),

    path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),

]
