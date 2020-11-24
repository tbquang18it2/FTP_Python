# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finalui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from ftplib import FTP
import re
import sys
import tkinter as tk
from tkinter import filedialog 

class Ui_MainWindow(object):
	def __init__(self):
		self.IP = None
		self.Name_User = None
		self.Password_User = None
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(600, 600)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")

		#Màn hình hiển thị kết quả
		self.areadisplay = QtWidgets.QTextEdit(self.centralwidget)
		self.areadisplay.setGeometry(QtCore.QRect(39, 60, 541, 221))
		self.areadisplay.setObjectName("areadisplay")
		#ô nhập tên folder mới
		self.edtcreatefoldel = QtWidgets.QTextEdit(self.centralwidget)
		self.edtcreatefoldel.setGeometry(QtCore.QRect(140, 330, 121, 31))
		self.edtcreatefoldel.setObjectName("edtcreatefoldel")
		#nút tạo folder mới
		self.btncreatefolder = QtWidgets.QPushButton(self.centralwidget)
		self.btncreatefolder.setGeometry(QtCore.QRect(270, 330, 61, 31))
		self.btncreatefolder.setObjectName("btncreatefolder")
		self.btncreatefolder.clicked.connect(self.addfolder)
		#self.btncreatefolder.clicked.connect(self.createFolder)
		#label
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(40, 330, 111, 31))
		self.label.setObjectName("label")
		#nút kết nối server
		self.btninfoserver = QtWidgets.QPushButton(self.centralwidget)
		self.btninfoserver.setGeometry(QtCore.QRect(50, 290, 111, 31))
		self.btninfoserver.setObjectName("btninfoserver")
		#label
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(40, 20, 21, 16))
		self.label_2.setObjectName("label_2")
		#ô nhập ip
		self.ip = QtWidgets.QTextEdit(self.centralwidget)
		self.ip.setGeometry(QtCore.QRect(60, 10, 121, 31))
		self.ip.setObjectName("ip")
		#label
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(190, 20, 47, 13))
		self.label_3.setObjectName("label_3")
		#ô nhập tên
		self.name = QtWidgets.QTextEdit(self.centralwidget)
		self.name.setGeometry(QtCore.QRect(240, 10, 141, 31))
		self.name.setObjectName("name")
		#label
		self.label_4 = QtWidgets.QLabel(self.centralwidget)
		self.label_4.setGeometry(QtCore.QRect(390, 20, 41, 16))
		self.label_4.setObjectName("label_4")
		#ô nhập pass
		self.password = QtWidgets.QTextEdit(self.centralwidget)
		self.password.setGeometry(QtCore.QRect(433, 10, 121, 31))
		self.password.setObjectName("password")
		#label
		self.label_5 = QtWidgets.QLabel(self.centralwidget)
		self.label_5.setGeometry(QtCore.QRect(40, 380, 111, 16))
		self.label_5.setObjectName("label_5")
		#ô nhập tên folder cần chuyển đến
		self.edtmovetofolder = QtWidgets.QTextEdit(self.centralwidget)
		self.edtmovetofolder.setGeometry(QtCore.QRect(140, 370, 121, 31))
		self.edtmovetofolder.setObjectName("edtmovetofolder")
		#nút chuyển folder
		self.btnmovetofolder = QtWidgets.QPushButton(self.centralwidget)
		self.btnmovetofolder.setGeometry(QtCore.QRect(270, 370, 61, 31))
		self.btnmovetofolder.setObjectName("btnmovetofolder")
		self.btnmovetofolder.clicked.connect(self.movetofolder)
		#thông tin folder hiện tại
		self.btninforfolder = QtWidgets.QPushButton(self.centralwidget)
		self.btninforfolder.setGeometry(QtCore.QRect(180, 290, 111, 31))
		self.btninforfolder.setObjectName("btninforfolder") 
		self.btninforfolder.clicked.connect(self.inforfolder)       
		#nút chuyển về folder trước đó
		self.btnreturnfolder = QtWidgets.QPushButton(self.centralwidget)
		self.btnreturnfolder.setGeometry(QtCore.QRect(440, 290, 111, 31))
		self.btnreturnfolder.setObjectName("btnreturnfolder")
		self.btnreturnfolder.clicked.connect(self.returnfolder)
		#label
		self.label_6 = QtWidgets.QLabel(self.centralwidget)
		self.label_6.setGeometry(QtCore.QRect(340, 330, 111, 31))
		self.label_6.setObjectName("label_6")
		#ô nhaajpp folder cần xóa
		self.edtdeletefolder = QtWidgets.QTextEdit(self.centralwidget)
		self.edtdeletefolder.setGeometry(QtCore.QRect(390, 330, 121, 31))
		self.edtdeletefolder.setObjectName("edtdeletefolder")
		# nút xóa folder
		self.btndeletefolder = QtWidgets.QPushButton(self.centralwidget)
		self.btndeletefolder.setGeometry(QtCore.QRect(520, 330, 71, 31))
		self.btndeletefolder.setObjectName("btndeletefolder")
		self.btndeletefolder.clicked.connect(self.deletefolder)
		#label
		self.label_7 = QtWidgets.QLabel(self.centralwidget)
		self.label_7.setGeometry(QtCore.QRect(340, 380, 101, 16))
		self.label_7.setObjectName("label_7")
		#nút ô nhập tên file cần xóa
		self.edtdeletefile = QtWidgets.QTextEdit(self.centralwidget)
		self.edtdeletefile.setGeometry(QtCore.QRect(390, 370, 121, 31))
		self.edtdeletefile.setObjectName("edtdeletefile")

		#label
		self.label_8 = QtWidgets.QLabel(self.centralwidget)
		self.label_8.setGeometry(QtCore.QRect(40, 420, 101, 16))
		self.label_8.setObjectName("label_8")
		#   ô nhập tên cũ
		self.edtoldname = QtWidgets.QTextEdit(self.centralwidget)
		self.edtoldname.setGeometry(QtCore.QRect(210, 410, 111, 31))
		self.edtoldname.setObjectName("edtoldname")
		#ô nhập tên mới
		self.edtnewname = QtWidgets.QTextEdit(self.centralwidget)
		self.edtnewname.setGeometry(QtCore.QRect(390, 410, 121, 31))
		self.edtnewname.setObjectName("edtnewname")
		#label
		self.label_9 = QtWidgets.QLabel(self.centralwidget)
		self.label_9.setGeometry(QtCore.QRect(150, 420, 61, 16))
		self.label_9.setObjectName("label_9")
		self.label_10 = QtWidgets.QLabel(self.centralwidget)
		self.label_10.setGeometry(QtCore.QRect(330, 420, 71, 16))
		self.label_10.setObjectName("label_10")
		#nút đổi tên
		self.btnrename = QtWidgets.QPushButton(self.centralwidget)
		self.btnrename.setGeometry(QtCore.QRect(520, 410, 75, 31))
		self.btnrename.setObjectName("btnrename")
		self.btnrename.clicked.connect(self.rename)
		#nút xóa file
		self.btndeletefile = QtWidgets.QPushButton(self.centralwidget)
		self.btndeletefile.setGeometry(QtCore.QRect(520, 370, 75, 31))
		self.btndeletefile.setObjectName("btndeletefile")
		self.btndeletefile.clicked.connect(self.deletefile)

		self.edtup_downfile = QtWidgets.QTextEdit(self.centralwidget)
		self.edtup_downfile.setGeometry(QtCore.QRect(150, 450, 251, 31))
		self.edtup_downfile.setObjectName("edtup_downfile")

		self.btnupload = QtWidgets.QPushButton(self.centralwidget)
		self.btnupload.setGeometry(QtCore.QRect(510, 450, 81, 31))
		self.btnupload.setObjectName("btnupload")
		self.btnupload.clicked.connect(self.uploadfile)

		self.btndownload = QtWidgets.QPushButton(self.centralwidget)
		self.btndownload.setGeometry(QtCore.QRect(270, 500, 91, 31))
		self.btndownload.setObjectName("btndownload")
		self.btndownload.clicked.connect(self.downloadfile)

		self.btnquit = QtWidgets.QPushButton(self.centralwidget)
		self.btnquit.setGeometry(QtCore.QRect(310, 290, 111, 31))
		self.btnquit.setObjectName("ChooseFile")
		self.btnquit.clicked.connect(self.defquit)

		self.ChooseFile = QtWidgets.QPushButton(self.centralwidget)
		self.ChooseFile.setGeometry(QtCore.QRect(410, 450, 91, 31))
		self.ChooseFile.setObjectName("btnquit")
		self.ChooseFile.clicked.connect(self.defChoosefile)
		self.label_12 = QtWidgets.QLabel(self.centralwidget)
		self.label_12.setGeometry(QtCore.QRect(40, 460, 101, 16))
		self.label_12.setObjectName("label_12")
		self.label_11 = QtWidgets.QLabel(self.centralwidget)
		self.label_11.setGeometry(QtCore.QRect(40, 500, 101, 16))
		self.label_11.setObjectName("label_11")
		self.edtnamefiledownload = QtWidgets.QTextEdit(self.centralwidget)
		self.edtnamefiledownload.setGeometry(QtCore.QRect(150, 500, 104, 31))
		self.edtnamefiledownload.setObjectName("edtnamefiledownload")

		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)


	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Client FTP"))
		self.btncreatefolder.setText(_translate("MainWindow", "Add"))
		self.label.setText(_translate("MainWindow", "Create New Folder"))
		self.btninfoserver.setText(_translate("MainWindow", "Connect Server"))
		self.label_2.setText(_translate("MainWindow", "IP:"))
		self.ip.setText("127.0.0.1")
		self.name.setText("tbquang")
		self.password.setText("12345")
		self.label_3.setText(_translate("MainWindow", "Name: "))
		self.label_4.setText(_translate("MainWindow", "Pass: "))
		self.label_5.setText(_translate("MainWindow", "Move to Folder"))
		self.btnmovetofolder.setText(_translate("MainWindow", "Move"))
		self.btninforfolder.setText(_translate("MainWindow", "Information Folder"))
		self.btnreturnfolder.setText(_translate("MainWindow", "Return Folder"))
		self.label_6.setText(_translate("MainWindow", "Del Folder"))
		self.btndeletefolder.setText(_translate("MainWindow", "Delete Folder"))
		self.label_7.setText(_translate("MainWindow", "Del File"))
		self.label_8.setText(_translate("MainWindow", "Rename Folder/File"))
		self.label_9.setText(_translate("MainWindow", "Old Name: "))
		self.label_10.setText(_translate("MainWindow", "New Name: "))
		self.btnrename.setText(_translate("MainWindow", "Rename"))
		self.btndeletefile.setText(_translate("MainWindow", " Delete File"))
		self.btnupload.setText(_translate("MainWindow", "Upload"))
		self.btndownload.setText(_translate("MainWindow", "Download"))
		self.btnquit.setText(_translate("MainWindow", "Quit"))
		self.ChooseFile.setText(_translate("MainWindow", "Choose File"))
		self.label_12.setText(_translate("MainWindow", "Choose  File UpLoad"))
		self.label_11.setText(_translate("MainWindow", "Name File Download"))


	#Hàm lấy IP 
	def getIP(self):
		ip = self.ip.toPlainText()
		return ip
	def getName(self):
		name = self.name.toPlainText()
		return name
	def getPass(self):
		password = self.password.toPlainText()
		return password
	#Hàm xủ lý nút Connected server
	def Connect(self):
		con = self.btninfoserver.clicked.connect(self.inforserver)
	def inforserver(self):
		ip = ui.getIP()
		user_name = ui.getName()
		password = ui.getPass()
		if user_name == "":
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Warning)
			msg.setText("Warning!!!")
			msg.setInformativeText("Please! Enter your username")
			msg.setWindowTitle("Warning")
			msg.exec_()	
		elif password == "":
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Critical)
			msg.setText("Error!!!")
			msg.setInformativeText("Please! Enter your password")
			msg.setWindowTitle("Error")
			msg.exec_()
		else:
			try:
				ftp_client.connect(ip,21)
				ftp_client.login(user_name,password)
				self.areadisplay.insertPlainText("Connected to Server: "+ftp_client.getwelcome()+"\n")
			except:
				msg = QtWidgets.QMessageBox()
				msg.setIcon(QtWidgets.QMessageBox.Critical)
				msg.setText("Error!!!")
				msg.setInformativeText("Oppp! Something was wrong! Try Again")
				msg.setWindowTitle("Error")
				msg.exec_()
	#Hàm xử lý nút Chọn file
	def defChoosefile(self):
		root = tk.Tk()
		root.withdraw()
		file_path = filedialog.askopenfilename()
		self.edtup_downfile.setText(file_path)
	#Hàm xử lý nút lấy thông tin Folder
	def inforfolder(self):
		try:
			self.areadisplay.insertPlainText("Infor: "+ftp_client.retrlines('LIST')+"\n")
		except:
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Critical)
			msg.setText("Error!!!")
			msg.setInformativeText("Oppp! Something was wrong! Try Again")
			msg.setWindowTitle("Error")
			msg.exec_()

	#Hàm xử lý nút thêm folder
	def addfolder(self):
		name_folder = self.edtcreatefoldel.toPlainText()
		if name_folder == "":
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Critical)
			msg.setText("Error!!!")
			msg.setInformativeText("Please Enter Name Folder")
			msg.setWindowTitle("Error")
			msg.exec_()
		elif bool(re.match('^[a-zA-Z0-9]*$',name_folder))==False:
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Critical)
			msg.setText("Error!!!")
			msg.setInformativeText("Names cannot contain special characters")
			msg.setWindowTitle("Error")
			msg.exec_()
		else:
			try:
				ftp_client.mkd(name_folder)
				ftp_client.cwd(name_folder)
				self.areadisplay.insertPlainText("Created Successfully. The current directory: "+ ftp_client.pwd()+"\n")
				self.edtcreatefoldel.setText("")
			except:
				msg = QtWidgets.QMessageBox()
				msg.setIcon(QtWidgets.QMessageBox.Critical)
				msg.setText("Error!!!")
				msg.setInformativeText("The folder is available or no connection to server!!Please Enter Another Name or Connect to server before performing the operation ")
				msg.setWindowTitle("Error")
				msg.exec_()

	#Hàm xử lý nút xóa folder
	def deletefolder(self):
		name_folder_delete = self.edtdeletefolder.toPlainText()
		if name_folder_delete == "":
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Critical)
			msg.setText("Error!!!")
			msg.setInformativeText("Please Enter Name Folder")
			msg.setWindowTitle("Error")
			msg.exec_()
		else:
			try:
				ftp_client.rmd(name_folder_delete)
				self.areadisplay.insertPlainText("Deleted Successfully "+name_folder_delete+"\n")
				self.edtdeletefolder.setText("")               
			except:
				msg = QtWidgets.QMessageBox()
				msg.setIcon(QtWidgets.QMessageBox.Critical)
				msg.setText("Error!!!")
				msg.setInformativeText("Oppp! Something was wrong! The folder does not exist!")
				msg.setWindowTitle("Error")
				msg.exec_()

	#Hàm xử lý nút xóa file
	def deletefile(self):
		name_file_delete = self.edtdeletefile.toPlainText()
		if name_file_delete == "":
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Critical)
			msg.setText("Error!!!")
			msg.setInformativeText("Please Enter Name Folder")
			msg.setWindowTitle("Error")
			msg.exec_()
		else:
			try:
				ftp_client.delete(name_file_delete)
				self.areadisplay.insertPlainText("Deleted Successfully "+name_file_delete+"\n")
				self.edtdeletefile.setText("")
				
			except:
				msg = QtWidgets.QMessageBox()
				msg.setIcon(QtWidgets.QMessageBox.Critical)
				msg.setText("Error!!!")
				msg.setInformativeText("Oppp! Something was wrong! The file does not exist!")
				msg.setWindowTitle("Error")
				msg.exec_()

	#Hàm xử lý nút kiểm tra file
	def checkfile(self):
		name_file_check = self.edtdeletefile.toPlainText()
		if name_file_check == "":
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Critical)
			msg.setText("Error!!!")
			msg.setInformativeText("Please Enter Name File")
			msg.setWindowTitle("Error")
			msg.exec_()
		else:
			try:
				self.areadisplay.insertPlainText("File Size: "+ftp_client.size(name_file_check)+"\n")
			except:
				msg = QtWidgets.QMessageBox()
				msg.setIcon(QtWidgets.QMessageBox.Critical)
				msg.setText("Error!!!")
				msg.setInformativeText("Oppp! Something was wrong! 550 SIZE not allowed in ASCII mode.")
				msg.setWindowTitle("Error")
				msg.exec_()


	#Hàm xử lý nút đổi tên file            
	def rename(self):
		old_name = self.edtoldname.toPlainText()
		new_name = self.edtnewname.toPlainText()
		if old_name == "" or new_name == "" :
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Warning)
			msg.setText("Warning!!!")
			msg.setInformativeText("Please Enter Name Folder/File")
			msg.setWindowTitle("Warning")
			msg.exec_()
		elif bool(re.match('^[a-zA-Z0-9.]*$',new_name))==False:
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Critical)
			msg.setText("Error!!!")
			msg.setInformativeText("Names cannot contain special characters")
			msg.setWindowTitle("Error")
			msg.exec_()

		else:
			try:
				ftp_client.rename(old_name,new_name)
				self.areadisplay.insertPlainText("Changed successfully from "+old_name+ " to " +new_name+ "\n")
				self.edtoldname.setText(""),
				self.edtnewname.setText("")  
			except:
				msg = QtWidgets.QMessageBox()
				msg.setIcon(QtWidgets.QMessageBox.Critical)
				msg.setText("Error!!!")
				msg.setInformativeText("Oppp! Something was wrong! The file does not exist!")
				msg.setWindowTitle("Error")
				msg.exec_()

	#Hàm xử lý nút chuyển đến folder
	def movetofolder(self):
		name_folder_move = self.edtmovetofolder.toPlainText()
		if name_folder_move == "":
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Warning)
			msg.setText("Warning!!!")
			msg.setInformativeText("Please Enter Name Folder!!")
			msg.setWindowTitle("Warning")
			msg.exec_()
		else:
			try:
				ftp_client.cwd(name_folder_move)
				self.areadisplay.insertPlainText("Successfully moved to the directory. The current directory: "+ftp_client.pwd()+"\n")
				self.edtmovetofolder.setText("")
			except:
				msg = QtWidgets.QMessageBox()
				msg.setIcon(QtWidgets.QMessageBox.Critical)
				msg.setText("Error!!!")
				msg.setInformativeText("Oppp! Something was wrong! The folder does not exist!")
				msg.setWindowTitle("Error")
				msg.exec_()

		
	#Hàm xử lý nút trở về 1 folder trước    
	def returnfolder(self):
		try:
			ftp_client.cwd("..")
			self.areadisplay.insertPlainText("Successfully moved to the directory. The current directory: "+ftp_client.pwd()+"\n")
		except:
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Critical)
			msg.setText("Error!!!")
			msg.setInformativeText("Oppp! Something was wrong!Being in the original folder")
			msg.setWindowTitle("Error")
			msg.exec_()

	#Hàm xử lý nút upload file
	#Điều kiện file upload lên từ client phải ở cùng hoặc sâu hơn vị trí đặt file chạy ftp-client (file code .python) hoặc phải trỏ được đường dẫn chính xác đến vị trí file.
	#Muốn upload đến thư mục nào đó thì thực hiện kết nối đến thư mục đó trên server.
	def uploadfile(self):
		link_file_upload = self.edtup_downfile.toPlainText()
		if link_file_upload == "": 
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Warning)
			msg.setText("Error!!!")
			msg.setInformativeText("Please insert name file need to upload!")
			msg.setWindowTitle("Error")
			msg.exec_()
		else:
			leng = len(link_file_upload)
			chuoi = link_file_upload.split("/")
			for tu in chuoi:
				name_file_upload = tu
			file_upload = open(link_file_upload,"rb") 
			ftp_client.storbinary("{CMD} {FileName}".
				format(CMD="STOR",FileName=name_file_upload),
				file_upload)
			print(file_upload.read()) 
			print(name_file_upload)
			file_upload.close()
			self.edtup_downfile.setText("")
			self.areadisplay.insertPlainText("Uploaded Successfully file: "+name_file_upload+"\n")

	#Hàm xử lý nút downloadfile
	#Muốn download file nào, thực hiện trỏ thư mục server chứa file đó
	#Kết nối vào FTP server folder chứa thư mục và thực hiện download
	def downloadfile(self):
		name_file_download = self.edtnamefiledownload.toPlainText()
		if name_file_download == "":
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Warning)
			msg.setText("Error!!!")
			msg.setInformativeText("Please insert name file need to download!")
			msg.setWindowTitle("Error")
			msg.exec_()
		else:
			try:
				file_path = name_file_download
				file_name = name_file_download
				file_stream = open(file_path,"wb")      
				ftp_client.retrbinary('RETR {}'.format(file_name),
							file_stream.write, 1024)
				file_stream.close() 
				self.areadisplay.insertPlainText("Download Successfully file: "+name_file_download+"\n") 
			except:
				msg = QtWidgets.QMessageBox()
				msg.setIcon(QtWidgets.QMessageBox.Warning)
				msg.setText("Error!!!")
				msg.setInformativeText("Please insert name file need to download!")
				msg.setWindowTitle("Error")
				msg.exec_()

	def defquit(self):
		try:
			ftp_client.quit()
			self.areadisplay.insertPlainText("Closed connection. See you again!!\n") 
		except:
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Critical)
			msg.setText("Error!!!")
			msg.setInformativeText("No connection!!!")
			msg.setWindowTitle("Error")
			msg.exec_()
#Main           

if __name__ == "__main__":
	ftp_client = FTP()
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	MainWindow1 = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	ui.Connect()
	MainWindow.show()
	sys.exit(app.exec_()) 