from django.urls import path

from .views import api_snapshot, api_tick, dashboard_view, export_csv

urlpatterns = [
    path("", dashboard_view, name="dashboard"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("api/snapshot/", api_snapshot, name="api_snapshot"),
    path("api/tick/", api_tick, name="api_tick"),
    path("api/export/csv/", export_csv, name="export_csv"),
]
