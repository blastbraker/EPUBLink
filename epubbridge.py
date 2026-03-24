import socket
import sys
import qrcode
from flask import Flask, send_file, render_template_string

app = Flask(__name__)
FILE_PATH = None

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>EPUBBridge</title>
</head>
<body style="text-align:center; font-family:sans-serif;">
    <h1>EPUBBridge</h1>
    <p>Your book is ready</p>
    <a href="/download">
        <button style="padding:15px; font-size:18px;">Download EPUB</button>
    </a>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

@app.route('/download')
def download():
    return send_file(FILE_PATH, as_attachment=True)

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def main():
    global FILE_PATH

    if len(sys.argv) < 2:
        print("Usage: epubbridge <file.epub>")
        return

    FILE_PATH = sys.argv[1]

    ip = get_local_ip()
    url = f"http://{ip}:8000"

    print(f"\n Hosted: {url}\n")

    qr = qrcode.make(url)
    qr.print_ascii()

    app.run(host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
