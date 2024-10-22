from setuptools import setup, find_packages

setup(
    name='rgb2hex',
    version='0.1.0.dev1023',
    author='Web Tech Moz',
    author_email='zoidycine@gmail.com',
    description='A simple Python library for converting between Hexadecimal and RGB color formats',
    long_description=open('README.md', 'r', encoding='UTF-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/webtechmoz/rgb2hex.git',
    packages=find_packages(),
    keywords=['hex2rgb', 'rgb2hex', 'rgbtohexadecimal', 'hex-to-rgb', 'rgbhex'],
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)