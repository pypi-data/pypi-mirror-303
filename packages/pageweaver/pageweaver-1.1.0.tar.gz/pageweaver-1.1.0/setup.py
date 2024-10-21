from setuptools import setup, find_packages
# make a function to read the Readme and use it a long description but in a single string
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='pageweaver',
    version='1.1.0',
    author='Krishnatejaswi S, Sridhar D Kedlaya',
    author_email='shentharkrishnatejaswi@gmail.com, sridhardked@gmail.com',
    description='A web crawler to fetch web novel chapters and generate a PDF.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/KTS-o7/pageweaver',
    keywords=['web novel', 'crawler', 'PDF generation', 'web scraping'],
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'pylatex',
        'argparse',
        'langdetect'
    ],
    entry_points={
        'console_scripts': [
            'pageweaver=pageweaver.novel_crawler_service:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)