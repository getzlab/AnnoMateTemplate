import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="<ReviewerName>",
    version="0.0.0",
    author="<author>",
    author_email="<author_email>",
    description="<description>",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/<repo>",
    project_urls={
        "Bug Tracker": "https://github.com/<repo>/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.9",
    install_requires = [
                        'ipykernel==6.22.0',
                        'pandas==1.5.2',
                        'setuptools',
                        'JupyterReviewer==0.0.7',
                       ]
)   