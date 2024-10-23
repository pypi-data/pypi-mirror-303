from setuptools import setup, find_packages

setup(
    name='mdfa',  # 包的名字
    version='0.1.0',  # 版本号
    packages=find_packages(),  # 自动发现模块
    install_requires=[  # 指定依赖项
        'torch>=1.7.0'
    ],
    author='backy',
    author_email='backywen@163.com',
    description='MDFA: A Multi-Dimensional Feature Attention model',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/your_project',  # 项目的GitHub地址
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
