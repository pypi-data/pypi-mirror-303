import os
import sys

import socket
from socketserver import TCPServer
from http.server import SimpleHTTPRequestHandler as RH
from http.server import HTTPServer
import ssl

from .INI import readini

class __EnhancedHTTPRequestHandler(RH):
    @staticmethod
    def get_default_extensions_map():
        """
        返回提供文件的默认 MIME 类型映射
        """

        extensions_map = readini(os.path.join(os.path.dirname(__file__), "extensions_map.ini"))["default"]
        # 这里的路径问题就得这么写, 不能直接用相对路径, 不然经过多脚本接连调用后会报错
        # FileNotFoundError: [Errno 2] No such file or directory: 'extensions_map.ini'

        return extensions_map

    def __init__(self, *args, **kwargs):
        self.extensions_map = self.get_default_extensions_map()
        super().__init__(*args, **kwargs)

    def do_GET(self):
        path = self.translate_path(self.path)
        if os.path.isfile(path):
            file_size = os.path.getsize(path)

            fpath, filename = os.path.split(path)
            basename, extension = os.path.splitext(filename)
            self.send_response(200)
            self.send_header("Content-Type", self.extensions_map.get(extension, "application/octet-stream") + "; charset=utf-8")

            # 设置Content-Disposition头，使得文件被下载
            self.send_header("Content-Disposition", f'attachment')
            self.send_header("Content-Length", str(file_size))

            self.end_headers()
            # 现在发送文件数据
            with open(path, 'rb') as file:
                self.wfile.write(file.read())
        else:
            super().do_GET()


    def send_head(self):
        path = self.translate_path(self.path)
        f = None
        if os.path.isdir(path):
            if not self.path.endswith('/'):
                # redirect browser - doing basically what apache does
                self.send_response(301)
                self.send_header("Location", self.path + "/")
                self.end_headers()
                return None
            for index in "index.html", "index.htm":
                index = os.path.join(path, index)
                if os.path.exists(index):
                    path = index
                    break
            else:
                return self.list_directory(path)
        ctype = self.guess_type(path)
        # Add charset=UTF-8 for text files
        if ctype.startswith('text/'):
            ctype += '; charset=UTF-8'
        try:
            # Always read in binary mode. Opening files in text mode may cause
            # newline translations, making the actual size of the content
            # transmitted *less* than the content-length!
            f = open(path, 'rb')
        except IOError:
            self.send_error(404, "File not found")
            return None
        self.send_response(200)
        self.send_header("Content-type", ctype)
        fs = os.fstat(f.fileno())
        self.send_header("Content-Length", str(fs[6]))
        self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
        self.end_headers()
        return f

def Fileserver(path: str = ".", res: str = "", port: int = 5001,
                bool_https: bool = False, certfile="cert.pem", keyfile="privkey.pem"):
    """
    快速构建文件服务器，默认使用 HTTP

    :param path: 工作目录(共享目录路径)
    :param res: IP 默认为本地计算机的IP地址
    :param port: 端口 默认为5001
    :param bool_https: 是否启用HTTPS，默认为False
    :param certfile: SSL证书文件路径，默认同目录下的cert.pem
    :param keyfile: SSL私钥文件路径，默认同目录下的privkey.pem
    :return: None
    """

    if not res:
        res = socket.gethostbyname_ex(socket.gethostname())[-1][-1]

    if bool_https:
        httpd = HTTPServer((res, port), __EnhancedHTTPRequestHandler)
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile, keyfile)
        httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
        print(f"HTTPS running at https://{res}:{port}")
    else:
        httpd = TCPServer((res, port), __EnhancedHTTPRequestHandler)
        print(f"HTTP running at http://{res}:{port}")

    os.chdir(path)  # 设置工作目录作为共享目录路径
    httpd.serve_forever()