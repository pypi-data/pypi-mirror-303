from setuptools import setup, find_packages
from setuptools.command.install import install

class CustomInstall(install):
    def run(self):
        # Call the standard install process
        install.run(self)
        # Display the warning message after installation
        print("\n\n====================== WARNING ======================")
        print("TaskGen is no longer maintained by John Tan Chong Min")
        print("The new repo is now AgentJo at https://github.com/tanchongmin/agentjo")
        print("Check out the pypl package here: https://pypi.org/project/agentjo/")
        print("=====================================================\n\n")

setup(
    name="taskgen-ai",
    version="4.0.1",
    packages=find_packages(),
    install_requires=[
        "openai>=1.3.6",
        "langchain",
        "dill>=0.3.7",
        "termcolor>=2.3.0",
        "requests",
        "PyPDF2",
        "python-docx",
        "pandas",
        "chromadb",
        "xlrd",
        "chromadb>=0.5.2",
        "asyncio"
    ],
    cmdclass={
        'install': CustomInstall,
    },
)
