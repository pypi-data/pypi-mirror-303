from setuptools import setup, find_packages

setup(
    name="ssak3",
    version="1.0.0",
    packages=find_packages(),   # 패키지 포함
    install_requires=[],        # 패키지가 의존하는 다른 패키지 목록
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
