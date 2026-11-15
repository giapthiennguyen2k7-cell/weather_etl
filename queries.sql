-- Bước 5: kiểm tra bằng SQL (chạy trong sqlite3 hoặc DB Browser)

-- 1) Chạy etl.py 2 lần, số dòng phải không đổi
SELECT COUNT(*) FROM weather;

-- 2) TODO: nhiệt độ trung bình theo ngày (gợi ý: GROUP BY date(time))
SELECT date(time) as ngay, avg(temperature_2m) as nhiet_do_trung_binh
FROM weather 
GROUP BY date(time);