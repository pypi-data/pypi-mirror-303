from setuptools import setup, find_packages

setup(
    name='guavasaurus',  # Added missing comma
    version='1.1',  # Version of your package
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=[
        'numpy',  # List any dependencies your library needs
        # Add other dependencies as needed
    ],
    description='A quantum computing library for quantum circuits and algorithms.',
    author='Idrees Ahmad',  # Replace with your name
    author_email='pythoncodes22@example.com',  # Replace with your email
    url='https://github.com/pythoncodes22/Quantum_constructor',  # Update with your repo URL
    classifiers=[
        'Programming Language :: Python :: 3',  # Specify Python versions
        'License :: OSI Approved :: MIT License',  # Replace with your license
        'Operating System :: OS Independent',  # OS compatibility
    ],
    python_requires='>=3.6',  # Specify minimum Python version
)
