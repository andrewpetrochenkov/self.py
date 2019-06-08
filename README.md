<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/self.svg?longCache=True)](https://pypi.org/project/self/)
[![](https://img.shields.io/pypi/v/self.svg?maxAge=3600)](https://pypi.org/project/self/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/self.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/self.py/)

#### Installation
```bash
$ [sudo] pip install self
```

#### Functions
function|`__doc__`
-|-
`self.self(method, *args, **kwargs)` |`@self` method decorator to return self object

#### Examples
```python
>>> from self import self

>>> class CLS:
	@self
	def method(self):
		...

	@self
	def method2(self):
		...

>>> CLS().method().method2() # jQuery like chain
```

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>