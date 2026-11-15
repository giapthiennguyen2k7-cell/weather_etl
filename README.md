# Weather ETL

Script ETL nhỏ: lấy dự báo thời tiết theo giờ của Hà Nội từ Open-Meteo, làm sạch và lưu vào SQLite.

## Dữ liệu
- Nguồn: 
    API open-meteo, 
    Tham số {
        "latitude":21.03, 
        "longitude":105.85, 
        "hourly":"temperature_2m,relative_humidity_2m",
        "timezone": "Asia/Bangkok"
    }
- Bảng `weather`: cột time, temperature_2m, relative_humidity_2m lưu thông tin cần thu thập

## Cách chạy
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python etl.py
```

## Cách hoạt động
TODO: 2–3 câu về Extract, Transform, Load và vì sao chạy lại không bị trùng dữ liệu.


## Checklist hoàn thành v1
- [x] Chạy 2 lần liên tiếp, số dòng không đổi
- [x] Mất mạng thì báo lỗi rõ ràng bằng log
- [ ] README đã điền đủ
- [x] Đã đẩy lên GitHub
