from setuptools import setup, find_packages

setup(
    name='jsonmodeler',
    version='0.1.1',
    description='A tool to convert JSON to model code in various languages',
    long_description=open('README.md', encoding="UTF8").read(),  # 确保 README.md 文件存在
    long_description_content_type='text/markdown',
    author='WenYu',  # 替换为你的名字
    author_email='cn.signal.hugo@gmail.com',  # 替换为你的电子邮件
    url='https://github.com/CN-WenYu/JsonModeler',  # 替换为你的项目 URL
    packages=find_packages(),  # 自动发现所有包
    install_requires=[
        # 在这里列出项目的依赖项，例如：'requests', 'numpy', ...
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    license='MIT',
    python_requires='>=3.5',  # 根据项目要求指定 Python 版本
    entry_points={
        'console_scripts': [
            'jsonmodeler=scripts.convert:main',  # 确保路径和函数名称正确
        ],
    },
)
