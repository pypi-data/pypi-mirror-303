from setuptools import setup, find_packages

setup(
    name='sthg_fastapi_logs',
    version='0.1.6',
    packages=find_packages(),
    description='Python FastApi logs',
    long_description=open('sthg_fastapi_logs/README.md').read(),
    long_description_content_type='text/markdown',
    author='DongQing',
    author_email='maoyouyu@163.com',
    url='https://github.com/yourusername/your_package_name',
    install_requires=[
        # 依赖项列表
    ],
    classifiers=[
        # 包分类列表，例如：
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)