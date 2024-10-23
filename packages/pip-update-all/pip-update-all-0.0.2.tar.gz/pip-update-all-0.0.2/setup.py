from setuptools import setup, find_packages


setup(
    name='pip-update-all',
    version='0.0.2',
    author='SurivZ',
    author_email='franklinserrano23@email.com',
    description='Paquete para actualizar todos los paquetes instalados con pip',
    long_description=open('./readme.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/SurivZ/pip-update-all',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'update = source:main',
        ],
    },
)