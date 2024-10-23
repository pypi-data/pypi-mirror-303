from setuptools import setup, find_namespace_packages

setup(
    name="ssak3",
    version="1.0.19",
    packages=find_namespace_packages(),       # 패키지 포함
    include_package_data=True,
    install_requires=[
        'apify==2.0.0',
        'loguru==0.7.2',
    ],
    author="bigzzodev",
    author_email="bigzzodev@gmail.com",
    description="ssak3 package",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/bigzzodev",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
