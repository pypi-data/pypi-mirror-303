from setuptools import setup, find_packages

setup(
    name='XMZAPI',
    version='0.0.1',
    description='米粥API配套SDK',
    long_description='本项目封装了米粥API的所有接口，可以方便的调用米粥API',
    author='祁筱欣',
    author_email='mzapi@x.mizhoubaobei.top',
    url='https://github.com/xiaomizhoubaobei/XMZAPI',
    packages=find_packages(),
    install_requires=[
        'huaweicloudsdkcore',
        'huaweicloudsdknlp',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)