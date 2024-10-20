from setuptools import setup, find_packages

setup(
    name='MAOuladrocket',
    version='1.0.0',
    author='Mohamed lamine OULAD SAID',
    author_email='mohamedamineouledsaid10@gmail.com',
    packages=find_packages(),  # Trouver automatiquement les packages
    url='http://pypi.python.org/pypi/MAOuladrocket/',
    license='LICENSE.txt',
    description='An awesome package that does something',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=[],  # Si vous avez des dépendances, vous pouvez les lister ici, sinon laissez vide
)

