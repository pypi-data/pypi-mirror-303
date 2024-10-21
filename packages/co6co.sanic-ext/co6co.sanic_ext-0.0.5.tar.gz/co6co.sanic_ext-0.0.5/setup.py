from setuptools import setup, find_packages

'''
作为发布包， 主目录下[co6co_sanic_ext],不能依赖其他第三方包，否则安装时会找不到依赖第三方包
'''
import co6co_sanic_ext
VERSION = co6co_sanic_ext.__version__

# read readmeFile contents
from os import path
currentDir = path.abspath(path.dirname(__file__))
with open(path.join(currentDir, 'README.md'), encoding='utf-8') as f: long_description = f.read()


setup(
    name="co6co.sanic_ext",
    version=VERSION,
    description="web 扩展",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[ "Programming Language :: Python :: 3", "Programming Language :: Python :: 3.6" ],
    include_package_data=True, zip_safe=True,
    #依赖哪些模块
    install_requires=["co6co","co6co.db-ext", "sanic","sanic-ext"],
    #package_dir= {'utils':'src/log','main_package':'main'},#告诉Distutils哪些目录下的文件被映射到哪个源码
    author='co6co',
    author_email ='co6co@qq.com',
    url="http://github.com/co6co",
    data_file={
        ('',"*.txt"),
        ('',"*.md"),
    },
    package_data={
        '':['*.txt','*.md'],
        'bandwidth_reporter':['*.txt']
    }
)