from setuptools import find_packages, setup

setup(
    name='notion_automation',  # Package name (used in `pip install`)
    version='0.1.0',  # Follow semantic versioning
    description='Automate Notion database creation with JSON schemas',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/notion-automation',  # GitHub repo link
    packages=find_packages(),  # Automatically detect packages
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
