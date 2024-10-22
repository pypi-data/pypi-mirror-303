from setuptools import setup, find_packages

setup(
    name='my_unique_pretty_package',  # Replace with your package name
    version='0.1',
    packages=find_packages(),
    install_requires=[],  # List any dependencies your package needs
    author='Your Name',
    author_email='you@example.com',
    description='A short description of your package',
    url='https://github.com/ShubhamSheth24/pretty',  # Replace with your repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
