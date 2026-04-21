from __future__ import annotations

import csv
from io import StringIO

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_http_methods

from .simulator import SIMULATOR


@require_GET
def dashboard_view(request: HttpRequest) -> HttpResponse:
    SIMULATOR.ensure_bootstrap()
    return render(request, "dashboard.html")


@require_GET
def api_snapshot(request: HttpRequest) -> JsonResponse:
    return JsonResponse(SIMULATOR.snapshot())


@require_GET
def api_tick(request: HttpRequest) -> JsonResponse:
    return JsonResponse(SIMULATOR.tick())


@require_GET
def export_csv(request: HttpRequest) -> HttpResponse:
    snapshot = SIMULATOR.snapshot()
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["Data/Hora", "pH", "Turbidez (NTU)", "Temperatura (degC)", "TDS (ppm)"])

    for row in snapshot["readings"]:
        writer.writerow([row["time"], row["ph"], row["turbidity"], row["temperature"], row["tds"]])

    response = HttpResponse(output.getvalue(), content_type="text/csv; charset=utf-8")
    response["Content-Disposition"] = "attachment; filename=relatorio_agua.csv"
    return response
