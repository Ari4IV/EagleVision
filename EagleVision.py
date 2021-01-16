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
        time.sleep(2)

if __name__ == '__main__':
    Process(target=httpserver).start()
    Process(target=EagleVision).start()