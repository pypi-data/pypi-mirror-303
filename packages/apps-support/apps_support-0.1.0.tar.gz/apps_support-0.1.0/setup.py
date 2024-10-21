# Импортируем модули:
from setuptools import setup, find_packages
# Главный код:
setup(
    name='apps_support',  # Имя вашей библиотеки
    version='0.1.0',     # Версия библиотеки
    packages=find_packages(),
    install_requires=[    # Список зависимостей
        # 'package-name',
    ],
    author='fhghfhfhfh',
    author_email='maxim.parkhomenko@internet.ru',
    description='Простая библиотека для MaxOS',
    long_description=open('README.md').read(),  # Длинное описание
    long_description_content_type='text/markdown',
    # url='https://github.com/yourusername/your-library',  # URL к проекту
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',  # Минимальная версия Python
)