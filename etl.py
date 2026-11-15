"""ETL nhỏ: Open-Meteo API -> làm sạch -> SQLite.

Làm lần lượt từng bước, chạy được bước nào rồi mới sang bước sau.
Tìm các dòng có TODO để biết chỗ cần tự điền.
"""
import json
import logging
import sqlite3
from pathlib import Path

import requests
import time 

URL = "https://api.open-meteo.com/v1/forecast"
PARAMS = {
    "latitude":21.03, 
    "longitude":105.85, 
    "hourly":"temperature_2m,relative_humidity_2m",
    "timezone": "Asia/Bangkok"
}
RAW = Path("data/raw.json")
DB = "weather.db"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)


def fetch():
    for attempt in range(3):
        try:
            resp = requests.get(URL, params = PARAMS, timeout = 10)
            resp.raise_for_status()
            data = resp.json()
            print(data)

            RAW.parent.mkdir(exist_ok=True)
            with open(RAW, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

            return data
        except requests.exceptions.Timeout:
            logging.warning("Time out, thử lại lần %d", attempt + 1)
            time.sleep(10)
        except requests.exceptions.HTTPError:
            logging.warning("HTTPError thử lại lần %d", attempt + 1)
            time.sleep(10)
        except requests.exceptions.ConnectionError: 
            logging.warning("ConnectionError thử lại lần %d", attempt + 1)
            time.sleep(10)
    raise RuntimeError("Không lấy được dữ liệu sau 3 lần thử")


def to_rows(data):
    """Transform: biến các mảng song song thành từng dòng (time, temp, humidity)."""
    h = data["hourly"]
    for t, temp, hum in zip(h["time"], h["temperature_2m"], h["relative_humidity_2m"]):
        yield (t, float(temp) if temp is not None else temp, int(hum) if hum is not None else hum)


def load(rows):
    """Load: ghi vào SQLite, chạy lại nhiều lần không bị trùng dòng."""
    conn = sqlite3.connect(DB)
    creat_sql =""" CREATE TABLE IF NOT EXISTS weather(
                    time TEXT PRIMARY KEY,
                    temperature_2m FLOAT,
                    relative_humidity_2m INT      
                );"""
    insert_table = """ INSERT INTO weather(time, temperature_2m, relative_humidity_2m)
                        VALUES(?,?,?) 
                        ON CONFLICT(time) DO UPDATE SET 
                            temperature_2m = excluded.temperature_2m,
                            relative_humidity_2m = excluded.relative_humidity_2m 
                ;"""
    cursor = conn.cursor()

    try:
        with conn:
            cursor.execute(creat_sql)
            cursor.executemany(insert_table, rows)
        logging.info("Đã ghi %d dòng vào %s", cursor.rowcount, DB)
    except sqlite3.Error:
        logging.exception("Lỗi khi ghi vào SQLite")
        raise
    finally: conn.close()


def main():
    data = fetch()
    load(to_rows(data))
    # TODO (bước 4): log số dòng lấy được và số dòng đã ghi
    logging.info("Xong")


if __name__ == "__main__":
    main()
