from django.urls import path
from admissions import views
from admissions.views import addadmission
from admissions.views import addadmissionReports


urlpatterns = [
    path('newadmin/', addadmission),
    path('admreports/', addadmissionReports)
]
