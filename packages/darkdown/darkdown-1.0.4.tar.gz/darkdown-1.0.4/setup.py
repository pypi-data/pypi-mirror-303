import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='darkdown',
     version='1.0.4',
     scripts=['darkdown'] ,
     author="phx",
     author_email="emai@example.com",
     description="A Python3 http.server wrapper that supports SSL, basic auth, markdown rendering, and styling support for markdown files and directory listings",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/phx/darkdown",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
