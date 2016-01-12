import sys
import setuptools
from setuptools.command.test import test as TestCommand

import nvstream


class PyTest(TestCommand):
    # """ Command to run tests using pytest framework
    # This is called via setup.py as ::
    #     python setup.py test

    # Some tests will take a long time to run, so an option is allowed to
    # skip those tests (if they are marked as such)::
    #     python setup.py test --no-runslow
    # should skip those tests
    # During test development it's convenient to write to stdout/stderr to
    # debug the test. use -s|--no-capture to achieve this::
    #     python setup.py test --no-capture
    # """
    # description = "run test scripts"
    # command_consumes_arguments = False

    # user_options = [
    #     ('no-runslow', None, "don't run tests marked as slow"),
    #     ('no-capture', "s", "don't capture stdout in tests"),
    # ]
    # boolean_options = [
    #     'no-runslow',
    #     'no-capture',
    # ]
    # def initialize_options(self):
    #     self.no_runslow = False
    #     self.no_capture = False
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        # params = ['tests']
        # if self.no_runslow:
        #     params += ['--no-runslow']
        # if self.no_capture:
        #     params += ['--capture=no']
        retcode = pytest.main(self.test_args)

        sys.exit(retcode)


setuptools.setup(
    name='nvstream',
    version=nvstream.__version__,
    tests_require=[
        'pytest',
        'coverage'
    ],
    install_requires=[
        'setuptools',
    ],
    cmdclass={
        'test': PyTest
    },
    author_email='fratczakz@gmail.com',
    description='Module for streaming night vision video from Raspbery PI',
    include_package_data=True,
    packages=setuptools.find_packages()
)
