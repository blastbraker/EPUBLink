from setuptools import setup

setup(
    name="epubbridge",
    version="0.1",
    py_modules=["epubbridge"],
    install_requires=[
        "flask",
        "qrcode"
    ],
    entry_points={
        "console_scripts": [
            "epubbridge=epubbridge:main"
        ]
    }
)
