from setuptools import setup, find_packages

setup(
    name="MAOuladrocket",
    version="0.1",
    description="A rocket simulation package",
    author="Mohamed lamine OULAD SAID",
    author_email="mohamedamineouledsaid10@gmail.com",
    license="MIT",
    packages=find_packages(),  # Inclut tous les sous-dossiers
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
