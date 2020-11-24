import logging

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Khởi tạo cổng 21 mà máy chủ FTP sẽ lắng nghe.
# Giá trị này phải lớn hơn 1023 trừ khi bạn chạy tập lệnh này dưới dạng thư mục gốc.
FTP_PORT = 21

def main():
    # Khởi tạo trình cấp quyền giả để quản lý người dùng 'ảo'
    authorizer = DummyAuthorizer()

    # Xác định người dùng mới có đầy đủ quyền read / write và chỉ đọc và thư mục gốc cho phép truy cập
    authorizer.add_user("tbquang", "12345", "D:/ki1nam3/LapTrinhMang/DoAn/Account/tbquang", perm="elradfmw")
    authorizer.add_user("tttung", "12345", "D:/ki1nam3/LapTrinhMang/DoAn/Account/tttung", perm="elradfmw")
    # người dùng ẩn danh
    authorizer.add_anonymous("D:/ki1nam3/LapTrinhMang/DoAn/Anonymous_Account")

    # Khởi tạo lớp trình xử lý FTP
    handler = FTPHandler
    handler.authorizer = authorizer

    # Xác định thông báo tùy chỉnh (chuỗi được trả về khi người dùng kết nối tới server)
    handler.banner = "pyftpdlib based ftpd ready."

    logging.basicConfig(filename='D:/ki1nam3/LapTrinhMang/DoAn/Login_Manager/pyftpd.log', level=logging.INFO)

    # Tùy chọn chỉ định phạm vi cổng để sử dụng cho các kết nối thụ động.
    #address = ('127.0.0.1', FTP_PORT)
    #Khởi tạo server
    #server = FTPServer(address, handler)
    server = FTPServer(("127.0.0.1", 21), handler)
    # thiết lập giới hạn kết nối
    server.max_cons = 256
    server.max_cons_per_ip = 5

    server.serve_forever()


if __name__ == '__main__':
    main()