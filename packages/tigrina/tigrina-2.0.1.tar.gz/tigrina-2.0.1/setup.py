from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name='tigrina',
    version='2.0.1',
    author='Gide Segid',
    author_email='gidesegid@gmail.com',
    packages=find_packages(),
    description="Tigrina alphabet processing, which helps to write Tigrina by Tigrina alphabets and other functionalities for manipulation of tigrina words.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    package_data={
        'tigrina': ['tg_data/adjectives.csv','tg_data/adverbs.csv','tg_data/nouns.csv',
                    'tg_data/verbs.csv','tg_data/tokenized_data.csv',
                    'tigrina/tg_data/adjectives.csv','tigrina/tg_data/adverbs.csv','tigrina/tg_data/nouns.csv',
                    'tigrina/tg_data/verbs.csv','tigrina/tg_data/tokenized_data.csv'],
    },
    install_requires=[
        "pandas"
    ],
    entry_points={
        'console_scripts': [
            'tigrina_words=tigrina.tg_main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    license="MIT",
    python_requires='>=3.6'
)
