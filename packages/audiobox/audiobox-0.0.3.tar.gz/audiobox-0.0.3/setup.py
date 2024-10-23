from setuptools import setup, find_packages

setup(
    name="audiobox",
    version="0.0.3",
    author="Taireru LLC",
    author_email="tairerullc@gmail.com",
    description="AudioBox allows the user to play music and sound effects on any platform as long as you have the files.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/TaireruLLC/audiobox",
    packages=find_packages(),
    install_requires=[
        "requests",
        "cryptography",
        "altcolor>=0.0.2"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    license="MIT",
)
