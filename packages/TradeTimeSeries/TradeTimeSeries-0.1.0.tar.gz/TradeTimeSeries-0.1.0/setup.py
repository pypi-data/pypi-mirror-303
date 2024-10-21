from setuptools import setup, find_packages
from pathlib import Path

# Leer el archivo README.md para la descripción larga
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# Leer el archivo requirements.txt para obtener las dependencias
with open('requirements.txt') as f:
    required_packages = f.read().splitlines()

setup(
    name='TradeTimeSeries',
    version='0.1.0',
    description='Manage exchange time series.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='nand0san',
    # author_email='tuemail@example.com',
    url='https://github.com/nand0san/TradeTimeSeries',
    packages=find_packages(),
    install_requires=required_packages,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    exclude_package_data={'': ['*.ipynb', '*.ipynb_checkpoints/*']},  # Exclusión de notebooks y checkpoints
)
