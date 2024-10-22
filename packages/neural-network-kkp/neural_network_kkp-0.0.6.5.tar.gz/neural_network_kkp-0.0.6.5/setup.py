from setuptools import setup, find_packages

setup(
    name="neural_network_kkp",
    version="0.0.6.5",
    author="Тихонов Иван",
    author_email="tihonovivan737@gmail.com",
    description="Простая библиотека для полносвязных нейронных сетей",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "numpy",
    ],
)