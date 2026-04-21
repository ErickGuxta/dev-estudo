from __future__ import annotations

from collections import deque
from datetime import datetime
from threading import Lock
from typing import Any

THRESHOLDS = {
    "ph": {"min": 6.5, "max": 8.5, "unit": "", "name": "pH"},
    "turbidity": {"max": 5.0, "unit": "NTU", "name": "Turbidez"},
    "temperature": {"min": 10, "max": 35, "unit": "degC", "name": "Temperatura"},
    "tds": {"max": 500, "unit": "ppm", "name": "Solidos Dissolvidos (TDS)"},
}


class WaterStationSimulator:
    def __init__(self) -> None:
        self._readings: deque[dict[str, Any]] = deque(maxlen=20)
        self._alerts: deque[dict[str, Any]] = deque(maxlen=50)
        self._lock = Lock()
        self._source_status = "waiting"
        self._source_message = "Aguardando dados do ESP32"

    def _now(self) -> datetime:
        return datetime.now()

    def _point_from_values(self, ph: float, turbidity: float, temperature: float, tds: float, timestamp: datetime) -> dict[str, Any]:
        return {
            "time": timestamp.strftime("%H:%M:%S"),
            "timestamp": int(timestamp.timestamp() * 1000),
            "ph": round(max(0.0, min(14.0, ph)), 2),
            "turbidity": round(max(0.0, turbidity), 2),
            "temperature": round(temperature, 1),
            "tds": int(max(0.0, tds)),
        }

    def set_source_state(self, status: str, message: str) -> None:
        with self._lock:
            self._source_status = status
            self._source_message = message

    def add_reading(self, ph: float, turbidity: float, temperature: float, tds: float, timestamp: datetime | None = None) -> dict[str, Any]:
        ts = timestamp or self._now()
        point = self._point_from_values(ph=ph, turbidity=turbidity, temperature=temperature, tds=tds, timestamp=ts)

        with self._lock:
            self._readings.append(point)
            new_alerts = self._check_alerts(point)
            for alert in reversed(new_alerts):
                self._alerts.appendleft(alert)
            self._source_status = "connected"
            self._source_message = "Recebendo dados reais do ESP32"
            return point

    def ensure_bootstrap(self) -> None:
        return None

    def _check_alerts(self, reading: dict[str, Any]) -> list[dict[str, Any]]:
        alerts: list[dict[str, Any]] = []
        now_ms = int(self._now().timestamp() * 1000)

        if reading["ph"] < THRESHOLDS["ph"]["min"] or reading["ph"] > THRESHOLDS["ph"]["max"]:
            alerts.append(
                {
                    "id": now_ms + 1,
                    "type": "pH",
                    "message": f"pH critico: {reading['ph']}",
                    "time": reading["time"],
                    "level": "danger",
                }
            )
        if reading["turbidity"] > THRESHOLDS["turbidity"]["max"]:
            alerts.append(
                {
                    "id": now_ms + 2,
                    "type": "Turbidez",
                    "message": f"Turbidez alta: {reading['turbidity']} NTU",
                    "time": reading["time"],
                    "level": "warning",
                }
            )
        if reading["temperature"] < THRESHOLDS["temperature"]["min"] or reading["temperature"] > THRESHOLDS["temperature"]["max"]:
            alerts.append(
                {
                    "id": now_ms + 3,
                    "type": "Temperatura",
                    "message": f"Temperatura fora do padrao: {reading['temperature']} degC",
                    "time": reading["time"],
                    "level": "warning",
                }
            )
        if reading["tds"] > THRESHOLDS["tds"]["max"]:
            alerts.append(
                {
                    "id": now_ms + 4,
                    "type": "TDS",
                    "message": f"TDS elevado: {reading['tds']} ppm",
                    "time": reading["time"],
                    "level": "warning",
                }
            )

        return alerts

    def tick(self) -> dict[str, Any]:
        with self._lock:
            return {
                "reading": self._readings[-1] if self._readings else None,
                "new_alerts": [],
                "alerts": list(self._alerts),
                "readings": list(self._readings),
            }

    def snapshot(self) -> dict[str, Any]:
        with self._lock:
            return {
                "readings": list(self._readings),
                "alerts": list(self._alerts),
                "thresholds": THRESHOLDS,
                "source": {
                    "status": self._source_status,
                    "message": self._source_message,
                },
            }


SIMULATOR = WaterStationSimulator()
