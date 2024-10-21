from setuptools import setup, find_packages

setup(
    name="bootstrap25",
    version="0.1.0",
    author="Your Name",
    author_email="your-email@example.com",
    description="A description of your project",
    #long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://pypi.org/project/gopikachugo/",
    packages=find_packages(),  # Automatically find packages in your project
    include_package_data=True,  # Include other files specified in MANIFEST.in
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[],  # List dependencies if any
)
