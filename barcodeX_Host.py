#coding:utf-8

""" 这个是BarcodeX的host服务器端程序，输入查询的字符串，然后将查询的结果通过TCP 发出
"""

import dbi,odbc
#import pypyodbc
#odbc=pypyodbc
import time


import socketserver

import string

def sql_str(str):
    """查询字符串，返回查询结果列表
    """
    '''connect a db'''
    conn = odbc.odbc(  # open a db connect
                 'Driver={Microsoft Access Driver (*.mdb)};DBQ=E:\\workspace\\py_work\\ODBC2003.mdb')
    cur = conn.cursor()  #get a cur
    #sql  define a char as work_no.
    #s=input('please input chars')
    sql='''SELECT *
                FROM IFX
                WHERE 流程卡编号 ='''+"'"+str+"'"
    cur.execute(sql)
    """
    cur.execute('''
                SELECT *
                FROM IFX
                WHERE 流程卡编号 = 'HWZ20140719001914'
                ''')
    """
    print('Column descriptions:')
    for col in cur.description:
        print(' ',col)             #print  table descriptions

    print('查询结果：')
    for d in cur.description:
        print (d[0])

     #print (d[0],end=' ')
    print()
    s=''
    for row in cur.fetchall():
        for field in row:
            #print (field,end=' ')  #this not run in python2.7
            print (field)
            s=s[0]+'|'+s[1] +'|'+s[2]
            print()
    print(s)
    
    #close
    conn.close()
    return s


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data =sql_result #self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        
        # just send back data
        self.request.sendall(self.data)

if __name__ == "__main__":
    sql_result=sql_str('HWZ20140719001914')  #返回查询列表

 
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    MyTCPHandler.data=sql_result
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
        
    server.serve_forever()
