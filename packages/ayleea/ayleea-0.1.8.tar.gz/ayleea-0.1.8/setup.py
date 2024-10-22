from setuptools import setup, find_packages

setup(
    name='ayleea',  # 包的名字
    version='0.1.8',  # 版本号
    author='Ayleea',  # 作者信息
    author_email='zshigerc@163.com',  # 作者邮箱
    description='An Tools Package',  # 简短描述
    long_description=open('README.md').read(),  # 长描述（通常从 README 文件中读取）
    long_description_content_type='text/markdown',  # 长描述的内容类型
    # url='https://github.com/yourusername/my_package',  # 项目的主页
    packages=find_packages(),  # 自动发现项目中的所有包
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',  # 最低 Python 版本要求
    install_requires=[
        # 'numpy','opencv-python'
    ],
)
