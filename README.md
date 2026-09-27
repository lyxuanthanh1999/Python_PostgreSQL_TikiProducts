# Python & PostgreSQL - Tiki Products ETL

Dự án đọc dữ liệu sản phẩm Tiki từ file JSON và nạp vào cơ sở dữ liệu PostgreSQL bằng Python (`psycopg2`).

## Cấu trúc thư mục

- `config.py`: Đọc cấu hình kết nối database từ file `database.ni` (hoặc `.ini`).
- `connect.py`: Kiểm tra và thiết lập kết nối tới PostgreSQL server.
- `create_table.py`: Tạo bảng `products` trong PostgreSQL.
- `insert.py`: Đọc file dữ liệu sản phẩm JSON, chuẩn hóa dữ liệu và nạp theo mẻ (batching) vào PostgreSQL.
- `tikiproducts.sql`: Script truy vấn kiểm tra dữ liệu sản phẩm trong DB.
- `requirements.txt`: Các thư viện phụ thuộc (`psycopg2-binary`).
- `database.ni`: File cấu hình kết nối database cục bộ.

## Hướng dẫn sử dụng

1. **Cài đặt thư viện phụ thuộc:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Cấu hình database trong file `database.ni`:**
   ```ini
   [postgresql]
   host=localhost
   database=tiki_product
   user=postgres
   password=your_password
   ```

3. **Kiểm tra kết nối và tạo bảng:**
   ```bash
   python connect.py
   python create_table.py
   ```

4. **Nạp dữ liệu:**
   Đặt file `products_output.json` vào thư mục `input/` và chạy:
   ```bash
   python insert.py
   ```
