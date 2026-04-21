from __future__ import annotations

import json
import os
import threading
import time
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from .simulator import SIMULATOR

try:
    import serial
    from serial import SerialException
except ImportError:  # pragma: no cover
    serial = None
    SerialException = Exception


@dataclass
class SerialConfig:
    port: str
    baudrate: int
    timeout: float


class ESP32SerialReader:
    def __init__(self) -> None:
        self._thread: threading.Thread | None = None
        self._stop_event = threading.Event()

    def _build_config(self) -> SerialConfig:
        return SerialConfig(
            port=os.getenv("ESP32_SERIAL_PORT", "COM3"),
            baudrate=int(os.getenv("ESP32_BAUDRATE", "115200")),
            timeout=float(os.getenv("ESP32_SERIAL_TIMEOUT", "1.0")),
        )

    def start(self) -> None:
        if self._thread and self._thread.is_alive():
            return

        self._stop_event.clear()
        self._thread = threading.Thread(target=self._run, name="esp32-serial-reader", daemon=True)
        self._thread.start()

    def stop(self) -> None:
        self._stop_event.set()

    def _run(self) -> None:
        if serial is None:
            SIMULATOR.set_source_state("error", "pyserial nao instalado. Rode: pip install pyserial")
            return

        config = self._build_config()

        while not self._stop_event.is_set():
            try:
                with serial.Serial(config.port, config.baudrate, timeout=config.timeout) as conn:
                    SIMULATOR.set_source_state("connected", f"Conectado em {config.port} @ {config.baudrate}")
                    self._read_loop(conn)
            except (SerialException, OSError) as exc:
                SIMULATOR.set_source_state("error", f"Sem conexao serial em {config.port}: {exc}")
                time.sleep(2)

    def _read_loop(self, conn: Any) -> None:
        while not self._stop_event.is_set():
            raw = conn.readline()
            if not raw:
                continue

            line = raw.decode("utf-8", errors="ignore").strip()
            if not line:
                continue

            parsed = self._parse_line(line)
            if not parsed:
                continue

            SIMULATOR.add_reading(
                ph=parsed["ph"],
                turbidity=parsed["turbidity"],
                temperature=parsed["temperature"],
                tds=parsed["tds"],
                timestamp=parsed.get("timestamp"),
            )

    def _parse_line(self, line: str) -> dict[str, Any] | None:
        # Formato 1 (JSON): {"ph":7.1,"turbidity":2.8,"temperature":25.3,"tds":310}
        if line.startswith("{") and line.endswith("}"):
            try:
                payload = json.loads(line)
                return self._normalize_payload(payload)
            except json.JSONDecodeError:
                return None

        # Formato 2 (chave=valor): ph=7.1,turbidity=2.8,temperature=25.3,tds=310
        if "=" in line:
            parts = [item.strip() for item in line.split(",") if item.strip()]
            payload: dict[str, Any] = {}
            for part in parts:
                if "=" not in part:
                    continue
                key, value = part.split("=", 1)
                payload[key.strip()] = value.strip()
            return self._normalize_payload(payload)

        return None

    def _normalize_payload(self, payload: dict[str, Any]) -> dict[str, Any] | None:
        try:
            ph = float(payload["ph"])
            turbidity = float(payload["turbidity"])
            temperature = float(payload["temperature"])
            tds = float(payload["tds"])
        except (KeyError, TypeError, ValueError):
            return None

        timestamp = None
        raw_ts = payload.get("timestamp")
        if raw_ts:
            try:
                timestamp = datetime.fromisoformat(str(raw_ts))
            except ValueError:
                timestamp = None

        return {
            "ph": ph,
            "turbidity": turbidity,
            "temperature": temperature,
            "tds": tds,
            "timestamp": timestamp,
        }


SERIAL_READER = ESP32SerialReader()
