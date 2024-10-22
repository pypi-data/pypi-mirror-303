from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="conta_bancaria",
    version="0.0.1",
    author="Felipe Dick",
    author_email="example@gmail.com",
    description="Exemplo de empacotamento",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/felipedick/dio-classes/tree/main/5.%20POO/Pacote%20Conta%20Bancaria",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.10',
)

