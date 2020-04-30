from django.urls import path
from .views import home, AuthorDetailViewCB

urlpatterns = [
    path('', home, name='library_home'),
    path ("author/<int:pk>", AuthorDetailViewCB.as_view(), name="author_detail"),
]