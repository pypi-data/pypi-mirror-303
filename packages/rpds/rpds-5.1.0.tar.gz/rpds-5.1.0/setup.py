from setuptools import setup, find_packages

setup(
    name="rpds",
    version="5.1.0",
    author="Guispark",
    author_email="xfiltrer@protonmail.com",
    description="PoC",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/guispark",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        # Dependências do seu pacote, se houver:
        # 'requests',
    ],
)
