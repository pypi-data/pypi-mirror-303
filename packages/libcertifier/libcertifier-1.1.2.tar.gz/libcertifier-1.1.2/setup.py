from setuptools import setup, find_packages
 
requirements = [
    'base58==2.1.1',
    'certifi==2024.8.30',
    'cffi==1.17.1',
    'charset-normalizer==3.4.0',
    'cryptography==43.0.1',
    'idna==3.10',
    'packaging==24.1',
    'psutil==6.0.0',
    'requests==2.32.3',
    'requests-toolbelt==1.0.0',
    'setuptools==75.2.0',
    'urllib3==2.2.3'
] 
 
setup(
    name='libcertifier',
    version='1.1.2',
    description='CLI to request xPKI certificates',
    package_dir = {"": "libcertifier"},
    packages=find_packages(where="libcertifier"),
    include_package_data=True,
    author="Russell Benjamin",
    author_email="russell_benjamin@comcast.com",
    license="Apache-2.0",
    install_requires=requirements,
    extras_require={
        "dev":["twine>=5.1.1"]
    },
    entry_points={
        'console_scripts': [
            'libcertifier=src.main:main', 
        ],
    },
)