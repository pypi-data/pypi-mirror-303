from setuptools import find_packages, setup

setup(
    name='notion_automation',
    version='1.0.2',
    description='Automate Notion database creation with JSON schemas',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Morgan Joyce',
    author_email='morganj2k@gmail.com',
    url='https://github.com/atxtechbro/notion-automation',
    packages=find_packages(),
    install_requires=[
        'requests',
        'python-dotenv',
        'pydantic',
        'pytest',
        'requests-mock'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'notion-cli=notion_automation.cli:main',  # Command-line entry point
        ],
    },
)
