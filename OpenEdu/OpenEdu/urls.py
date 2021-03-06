from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('lessons/', include('StudentLessons.urls')),
    path('lessonst/', include('TeacherLessons.urls')),
    path('shedule/', include('Shedule.urls')),
    path('gradebook/', include('GradeBook.urls')),
    path('adminpanel/', include('AdminPanel.urls')),
]
