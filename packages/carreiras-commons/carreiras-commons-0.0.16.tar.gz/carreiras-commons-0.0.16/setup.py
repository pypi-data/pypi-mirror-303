from setuptools import setup

setup(
    name='carreiras-commons',
    version='0.0.16',
    author='HYTI',
    author_email='contato@titcs.com.br',
    packages=['carreiras_commons','carreiras_commons.enum','carreiras_commons.messaging','carreiras_commons.util','carreiras_commons.seguranca','carreiras_commons.seguranca.util'],
    description='Common functions to carreiras projects',
    long_description='Common functions to carreiras projects',
    url='https://dev.azure.com/TITBrasil/Carreiras/_git/CARREIRAS-COMMON',
    project_urls={
        'Código fonte': 'https://TITBrasil@dev.azure.com/TITBrasil/Carreiras/_git/CARREIRAS-COMMON',
        'Download': 'https://TITBrasil@dev.azure.com/TITBrasil/Carreiras/_git/CARREIRAS-COMMON'
    },
    license='MIT',
    keywords='carreiras',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Scientific/Engineering :: Physics'
    ]
)
