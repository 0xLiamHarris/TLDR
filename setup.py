from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess
import sys

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        try:
            # Attempt to install Playwright browsers
            subprocess.check_call([sys.executable, "-m", "playwright", "install"])
            print("Successfully installed Playwright browsers.")
        except subprocess.CalledProcessError as e:
            print("Failed to install Playwright browsers automatically. You may need to run 'playwright install' manually.")
            raise e

setup(
    name='TLDR',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'beautifulsoup4==4.9.3',
        'requests==2.25.1',
        'playwright==1.41.2',
    ],
    cmdclass={
        'install': PostInstallCommand,
    },
    entry_points={
        'console_scripts': [
            'TLDR=app.scraper:main',
        ],
    },
)
