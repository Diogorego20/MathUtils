from setuptools import setup, find_packages

setup(
    name='mathutils-pacote',
    version='1.0.0',
    author='Aluno Diogo Da Silva Rego, 20240045381',
    author_email='diogo.rego@exemplo.com',
    description='Um pacote Python simples para funções matemáticas como Fibonacci e Fatorial.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/exemplo/mathutils-pacote',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[],
    extras_require={
        'dev': [
            'pytest>=6.0',
            'check-manifest',
            'twine',
        ]
    },
    entry_points={},
    include_package_data=True,
    zip_safe=False
)


