# !/usr/bin/python
from setuptools import setup, find_packages

setup(
    name='nta',
    version='1.0.6.dev0',
    url='https://github.com/hwonyo/naver_talk_sdk',
    license='MIT License',
    description='A Python Library For Naver TalkTalk',
    author='wonyoHwang',
    author_email='hollal0726@gmail.com',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        "requests>=2.20.0",
    ],
    keywords=['nta', 'navertalk', 'naver', 'chatbot'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ]
)

