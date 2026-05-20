from rest_framework.routers import DefaultRouter

from student.views import StudentViewSet, CourseViewSet

router = DefaultRouter()
router.register('students', StudentViewSet)
router.register('courses', CourseViewSet)
urlpatterns = router.urls