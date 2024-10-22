from setuptools import setup, find_packages

setup(
    name='xcloudforlinux',
    version='0.4.3',
    packages=find_packages(),
    package_data={
        'xcloudforlinux': ['resources/*.jar'],
    },
    include_package_data=True,
    install_requires=[
        'JPype1==1.5.0',
        'jinja2==3.1.4'
    ],
    description='这是一个国信行云数据库并发查询python程序,主要应用于自动通报',
    long_description=open('README.md',encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/bailulue',
    author='bailu',
    author_email='yabailu@chinatelecom.cn'
)
