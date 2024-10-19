from setuptools import setup, find_packages

setup(
    name="single-kan",
    version="0.2.0",
    author="Zhijie Chan",
    author_email="zhijiechencs@gmail.com",
    description="Python libaray for SKAN (Single-parameterized KAN)",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/chikkkit/SKAN",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        # 'numpy',
        # 'requests',
    ],
)