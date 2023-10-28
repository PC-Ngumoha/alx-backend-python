# Unittests & Integration Tests (Python)

## Useful Points
- _Unit testing_ is the process of testing that a particular code unit (i.e a function) returns the correct output for different sets of input.

- _Integration tests_ aim to test interactions between every part of the code. Essentially, they aim to catch code additions that could cause code breakages and prevent such before it happens.

- A _Test case_ is a unique test scenario that must be set up and checked for correctness.

- A _Test fixture_ is a term used to refer to the lines of code which handle the process of setting up an environment for our test cases to run.

- A _Test suite_ is a grouping of individual test cases based on the features they are meant to test.

- The official documentation defines _mocking_ as a testing pattern which allows us to replace parts of our code with mock objects A.K.A _copies_ and make assertions about how they've been used.

- The goal of _mocking_ is to test that our code actually tries to access an external service and not to test whether the external service did what it was supposed to do when called. To that end, a common rule in mocking is to _test an item where it's used and not where it comes from_

- _Mocking_ essentially gives us a way to test the internal functionality of methods without any side effects.

- _Parameterized Testing_ is a system/type of testing in which we are able to create a single test which can be run multiple times each with different input and output values. This is useful when we notice that our test cases are becoming more and more redundant as this enables to create a single test case which can be used to test for all possible edge cases which we specify as _parameterized inputs_. Sounds really neat.



## Useful Links

- [Difference Between Unit Testing and Integration Testing](https://www.geeksforgeeks.org/difference-between-unit-testing-and-integration-testing/)

- [unittest python package documentation page](https://docs.python.org/3/library/unittest.html)

- [unittest.mock python package documentation page](https://docs.python.org/3/library/unittest.mock.html)

- [An introduction to mocking in python](https://www.toptal.com/python/an-introduction-to-mocking-in-python)

- [parameterized](https://pypi.org/project/parameterized/)

- [What are Parameterized Tests?](https://medium.com/@suman.maity112/parameterized-tests-8929080901ee)

- [Memoization Wikipedia page](https://en.wikipedia.org/wiki/Memoization)