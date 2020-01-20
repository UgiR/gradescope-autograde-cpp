# Gradescope Autograder for C++

Download v1.1: [autograder.zip](https://github.com/UgiR/gradescope-autograde-cpp/releases/download/v1.1/autograder.zip)

To use new features in the master branch, clone or download this repository.

### Configuration

In `config.yml`, define all files that must be submitted by the student.

Example `config.yml`:

```
limit_submissions: -1  # limit number of submissions accepted. Set to -1 for unlimited (default: -1)
required_files:
  - student_file.h
```

If any of the required files are missing, the autograder terminates with a message indicating a missing file.

If all required files are submitted, they are moved into the `/autograder/tests` directory.

### Writing Tests

Create a new directory under `/autograder/tests`. This is where you can include any test files.

Files:

* `run_test` (required):

    In order for the autograder to be able to run the test, you must include a `run_test` executable file that runs
    the test. This can be in any language, so make sure it includes a shebang line (`#!/usr/bin/env bash` for example).

* `test.yml` (optional)

    This is the configuration for the specific test.

    Example `test.yml` file:

    ```
    weight: 15.0  # weight/score of the test (default: 1)
    name: 'BST balancing'  # (default: '')
    message: 'insert() must maintain a balanced BST'  # (default: '')
    show_output: false  # whether to display stdout/stderr output on failure (default: true)
    timeout: 10  # test fails if it does not finish running in 10 seconds (default: null)
    visibility: hidden  # controls visibility of test case to students (default: visible)
    ```

* Any other files that `run_test` requires.

#### CLI

To facilitate the process of writing tests, it is possible to generate new test directories via command line.

Example:

```
./grader add test -d my_new_test
```

Executing this command will generate a new directory named "my_new_test" with a pre-populated `config.yml` file and an
empty `run_test` file.

#### Student submitted files

As specified above, the files listed in `config.yml` are moved into `/autograder/tests`. In the context of any
individual test directory, these files are found in its parent directory.

### Example output

![Gradescope output](https://i.imgur.com/Gsb3lMg.png)
