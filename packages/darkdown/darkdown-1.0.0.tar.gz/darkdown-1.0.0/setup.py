from setuptools import setup, find_packages

# Read the content of your README.md file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="darkdown",
    version="1.0.0",
    author="phoenix",
    author_email="lphxl@pm.me",
    description="A secure Markdown server with GitHub-style rendering",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/phx/darkdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "markdown-it-py",
        "mdurl",
    ],
    entry_points={
        "console_scripts": [
            "darkdown=darkdown:main",
        ]
    },
    include_package_data=True,
)
