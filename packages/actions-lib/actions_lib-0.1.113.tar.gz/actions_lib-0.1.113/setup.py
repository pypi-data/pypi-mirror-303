from setuptools import setup, find_packages

setup(
    name="actions_lib",                        # package name
    version="0.1.113",                            # version
    description="",  # description
    long_description=open("README.md").read(),  # README.md long_description
    long_description_content_type="text/markdown",  # long description content type
    author="ardio",                         # author
    license="MIT",                              # license
    packages=find_packages(),                   # find packages
    include_package_data=True,
    package_data={
        '': ['**/*.*'],
    },
    install_requires=[
        'web3'
    ],
    classifiers=[                               # classifiers
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',                    # supported Python version
)
