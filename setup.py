import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyautosim',
    version='0.1',
    author='BAYMEX SOLUTION',
    description='automation simulation library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/BAYMEX-SOLUTION/pyautosim',
    packages=setuptools.find_packages(),
    python_requires='>=3.4',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
)
