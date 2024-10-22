from setuptools import setup, find_packages

setup(
    name="test_cloud_storage",
    version="0.6.3",
    author="Aaditya Muleva",
    author_email="aaditya.muleva@trovehealth.io",
    description="A unified cloud storage package for AWS, Azure, and GCP",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    license='MIT',
    install_requires=[
        'boto3',  
    ],
)