from setuptools import setup, find_packages

setup(
    name="fancyutil",
    version="0.0.1",
    author="Taireru LLC",
    author_email="tairerullc@gmail.com",
    description="A package designed to add a little fancy untility functions and make your life better.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/TaireruLLC/fancyutil",
    packages=find_packages(),
    install_requires=[
        "altcolor",
        "mutagen"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
