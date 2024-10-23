from setuptools import setup, find_packages

setup(
    name="pdftoword",
    version="0.1",
    description="A simple PDF to Word converter with a drag-and-drop interface.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Adam Dinelli",
    author_email="isaiahjpeterson007@example.com",  # Replace with your email
    url="https://github.com/yourusername/pdftoword",  # Replace with your GitHub repo
    packages=find_packages(),
    install_requires=[
        "tkinterdnd2",
        "pdf2docx"
    ],
    entry_points={
        "console_scripts": [
            "pdftoword=pdftoword.__main__:run_app",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
