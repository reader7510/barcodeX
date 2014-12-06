#coding:utf-8

import os
import socket
import sys
#import socketserver


def runAutoJob(exe_name,wafer_id,work_no,device_name):
    '''Run AutoJob as comand with args,the args is wafer_id,work_no,device_name
        Send text into AutoJob Edit(Text_box)'''
    s=wafer_id+' '+work_no+' '+device_name
    os.system(exe_name+' '+s)


def receive_str(HOST="localhost", PORT=9999):
    #data = " ".join(sys.argv[1:])  这里接受参数

    # Create a socket (SOCK_STREAM means a TCP socket)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        #sock.sendall(bytes(data + "\n", "utf-8"))
        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
    finally:
        sock.close()
    print("Received: {}".format(received))
    return received


#test code
if __name__=='__main__':
    
    list=receive_str(HOST="localhost", PORT=9999)
    list=list.split('|')
    runAutoJob(r"E:\workspace\BarcodeX\run_args.exe",list[1],list[0],list[2])

   
