from setuptools import setup, find_packages

setup(
    name="AsyncDFD",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "gevent", 
        "tabulate",
        "tenacity",
    ],
    author="Haoyu Wang",
    author_email="Haoyu_Wang_1103@outlook.com",
    description="A library for async accelerate based on gevent coroutine in python.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/R0k1e/AsyncDFD.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
)