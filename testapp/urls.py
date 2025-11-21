from django.contrib import admin
from django.urls import path

from maykin_health_checks.api.views import HealthChecksView
from testapp.checks import DummyCheck, DummyCheckFail

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "health-checks-injected-collector",
        HealthChecksView.as_view(
            checks_collector=lambda: [DummyCheck(), DummyCheckFail()]
        ),
        name="health-checks-injected-collector",
    ),
    path(
        "health-checks-injected-checks",
        HealthChecksView.as_view(checks=[DummyCheck(), DummyCheckFail()]),
        name="health-checks-injected-checks",
    ),
]
