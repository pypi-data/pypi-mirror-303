from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent

with open('requirements.txt') as f:
    required_packages = f.read().splitlines()

setup(
    name='panzer',
    version='1.0.9',
    author='nand0san',
    author_email='',
    description='REST API manager for Binance API. Manages weights and credentials simply and securely.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/nand0san/panzer',  # Asegúrate de poner la URL correcta
    packages=find_packages(),
    include_package_data=True,  # Asegura que se respete MANIFEST.in
    install_requires=required_packages,

    classifiers=[
        'Development Status :: 3 - Alpha',  # 3 - Alpha/4 - Beta/5 - Production/Stable
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',  # Asegúrate de especificar las versiones que soporta
        # 'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',  # Asegúrate de especificar la versión de Python necesaria
    package_data={
        # Si hay datos como .json o .txt que necesitas incluir, especifica aquí
    },
    exclude_package_data={'': ['*.ipynb', '*.ipynb_checkpoints/*']},  # Exclusión de notebooks y checkpoints
)
