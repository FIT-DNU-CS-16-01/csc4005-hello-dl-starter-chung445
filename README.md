[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Npp34-o8)
# CSC4005 – Lab 0 Starter Kit
## Lab 0: Environment Setup & Smoke-Test Pipeline

## Mục tiêu
Lab 0 giúp sinh viên:
- thiết lập môi trường Python cho học phần CSC4005,
- cài đặt các thư viện cốt lõi,
- chạy thử một pipeline học sâu tối thiểu,
- sinh log, figure, checkpoint để chứng minh môi trường hoạt động,
- chuẩn bị nền tảng cho các lab tiếp theo.

## Yêu cầu phần mềm
- Python 3.10 hoặc 3.11
- pip
- Khuyến nghị: VS Code / PyCharm / Jupyter

## Bước 1. Tạo môi trường
### Cách 1: dùng venv
```bash
python -m venv csc4005_env
```

Kích hoạt môi trường:

- Windows:
```bash
csc4005_env\Scripts\activate
```

- macOS / Linux:
```bash
source csc4005_env/bin/activate
```

## Bước 2. Cài thư viện
```bash
pip install -r requirements.txt
```

## Bước 3. Kiểm tra môi trường
```bash
python check_env.py
```

## Bước 4. Chạy smoke-test pipeline
```bash
python run_smoke_test.py
```

## Output mong đợi
Sau khi chạy thành công, hệ thống sẽ sinh ra:
- `outputs/logs/env_check.txt`
- `outputs/logs/smoke_test_log.txt`
- `outputs/figures/loss_curve.png`
- `outputs/checkpoints/smoke_model.pt`

## Kết quả chạy thực tế
- `check_env.py` chạy thành công, tạo file `outputs/logs/env_check.txt`.
- `run_smoke_test.py` chạy thành công, lưu log `outputs/logs/smoke_test_log.txt`, figure `outputs/figures/loss_curve.png`, và checkpoint `outputs/checkpoints/smoke_model.pt`.
- Kết quả huấn luyện:
  - Epoch 1/3 | train_loss=0.8189 | test_loss=0.6842 | test_acc=0.5200
  - Epoch 2/3 | train_loss=0.6936 | test_loss=0.6102 | test_acc=0.6500
  - Epoch 3/3 | train_loss=0.6078 | test_loss=0.5564 | test_acc=0.7400

## Cách nộp bài
Sinh viên nộp lại toàn bộ project sau khi đã chạy xong, bao gồm:
- README đã cập nhật thông tin máy và kết quả chạy
- requirements.txt
- check_env.py
- run_smoke_test.py
- config
- toàn bộ thư mục outputs
- ảnh chụp màn hình terminal hoặc output thành công

## Sinh viên cần cập nhật README này
- Họ tên: Nguyễn Việt Chung
- MSSV:1771040005
- Lớp:KHMT17-01
- Hệ điều hành: Windows 11
- Python version: 3.13.5
- Torch version: 2.11.0+cpu
- Thiết bị chạy: CPU
- Ghi chú lỗi gặp phải khi setup (nếu có): Không có lỗi
