from setuptools import setup, find_packages
import structmsig as pkg

setup(
    name=pkg.__name__,
    version=pkg.__version__,
    description=pkg.__description__,
    author=pkg.__author__,
    author_email=pkg.__author_email__,
    url=pkg.__url__,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        "ecdsa>=0.19.0",
        "pydantic>=2.9.2",
        "pyOpenSSL>=24.2.1"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # 定義支持的 Python 版本
)