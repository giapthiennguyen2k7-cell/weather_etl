"""ETL nhỏ: Open-Meteo API -> làm sạch -> SQLite.

Làm lần lượt từng bước, chạy được bước nào rồi mới sang bước sau.
Tìm các dòng có TODO để biết chỗ cần tự điền.
"""
import json
import logging
import sqlite3
from pathlib import Path

import requests

URL = "https://api.open-meteo.com/v1/forecast"
PARAMS = {
    # TODO (bước 0): đọc docs Open-Meteo rồi điền
    # latitude, longitude, hourly (temperature_2m, relative_humidity_2m), timezone
}
RAW = Path("data/raw.json")
DB = "weather.db"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)


def fetch():
    """Extract: gọi API, lưu JSON gốc vào data/raw.json, trả về dict."""
    # TODO (bước 1):
    # - requests.get(URL, params=PARAMS, timeout=...)
    # - raise_for_status(), bắt lỗi mạng bằng try/except
    # - tạo thư mục data/ nếu chưa có, ghi JSON gốc ra RAW
    # - return resp.json()
    ...


def to_rows(data):
    """Transform: biến các mảng song song thành từng dòng (time, temp, humidity)."""
    h = data["hourly"]
    for t, temp, hum in zip(h["time"], h["temperature_2m"], h["relative_humidity_2m"]):
        # TODO (bước 2): xử lý None, ép kiểu, rồi yield (t, temp, hum)
        ...


def load(rows):
    """Load: ghi vào SQLite, chạy lại nhiều lần không bị trùng dòng."""
    conn = sqlite3.connect(DB)
    with conn:
        # TODO (bước 3):
        # - CREATE TABLE IF NOT EXISTS ... (time là PRIMARY KEY)
        # - executemany(...) với dấu ?, dùng upsert (ON CONFLICT ... DO UPDATE)
        ...
    conn.close()


def main():
    data = fetch()
    load(to_rows(data))
    # TODO (bước 4): log số dòng lấy được và số dòng đã ghi
    logging.info("Xong")


if __name__ == "__main__":
    main()
