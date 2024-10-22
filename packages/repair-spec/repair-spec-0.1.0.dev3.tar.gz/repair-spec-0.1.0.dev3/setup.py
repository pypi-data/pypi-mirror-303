from setuptools import setup, find_packages

setup(
    name="repair-spec",
    version="0.1.0.dev3",
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=[
        "openai",
    ],
    author="Sibo Zhang",
    author_email="zhangsibo1129@gmail.com",
    description="Auto repair spec",
    url="https://github.com/zhangsibo1129/specrepair",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
