from setuptools import setup, find_packages

classifiers = [
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 5 - Production/Stable',

    # Indicate who your project is intended for
    # 'Intended Audience :: Developers',
    # 'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish (should match "license" above)
    'License :: Apache License Version 2.0',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3'
]

long_description = ''
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

description = 'Fast 7zip crack assistant tool which support GPU/CPU.'
install_requires = []

setup(
    name='tt7zcrack',
    version='0.0.8',
    description=description,
    author='tp7309',
    author_email='yiyou7309@gmail.com',
    url='https://github.com/tp7309/tt7zcrack',
    license='Apache License Version 2.0',
    keywords='7z 7zip password crack hashcat jtr john gpu',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'tt7zcrack = src.tt7zcrack:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.5',
)

# md2rst
# pandoc --from=markdown --to=rst --output=README.rst README.md

# upload
# python setup.py bdist_wheel
# python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# python -m pip install --index-url https://test.pypi.org/simple/ --no-deps tt7zcrack -U
# twine upload dist/*

# pyinstaller
# pyinstaller --onefile src/tt7zcrack.py


# auto generate requirements.txt
# pip freeze --local > requirements.txt

# view coverage report
# coverage html -d coverage_html

# format code style
# yapf -i -r .
