import sys
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    readme = fh.read()

with open("CHANGELOG.md", "r", encoding="utf-8") as fh:
    changelog = fh.read()

long_description = readme + "\n\n" + changelog

install_requires = [
    'aiosignal',
    'argon2-cffi',
    'argon2-cffi-bindings',
    'arrow',
    'grpcio',
    'keras',
    'h11',
    'httpcore',
    'idna',
    'isoduration',
    'iterators',
    'Jinja2',
    'json5',
    'jsonpointer',
    'jsonschema',
    'jsonschema-specifications',
    'kiwisolver',
    'MarkupSafe',
    'matplotlib-inline',
    'mistune',
    'mpmath',
    'msgpack',
    'nbconvert',
    'nbformat',
    'nest-asyncio',
    'numpy',
    'packaging',
    'pandas',
    'pandocfilters',
    'parso',
    'pexpect',
    'pillow',
    'protobuf',
    'platformdirs',
    'prometheus_client',
    'prompt-toolkit',
    'psutil',
    'ptyprocess',
    'pure-eval',
    'pybind11-global',
    'pycparser',
    'pycryptodome',
    'Pygments',
    'pyparsing',
    'python-dateutil',
    'pytz',
    'PyYAML',
    'referencing',
    'requests',
    'rich',
    'rpds-py',
    'six',
    'sniffio',
    'stack-data',
    'sympy',
    'terminado',
    'tinycss2',
    'torch',
    'torchvision',
    'tornado',
    'tqdm',
    'traitlets',
    'typer',
    'types-python-dateutil',
    'typing_extensions',
    'tzdata',
    'urllib3',
    'wcwidth',
    'webencodings',
    'websocket-client',
]

setup(
    name="cifer",
    version="0.1.23",
    author="cifer.ai",
    author_email="parit@cifer.ai",
    description="Federated Learning and Fully Homomorphic Encryption",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.cifer.ai",
    license="Apache License 2.0",
    packages=find_packages(include=["cifer", "cifer.*"]),  # รวม nested packages
    include_package_data=True,  # รวมไฟล์ข้อมูลเพิ่มเติม
    package_dir={'client': 'Client'},
    install_requires=install_requires,  
    tests_require=[
        'coverage', 'wheel', 'pytest', 'requests_mock'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",  
        "License :: OSI Approved :: Apache Software License",
        "Development Status :: 3 - Alpha",  
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
    ]
)
