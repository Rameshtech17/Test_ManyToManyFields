from django.urls import path
from .views import BookView, AutherView, AlbumView, TrackView, AlbumTrackView, ClassView, StudentView, ClassStudentView
urlpatterns = [
    path('book/', BookView.as_view()),
    path('auther/', AutherView.as_view()),
    path('album/', AlbumView.as_view()),
    path('track/', TrackView.as_view()),
    path('albumtrack/', AlbumTrackView.as_view()),
    path('class/', ClassView.as_view()),
    path('student/', StudentView.as_view()),
    path('classstudent/', ClassStudentView.as_view()),

]
