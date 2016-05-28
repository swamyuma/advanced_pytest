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
##Persisting Commandline Options
Always exit at first fail and show locals for all tests
```ini
[pytest]
addopts = -x -l # will always use thes options for all tests
```
##Pytest Marking
Mark any test with a keyword and select based on keyword to run on not run 
```python
import pytest

@pytest.mark.codec_x
def test_codec_x():
    print "X"

@pytest.mark.codec_y
def test_codec_y():
    print "Y"
```
and run it as
```bash
py.test -m "codec_x"
py.test -m "codec_y"
py.test -m "not codec_x"
```
##Skip all test functions of a class or module
You can use the skipif decorator (and any other marker) on classes:
```python
@pytest.mark.skipif(sys.platform == 'win32',
                    reason="does not run on windows")
class TestPosixCalls:

    def test_function(self):
        "will not be setup or run under 'win32' platform"
```
##Mark a test function as expected to fail
You can use the xfail marker to indicate that you expect a test to fail:
```python
@pytest.mark.xfail
def test_function():
    ...
```
This test will be run but no traceback will be reported when it fails. Instead terminal reporting will list it in the “expected to fail” (XFAIL) or “unexpectedly passing” (XPASS) sections.
##Beyond Simple Testing: fixtures
Something that provides a fixed baseline
* initialzation before tests are run
* avoids repetitive calls
* leverages dependency injection
```python
import pytest

@pytest.fixture
def somevalue():
    return 42

def test_somevalue(somevalue):
    assert somevalue == 42
```
##Reuse the same fixture in same session or all modules
###Scoping fixture functions
```python
# content of conftest.py
import pytest
import smtplib
@pytest.fixture(scope="module")
def smtp():
    return smtplib.SMTP("smtp.gmail.com")

# content of test_module.py

def test_ehlo(smtp):
    response, msg = smtp.ehlo()
    assert response == 250
    assert b"smtp.gmail.com" in msg
    assert 0  # for demo purposes

def test_noop(smtp):
    response, msg = smtp.noop()
    assert response == 250
    assert 0  # for demo purposes
```
and run it
```bash
$ py.test test_module.py
======= test session starts ========
platform linux -- Python 3.4.0, pytest-2.9.1, py-1.4.31, pluggy-0.3.1
rootdir: $REGENDOC_TMPDIR, inifile:
collected 2 items

test_module.py FF

======= FAILURES ========
_______ test_ehlo ________

smtp = <smtplib.SMTP object at 0xdeadbeef>

    def test_ehlo(smtp):
        response, msg = smtp.ehlo()
        assert response == 250
        assert b"smtp.gmail.com" in msg
>       assert 0  # for demo purposes
       E       assert 0

       test_module.py:6: AssertionError
       _______ test_noop ________

       smtp = <smtplib.SMTP object at 0xdeadbeef>

   def test_noop(smtp):
       response, msg = smtp.noop()
               assert response == 250
               >       assert 0  # for demo purposes
               E       assert 0

               test_module.py:11: AssertionError
                           ======= 2 failed in 0.12 seconds ========

```
You see the two assert 0 failing and more importantly you can also see that the same (module-scoped) smtp object was passed into the two test functions because pytest shows the incoming argument values in the traceback. As a result, the two test functions using smtp run as quick as a single one because they reuse the same instance.
"session" scope is usefull for cross test caching. All tests in a given directory will use the same fixture using it.
##Fixture finalization / executing teardown code
pytest supports execution of fixture specific finalization code when the fixture goes out of scope. By accepting a request object into your fixture function you can call its request.addfinalizer one or multiple times:
```python
# content of conftest.py

import smtplib
import pytest

@pytest.fixture(scope="module")
def smtp(request):
    smtp = smtplib.SMTP("smtp.gmail.com")
    def fin():
        print ("teardown smtp")
        smtp.close()
    request.addfinalizer(fin)
    return smtp  # provide the fixture value
```
and run it
```bash
$ py.test -s -q --tb=no
FFteardown smtp
```

