from setuptools import setup, find_packages

setup(
    name="robocore",  # Package name
    version="0.0.1",  # Package version
    author="Pranay Thangeda",
    author_email="contact@prny.me",
    description="A Python middleware for robotic communication.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/pthangeda/robocore",
    packages=find_packages(),
    install_requires=[
        "pyzmq>=22.0.0",
        "PyYAML>=5.4",
        "rerun-sdk>=0.19.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    license='MIT', 
    keywords='robotics communication middleware',
)