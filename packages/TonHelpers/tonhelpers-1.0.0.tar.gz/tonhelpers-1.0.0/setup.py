from setuptools import setup 

setup(
        name = 'TonHelpers',
        version = '1.0.0',
        author = 'Eriton Gomes De Souza',
        author_email = 'eriton.gomes.souza@gmail.com',
        packages = ['TonHelpers'],
        description = 'Funções denomidas Helpers para ajudar da otimização',
        long_description = 'Funções denomidas Helpers para ajudar da otimização',
        url = 'https://github.com/yanorestes/aluratemp',
        project_urls = { 'Código fonte': 'https://github.com/yanorestes/aluratemp',
        'Download': 'https://github.com/yanorestes/aluratemp/archive/1.0.0.zip' },
        license = 'MIT',
        keywords = 'Função otimização',
    #     classifiers = [
    #     'Development Status :: 5 - Production/Stable',
    #     'Intended Audience :: Developers',
    #     'License :: OSI Approved :: MIT License',
    #     'Natural Language :: Portuguese (Brazilian)',
    #     'Operating System :: OS Independent',
    #     'Topic :: Software Development :: Internationalization',
    #     'Topic :: Scientific/Engineering :: Physics'
    # ],
        install_requires = [
        "requests>=2.25.1",
        "numpy",
        "pandas",
        "pytest==8.3.3"
    ],
        # extras_require={
        #     "dev": ["pytest>=6.0", "black"],  # Dependências adicionais para desenvolvimento
        #     "docs": ["sphinx>=3.0", "mkdocs"],  # Dependências para documentação
        # },
        python_requires = '>=3.6'
    )