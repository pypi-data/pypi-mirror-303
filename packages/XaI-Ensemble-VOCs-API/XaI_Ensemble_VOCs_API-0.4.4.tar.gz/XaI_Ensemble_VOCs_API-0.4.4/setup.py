from setuptools import setup, find_packages

#para atualizar a biblioteca
#python setup.py sdist bdist_wheel
#twine upload dist/*

setup(
    name='XaI_Ensemble_VOCs_API',  # Replace with your package’s name
    version='0.4.4',# Atualize a versão aqui
    packages=find_packages(),
    install_requires=[
        'lime==0.1.1.37',
        'shap==0.46.0',
        'seaborn==0.13.2',
        'plotly',
        'tensorflow',
        'wheel'
    ],
    author='Michael Lopes Bastos',  
    author_email='mlb@cin.ufpe.br',
    description='A library for do the explaination of data using a new ensenble of XAI methods',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # License type
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)