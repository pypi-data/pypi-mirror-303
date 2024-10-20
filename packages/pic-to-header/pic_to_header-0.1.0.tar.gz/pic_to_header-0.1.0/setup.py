from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pic-to-header",
    version="0.1.0",
    author="Sunwood-ai-labs",
    author_email="your.email@example.com",
    description="A Python application to generate header images using mask and input images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sunwood-ai-labs/pic-to-header",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    install_requires=[
        "streamlit",
        "opencv-python",
        "numpy",
        "loguru",
    ],
    entry_points={
        "console_scripts": [
            "pic-to-header=pic_to_header.app:main",
        ],
    },
)
