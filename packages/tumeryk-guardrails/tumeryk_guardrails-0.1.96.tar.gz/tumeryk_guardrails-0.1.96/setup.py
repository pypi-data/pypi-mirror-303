from setuptools import setup, find_packages

setup(
    name="tumeryk_guardrails",
    version="0.1.96",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    author="Tumeryk",
    author_email="support@tumeryk.com",
    description="API Client for Tumeryk_Guardrails",
    long_description=open("PKG-INFO").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)