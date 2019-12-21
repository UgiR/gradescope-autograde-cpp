# Gradescope Autograder for C++

### Configuration

In `config.yml`, define all files that must be submitted by the student.

Example `config.yml`:

```
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
    ```

* Any other files that `run_test` requires.

#### Student submitted files

As specified above, the files listed in `config.yml` are moved into `/autograder/tests`. In the context of any
individual test directory, these files are found in its parent directory.

### Example output

![Gradescope output](https://i.imgur.com/v7RytqQ.png)
