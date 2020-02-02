import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
with open("requirements.txt", "r") as fh:
    install_requires = fh.read().splitlines()

setuptools.setup(
     name='fastquant',  
     version='0.1.2.8',
     author="Lorenzo Ampil",
     author_email="lorenzo.ampil@gmail.com",
     description="Bringing quantitative investing to the mainstream",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/enzoampil/fastquant",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
         "Operating System :: OS Independent",
     ],
     install_requires=install_requires,
 )
