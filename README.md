# Advanced pytest
## Passing commandline arguments to pytest
Pass input arguments from commandline to test file
```sh
py.test -s -q test_sample.py --slide_number "Slide1"

py.test -s -q test_sample.py --slide_number "Slide2"
```
## Test parametrization
Use `pytest.mark.parametrize` to test website title on `Firefox` and `Chrome` browsers
```sh
py.test -s -q test_website_title.py
```
## Using pytest and mock libraries
Use pytest with mock library to test weather forecast module
### Reference
https://www.youtube.com/watch?v=RcN26hznmk4
