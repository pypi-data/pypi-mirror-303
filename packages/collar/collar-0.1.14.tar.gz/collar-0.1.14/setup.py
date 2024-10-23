from setuptools import setup, find_packages

setup(
    name='collar',  #
    version='0.1.7',  # 版本号
    author='Ding Haitao',
    author_email='dinght1975@gmail.com',
    description='一个利用LLM来一起进行项目开发的工具',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dinght-1975/collar_project',  # 项目主页
    packages=find_packages(),  # 自动查找所有包，排除 Java 项目和测试
    include_package_data=True,  # 包含 MANIFEST.in 指定的文件
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # 选择适合的许可证
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    install_requires=[  # 项目依赖
        'openai',
        'jpype1'
    ],
    entry_points={
        'console_scripts': [
            'collar=collar:main',  # 这里假设你的 collar 模块有一个 main() 函数
        ],
    },
)