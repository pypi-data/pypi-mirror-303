from setuptools import setup, find_packages

setup(
    name="proj_pacote_processamento",  # Nome do pacote baseado no nome do projeto
    version="0.1",  # Versão do pacote
    description="Pacote para processamento de imagens",
    author="Renan Azevedo",
    author_email="renanazevedoofc_msc@outlook.com",
    packages=find_packages(),  # Encontrar automaticamente os pacotes
    install_requires=[
        'numpy',  # Dependências do projeto
        'matplotlib',
        'scikit-image',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Requer Python 3.6 ou superior
)
