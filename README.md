# Weather ETL

Script ETL nhỏ: lấy dự báo thời tiết theo giờ của Hà Nội từ Open-Meteo, làm sạch và lưu vào SQLite.

## Dữ liệu
- Nguồn: TODO (API nào, tham số gì)
- Bảng `weather`: TODO (các cột và ý nghĩa)

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
- [ ] Chạy 2 lần liên tiếp, số dòng không đổi
- [ ] Mất mạng thì báo lỗi rõ ràng bằng log
- [ ] README đã điền đủ
- [ ] Đã đẩy lên GitHub
