# coding=utf-8
from pathlib import Path
from setuptools import setup, find_packages
import os

# with open("README.md", "r",encoding='utf8') as fh:
#     long_description = fh.read()

# filepath = ((Path(__file__).parent / Path('README.md')).absolute()).as_posix()
filepath = 'README.md'
print(filepath)

install_requires = [
    'pymongo>=4.0.2',
    'tomorrow3>=1.1.0',
    'concurrent-log-handler>=0.9.19',
    'elasticsearch',
    'requests',
    'python-json-logger>=0.1.10',
    'nb_filelock',
    'service-identity'
]

if os.name == 'nt':
    install_requires.append('pywin32')

setup(
    name='ga_log',  #
    version="1.2.4",
    description=(
        'fork ga_log '
    ),
    keywords=["logging", "logger", "multiprocess file handler", "color handler"],
    # long_description=open('README.md', 'r',encoding='utf8').read(),
    #long_description_content_type="text/markdown",
    #long_description=open(filepath, 'r', encoding='utf8').read(),
    #url='https://github.com/ydf0509/nb_log',
    # data_files=[filepath],
    author='ziko',
    #author_email='ydf0509@sohu.com',
    maintainer='ziko',
    #maintainer_email='ydf0509@sohu.com',
    license='BSD License',
    packages=find_packages(),
    include_package_data=True,
    platforms=["all"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=install_requires
)
"""
打包上传
python setup.py sdist upload -r pypi



python setup.py sdist & twine upload dist/*
python setup.py sdist & python -m  twine upload dist/ga_log-7.6.tar.gz

twine upload dist/*


python -m pip install ga_log --upgrade -i https://pypi.org/simple   # 及时的方式，不用等待 阿里云 豆瓣 同步
"""
