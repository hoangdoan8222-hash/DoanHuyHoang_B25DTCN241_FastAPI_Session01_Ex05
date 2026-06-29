from fastapi import FastAPI

app = FastAPI()

@app.get("/students")
def get_students():
    return {"message": "Danh sách sinh viên"}

@app.get("/students/detail")
def get_student_detail():
    return {"message": "Chi tiết sinh viên"}

@app.post("/students")
def create_student():
    return {"message": "Thêm sinh viên thành công"}

@app.put("/students/update")
def update_student():
    return {"message": "Cập nhật sinh viên thành công"}

@app.delete("/students/delete")
def delete_student():
    return {"message": "Xóa sinh viên thành công"}

@app.get("/students/statistics")
def student_statistics():
    return {"message": "Thống kê sinh viên"}

@app.get("/students/active")
def active_students():
    return {"message": "Danh sách sinh viên đang học"}

@app.get("/students/top")
def top_students():
    return {"message": "Danh sách sinh viên nổi bật"}

# Tạo các endpoint theo đúng HTTP method.
# Đặt tên endpoint rõ ràng, dễ hiểu.
# Mỗi endpoint có một hàm xử lý riêng.
# Trả về response có thông báo rõ ràng.
# Bổ sung 2 endpoint mở rộng: /students/active và /students/top.