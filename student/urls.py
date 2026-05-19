from rest_framework.routers import DefaultRouter

from student.views import StudentViewSet

router = DefaultRouter()
router.register('students', StudentViewSet)
urlpatterns = router.urls