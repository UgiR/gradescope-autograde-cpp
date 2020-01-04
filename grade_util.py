import os
import shutil
import json
from pathlib import Path


class Config:
    SUBMITTED_SOURCE = '/autograder/submission'
    SUBMISSION_META_FILE = '/autograder/submission_metadata.json'
    RESULTS_FILE = '/autograder/results/results.json'
    TEST_DIR = '/autograder/source/tests'  #  directory where all tests reside


def file_exists(path: str) -> bool:
    return Path(path).is_file()


def is_submitted(*files: str) -> bool:
    for file in files:
        if not file_exists(os.path.join(Config.SUBMITTED_SOURCE, file)):
            return False
    return True


def write_result(**kwargs):
    with open(Config.RESULTS_FILE, 'w+') as result:
        json.dump(kwargs, result)


def write_predefined_result(file: str):
    shutil.copyfile(file, Config.RESULTS_FILE)


def number_submissions():
    '''
    :return: Number of previous submissions. On first submission, will return 0.
    '''
    with open(Config.SUBMISSION_META_FILE) as file:
        meta = json.load(file)
        return len([submission for submission in meta['previous_submissions'] if float(submission['score']) > 0])

