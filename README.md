## Adding Tests

1. Create a new directory under `/autograder/tests` with all the required test files.

2. In order for the autograder to be able to run the test, you must also include a `compile.sh` file that
compiles/prepares the test to be executed.

3. After executing `compile.sh`, the autograder, by default, will attempt to run an executable named `text.exe`. If the
procedure to run the test is more complex, also include a `run.sh` file.

Files:

* `compile.sh` (required)

* `run.sh` (optional) - defaults to `./test.exe`

* `test.yml` (optional)

Example `test.yml` file:

```
weight: 15.0
name: 'BST balancing'
message: 'insert() must maintain a balanced BST'
```