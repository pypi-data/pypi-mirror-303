from setuptools import setup, find_packages

setup(
    name="GorillaTag",  # This is the name of your package
    version="0.3",
    packages=find_packages(),
    install_requires=["requests"],  # Add any external dependencies if needed
    description="A room tracker package",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Ace",
    author_email="olimasterbiznes@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
