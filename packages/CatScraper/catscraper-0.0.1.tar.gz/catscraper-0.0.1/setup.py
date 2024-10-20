from setuptools import setup, find_packages

setup(
    name='CatScraper',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'Epate'
    ],
    # 其他元数据
    author='KitchenSweeper',
    author_email='xiaoxiaogzs@outlook.com',
    description='CatScraper is a Python library that automates tasks on the Codemao (编程猫) platform, helping users perform repetitive actions like liking, collecting, and more. With its easy-to-use code and customizable functions, CatScraper simplifies workflows and boosts productivity for developers and Codemao users alike.',
    keywords='codemao',
    url='https://github.com/kitswe/CatScraper',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
