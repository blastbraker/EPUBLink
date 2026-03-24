from setuptools import setup

setup(
    name="epubbridge",
    version="0.1",
    packages=["epubbridge"],
    install_requires=[
        "flask",
        "qrcode"
    ],
    entry_points={
        "console_scripts": [
            "epubbridge=epubbridge.cli:main"
        ]
    },
    author="Ali",
    description="Send EPUB files from Windows to iPhone over Wi-Fi",
    url="https://github.com/yourusername/epubbridge",
    license="MIT"
)
