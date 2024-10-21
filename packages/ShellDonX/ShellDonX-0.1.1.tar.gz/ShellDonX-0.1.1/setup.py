from setuptools import setup, find_packages

setup(
    name="ShellDonX",  # Your package name
    version="0.1.1",  # Package version
    description="Your project's description here",
    long_description=open('README.md').read(),  # Pulls from README.md
    long_description_content_type='text/markdown',  # This ensures markdown rendering on PyPI
    url="https://github.com/DeadmanXXXII/Shell_Don",  # GitHub repo URL
    author="Deadman",
    author_email="themadhattersplayground@gmail.com",
    license="MIT",  # License type
    packages=find_packages(),  # Automatically finds package folders
    install_requires=[
        # List your dependencies here
        "urllib.parse",
        "html",
        "json",
        "zlib",
        "tkinter",
        "argparse",
        "sys",
        "cryptography",
        "tkinter",
        "setuptools"
        
        # For example, if using Flask: "flask>=2.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11.0",  # Specify the minimum Python version
)
