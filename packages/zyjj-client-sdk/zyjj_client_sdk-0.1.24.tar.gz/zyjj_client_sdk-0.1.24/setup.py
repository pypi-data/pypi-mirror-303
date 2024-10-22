from setuptools import setup, find_packages

setup(
    name='zyjj_client_sdk',
    version='0.1.24',
    description='智游剪辑客户端sdk包',
    url='https://github.com/zyjj-cc/zyjj-client-sdk',
    author='zyjj',
    author_email='zyjj.cc@foxmail.com',
    license='MIT',
    long_description="智游剪辑客户端sdk包",
    packages=find_packages(),
    install_requires=[
        'requests~=2.31.0',
        'paho-mqtt~=1.6.1',
        'cos-python-sdk-v5~=1.9.26',  # 腾讯云cos
        "oss2~=2.19.0",  # 阿里云oss
        'tencentcloud-sdk-python~=3.0.1090',  # 腾讯云SDK
        'graphviz~=0.20.3',  # 绘图
        'tenacity~=9.0.0',  # 重试框架
        'AudioSegment~=0.23.0',  # 音频分割
        'chardet~=5.2.0',  # 编码检测
        'pytest~=8.2.1',  # 单元测试
        'Pillow~=10.4.0',  # 图片处理
        'numpy~=2.0.1',  # numpy
    ]
)
