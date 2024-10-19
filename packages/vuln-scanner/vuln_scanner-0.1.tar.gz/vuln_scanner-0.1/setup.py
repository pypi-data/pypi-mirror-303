from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='vuln_scanner',
    version='0.1',
    author='ALMHEB',
    author_email='appasqw107@gmail.com',
    description='مكتبة للكشف عن ثغرات XSS، SQL Injection، LFI، و RFI',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AL-MHIB',  
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)