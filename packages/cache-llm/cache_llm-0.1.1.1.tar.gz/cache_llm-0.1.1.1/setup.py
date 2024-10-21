from setuptools import setup, find_packages

setup(
    name="cache-llm",
    version="0.1.1.1",
    author="li-xiu-qi",
    author_email="lixiuqixiaoke@qq.com",
    description="A simple cache for LLM",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/li-xiu-qi/cache-llm",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "aiohttp==3.10.10",
        "diskcache==5.6.3",
        "openai==1.52.0",
        "pydantic==2.9.2",
        "setuptools==75.1.0",
    ],
)