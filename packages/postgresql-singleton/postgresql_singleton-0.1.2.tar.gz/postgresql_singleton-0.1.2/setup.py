from setuptools import setup, find_packages

setup(
    name="postgresql-singleton",
    version="0.1.2",
    packages=find_packages(),
    install_requires=[
        "psycopg2-binary",
    ],
    description="PostgreSQL Singleton connection pool manager",
    author="Song Seung Hwan",
    author_email="shdth117@gmail.com",
    url="https://github.com/alkaline2018/postgresql-singleton",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)