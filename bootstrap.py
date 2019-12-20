import subprocess

#  Code to be executed before the tests are run
def init():
    #  3. compile Catch once so we are not recompiling for each test
    #     the resulting .o object file will be use for all tests
    subprocess.call(['make', 'catch-essential'], cwd='/autograder/source/tests')
