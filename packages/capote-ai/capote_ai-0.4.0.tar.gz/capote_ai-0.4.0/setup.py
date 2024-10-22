from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name= 'capote_ai',
    version='0.4.0',
    packages=find_packages(),
    install_requirements=[
        # Add dependencies here
        'openai',
        'python-dotenv',
        'PyMuPDF',
        'pdfplumber',
        'pandas',
    ],
    long_description=description,
    long_description_content_type="text/markdown",
)