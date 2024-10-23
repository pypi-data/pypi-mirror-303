from setuptools import setup, find_packages

setup(
    name='wai_cli',  # Название пакета
    version='0.1',  # Версия пакета
    packages=find_packages(),  # Находит все подпакеты
    install_requires=[],  # Зависимости
    entry_points={
        'console_scripts': [
            'wai=wai_cli.main:main',  # Команда, которая будет доступна в терминале
        ],
    },
)