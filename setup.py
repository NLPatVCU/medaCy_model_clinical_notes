from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from medacy_model_clinical_notes import __version__, __authors__
import sys

packages = find_packages()

def readme():
    with open('README.md') as f:
        return f.read()

class PyTest(TestCommand):
    """
    Custom Test Configuration Class
    Read here for details: https://docs.pytest.org/en/latest/goodpractices.html
    """
    user_options = [("pytest-args=", "a", "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ""

    def run_tests(self):
        import shlex
        # import here, cause outside the eggs aren't loaded
        import pytest

        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)

setup(
    name='medacy_model_clinical_notes',
    version=__version__,
    license='GNU GENERAL PUBLIC LICENSE',
    description='medaCy compatable model for mining clinical notes.',
    long_description=readme(),
    packages=packages,
    url='https://github.com/NanoNLP/medaCy_model_clinical_notes',
    author=__authors__,
    author_email='contact@andriymulyar.com',
    keywords='natural-language-processing medical-natural-language-processing machine-learning nlp-library metamap clinical-text-processing',
    classifiers=[
        '( Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 3.5',
        'Natural Language :: English',
        'Topic :: Text Processing :: Linguistic',
        'Intended Audience :: Science/Research'
    ],
    install_requires=[
        'medacy>=0.0.3',
    ],
    tests_require=["pytest"],
    cmdclass={"pytest": PyTest},
    include_package_data=True,
    zip_safe=False

)
