from setuptools import find_packages, setup

print(find_packages())

setup(
    name="scuffed_python_orchestrator",
    version="0.1.0",
    author="Michael Howard",
    author_email="",
    description="",
    packages=find_packages(),
    package_data={'scuffed_python_orchestrator': ['data/*']}, 
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent"
        ], 
    install_requires=[],
    python_requires=">=3.9"
)

