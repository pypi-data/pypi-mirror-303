from setuptools import setup, find_packages

setup(
    name='excel_to_json_converter',
    version='0.1.0',
    author='Ksr小熙',
    author_email='',
    description='A simple library to convert Excel sheets to JSON format by Ksr小熙',
    # long_description=open('D:\excel_to_json_converter\README.md').read(),
    # long_description_content_type='text/markdown',
    url='https://github.com/Future0537/Ksr_SHARE/tree/main/excel_to_json_converter',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
