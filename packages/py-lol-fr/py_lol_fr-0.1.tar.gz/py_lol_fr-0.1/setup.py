from setuptools import setup, find_packages

setup(
    name="py_lol_fr",
    version="0.1",
    description="Un package qui permet l'utilisation simplifié de l'api de League of Legends",
    author="Manolo",
    author_email="emmanuelar.pro@gmail.com",
    packages=find_packages(),
    url="https://github.com/Manoleau/py_lol",
    install_requires=[
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
)
