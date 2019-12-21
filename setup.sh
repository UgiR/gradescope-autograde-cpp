#!/usr/bin/env bash

# Prepare autograder environment

# Install Python dependencies declared in requirements.txt
apt-get install -y python python3-pip
pip3 install -r /autograder/source/requirements.txt

# Install valgrind memory tool
apt-get install valgrind -y

# Install Catch Framework for C++ testing
apt-get install catch -y

# Install cppcheck for static code analysis
apt-get install cppcheck -y

# Move python uploaded grader files into the same directory as run_autograder
cp /autograder/source/grade_util.py /autograder
cp /autograder/source/bootstrap.py /autograder
cp /autograder/source/config.yml /autograder
