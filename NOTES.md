#Pytest Features
##Reference
http://pytest.org/latest/getting-started.html
##Test Discovery
pytest implements the following standard test discovery:

* If no arguments are specified then collection starts from testpaths (if configured) or the current directory. Alternatively, command line arguments can be used in any combination of directories, file names or node ids.
* recurse into directories, unless they match norecursedirs
* test_*.py or *_test.py files, imported by their test package name.
* Test prefixed test classes (without an __init__ method)
* test_ prefixed test functions or methods are test items
##Assert Expected Exceptions
Use context manager to test exceptions
```python
# content of test_sysexit.py
import pytest
def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()
```
##Combining Multiple Tests
Once you start to have more than a few tests it often makes sense to group tests logically, in classes and modules. Let’s write a class containing two tests:

# content of test_class.py
```python
class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')
```
##Specifying tests / selecting tests
Several test run options:
```bash
py.test test_mod.py   # run tests in module
py.test somepath      # run all tests below somepath
py.test -k stringexpr # only run tests with names that match the
                      # "string expression", e.g. "MyClass and not method"
                      # will select TestMyClass.test_something
                      # but not TestMyClass.test_method_simple
py.test test_mod.py::test_func  # only run tests that match the "node ID",
                                # e.g "test_mod.py::test_func" will select
                                # only test_func in test_mod.py
py.test test_mod.py::TestClass::test_method  # run a single method in
                                             # a single class
```
