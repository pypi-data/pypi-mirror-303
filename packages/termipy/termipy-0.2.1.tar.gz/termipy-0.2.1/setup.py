from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='termipy',
    version='0.2.1',
    author='Pratik Kumar',
    author_email='pr2tik1@gmail.com',
    description='A versatile command-line shell with system monitoring capabilities',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/pr2tik1/termipy',
    packages=find_packages(include=['termipy', 'termipy.*']),
    install_requires=[
        'psutil',
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'termipy=termipy.main:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    extras_require={
        'test': [
            'pytest>=6.2.5',
            'pytest-cov>=2.12.1',
        ],
    },
)