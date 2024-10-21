from setuptools import setup, find_packages

setup(
    name="vlm-ocr",
    version="0.1.2",
    author="Ethan Bailie",
    author_email="eabailie@uwaterloo.ca",
    description="A library for OCR using VLMs. Currently supports OpenAI. Will work on Unix operating systems out of the box, some tweaking may be needed for Windows.",
    packages=find_packages(),
    install_requires=[
        "openai==1.51.0",
        "anthropic==0.36.2",
        "pdf2image==1.17.0",
        "python-dotenv==1.0.1",
        "requests==2.32.3"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
