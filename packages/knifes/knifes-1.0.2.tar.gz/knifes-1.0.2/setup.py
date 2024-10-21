from setuptools import setup, find_packages


setup(
    name="knifes",
    version="1.0.2",
    author="knifes",
    author_email="author@example.com",
    description="Swiss Army Knife",
    long_description="`pip install knifes --index-url https://pypi.python.org/simple -U`",
    long_description_content_type="text/markdown",
    url="https://github.com/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "anyio",  # required by shell
        # "python-dotenv",  # required by deploy
        # "gevent",  # required by deploy/celery
        # "httpx[http2]",
        # 'cryptography',  #  required by aes
    ],
    # entry_points={
    #     "console_scripts": [
    #         "deploy = knifes.deploy.main:app",
    #     ],
    # },
)
