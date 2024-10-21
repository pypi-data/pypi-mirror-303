from setuptools import setup, find_packages

setup(
    name='latex_generator_example',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[], 
    author='Alexnadr Kozhevnikov',
    author_email='alexandr.kozhevnikov8@yandex.ru',
    description='Библиотека для генерации LaTeX таблиц и изображений.',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)