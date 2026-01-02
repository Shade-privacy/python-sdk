from setuptools import setup, find_packages

setup(
    name="veil-privacy",
    version="1.0.5",
    description="Veil Privacy SDK — private execution & privacy tooling",
    long_description=(
        "Veil Privacy SDK\n\n"
        "Veil is a privacy execution toolkit enabling confidential flows, "
        "commitment-based systems, and privacy-preserving infrastructure "
        "across multiple chains.\n\n"
        "Formerly known as shade-privacy."
    ),
    long_description_content_type="text/plain",
    author="Peter Njuguna",
    author_email="",
    url="https://veil.so",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=[
        # add real deps here if any
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Security :: Cryptography",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
