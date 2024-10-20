from setuptools import setup, find_packages

setup(
    name="LinearRegression-FB-1",  # Package name
    version="0.1.0",  # Initial version
    author="Your Name",  # Your name
    author_email="your.email@example.com",  # Your email
    description="A simple linear regression package implemented from scratch",  # Short description
    url="https://github.com/",  # URL of the package (e.g., GitHub repo)
    packages=find_packages(),  # Automatically find the package
    install_requires=[  # Dependencies
        'numpy>=1.18.0',
    ],
    classifiers=[  # Metadata to help users find your package
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Specify the minimum Python version required
)
