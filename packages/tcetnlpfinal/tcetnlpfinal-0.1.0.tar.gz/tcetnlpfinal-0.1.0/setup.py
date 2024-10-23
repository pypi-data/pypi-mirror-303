from setuptools import setup, find_packages

setup(
    name="tcetnlpfinal",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[  # Optional: list your project dependencies here.
        # 'dependency1',
        # 'dependency2',
    ],
    author="Ishaan",
    author_email="ishaang1410@gmail.com",
    description="A brief description of your project.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Example: choose a license
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
