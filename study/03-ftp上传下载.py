# _*_ coding:utf-8 _*_
#下载
#怎么完成下载
#	1.创建一个空新文件
#	2.向里面写数据
#	3.关闭
from socket import *
import struct
def downlop():
	'''下载数据过程分三部
		1.客户端发送数据请求包
		2.服务器收到数据请求包，发送数据
		3.确定数据收到，发送确认数据到服务器上

		步聚循环直到数据发送完成
	'''
	#ip=input("请输入服务器IP：")
	ip='192.168.2.174'
	#以UDP
	udpSocket=socket(AF_INET,SOCK_DGRAM)
	#绑定
	#ip=udpSocket.bind(ip,69)
	#请求包
	sendaddr=(ip,69)
	print (sendaddr)
	try:
		sendData=struct.pack("!H8sb5sb",1,b"test.jpg",0,b"octet",0)
		#发送请求包到服务器上
		udpSocket.sendto(sendData,sendaddr)
		print ("-----------------")
		#如果服务器上接收到信息，给客户端发一信息
		recvData,recvadrr=udpSocket.recvfrom(1024)
		print (recvData)
		print (recvadrr)
	except Exception as e:
		print (e)
	num=0
	while True:
	
		#如果服务器上接收到信息，给客户端发一信息,客户端会接收一条信息其内容形式为元组
		recvData,recvadrr=udpSocket.recvfrom(1024)	
		recvDatalen=len(recvData)
		print(recvDatalen)
		#收到服务器上发送数据后要解数包
		resultTuple=struct.unpack("!HH",recvData[:4])
		#第0位是操作码，第1位是编号
		czNum=resultTuple[0]
		bhNum=resultTuple[1]
		
		print (czNum)
		#当操作码值为1表示下载，2表示上传,3表示发送的数据包，4表示确定收到数据，5表示出错
		if czNum==3:#是否为数据包
			#判断包编码是否是第一次接收数据
			if bhNum==1:
				#第一次接收数据创建文件,并以追加的模式打开
				filename=open("test.jpg","ba")
			#把数据写入文件
			print (recvData[4:])
			filename.write(recvData[4:])
			
			#数据包表示收到数所
			sendData=struct.pack("!HH",4,bhNum)

			#向服务器发数据表示收到,第二个参数表接收服务器的地址
			#原因：向服务器确定收数据必须是服务器发送过来数据的ip和端口
			udpSocket.sendto(sendData,recvadrr)

			if recvDatalen<516:
				filename.close()
				print("下载完成")
				break

		elif czNum==5:
			print("下载出错,错误的编号：%s"%bhNum)
			break

	udpSocket.close()


def uploap():
	'''
	上传文件步聚
	1.打开文件
	2.读取文件
	3.上传文件
	'''
	#filen=input("请输入要上传的文件名：")
	filen='test.txt'
	ip='192.168.2.174'
	#以UDP
	udpSocket=socket(AF_INET,SOCK_DGRAM)
	#绑定
	#ip=udpSocket.bind(ip,69)
	#请求包
	sendaddr=(ip,69)
	print (sendaddr)
	try:
		filename=open(filen,'rb')
		sendData=struct.pack("!H8sb5sb",2,filen.encode("utf-8"),0,b"octet",0)
		#发送请求包到服务器上
		udpSocket.sendto(sendData,sendaddr)
		revcData,recvadrr=udpSocket.recvfrom(1024)
		print("___________22__")
		print (recvadrr)
	except Exception as e:
		print (e)
	num=0
	reaNum=0
	while True:
		#读文件
		readData=filename.read(512)
		print (readData)
		if readData==b'':
			reaNum+=1
			if reaNum>1:
				break
		#如果服务器上接收到信息，给客户端发一信息,客户端会接收一条信息其内容形式为元组
		sendData=struct.pack("!HH",3,num)+readData
		try:
			udpSocket.sendto(sendData,recvadrr)
			recvDatalen=len(readData)
			revcData,recvadrr=udpSocket.recvfrom(1024)
			#收到服务器上发送数据后要解数包
			resultTuple=struct.unpack("!HH",revcData[:4])
			#第0位是操作码，第1位是编号
			czNum=resultTuple[0]
			bhNum=resultTuple[1]
		
			print (revcData,num,bhNum,recvadrr,czNum)
			#当操作码值为1表示下载，2表示上传,3表示发送的数据包，4表示确定收到数据，5表示出错
			if reaNum>1 or recvDatalen<512:
				print("上传完成")
				break

			# elif czNum==5:
			# 	print("上传出错,错误的编号：%s"%bhNum)
			# 	break
		except Exception as e:
			print (e)
		print (num)
		num+=1

	print ("---------------333----------")
	#filename.close()
	udpSocket.close()



if __name__=='__main__':
	print("-------------------1------------------------")
	#downlop()
	uploap()

#疑问：用的一个TFTP服务端工具，在上传数据小512是会出向服务器再次发一次空包，服务器状态才是成功
#否则为失败，当成功以后传数文件为空，



