from setuptools import setup, find_packages

setup(
    name='gopikachugo',  # Your package name
    version='0.1.0',  # Version of your package
    packages=find_packages(),  # Automatically find packages in the current directory
    include_package_data=True,  # Include data files specified in MANIFEST.in
    description='A brief description of your package',  # Description of your package
    author='Your Name',  # Your name
    author_email='your.email@example.com',  # Your email
    license='MIT',  # License type
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version required
)
