from setuptools import setup, find_packages

setup(
    name='sharedir',  # The package name
    version='0.1',  # Initial version number
    description='A simple tool to share files and directories over LAN or internet.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # Set content type of the README
    author='Ujjawal Saini',  # Replace with your name
    author_email='spignelon@proton.me',  # Replace with your email
    url='https://github.com/spignelon/ShareDir',  # Replace with the actual URL
    license='AGPL-3.0',
    packages=find_packages(),
    install_requires=[  # Dependencies as per your `requirements.txt`
        'blinker==1.8.2',
        'click==8.1.7',
        'diceware==0.10',
        'Flask==3.0.3',
        'itsdangerous==2.2.0',
        'Jinja2==3.1.4',
        'MarkupSafe==2.1.5',
        'pypng==0.20220715.0',
        'qrcode==7.4.2',
        'setuptools==75.1.0',
        'typing_extensions==4.12.2',
        'Werkzeug==3.0.4'
    ],
    entry_points={
        'console_scripts': [
            'sharedir = sharedir.sharedir:main',  # Command to run the script
        ],
    },
    classifiers=[  # Classifiers help categorize the package
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Utilities',
    ],
    python_requires='>=3.6',  # Minimum Python version requirement
)
