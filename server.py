import http.server
import os
import socketserver
import sys
import threading
import webbrowser

PORT = 8000
ROOT = os.path.dirname(os.path.abspath(__file__))
URL = f"http://127.0.0.1:{PORT}/index.html"


class Server(socketserver.TCPServer):
    allow_reuse_address = True


def open_browser():
    webbrowser.open(URL)


os.chdir(ROOT)

try:
    httpd = Server(("127.0.0.1", PORT), http.server.SimpleHTTPRequestHandler)
except OSError:
    # 端口已被占用，说明服务可能已经在运行，直接打开页面
    webbrowser.open(URL)
    sys.exit(0)

threading.Timer(1.0, open_browser).start()
print(f"照片墙已启动：{URL}")
print("关闭这个窗口，图片就看不到了。")
sys.stdout.flush()

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
