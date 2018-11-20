[![](https://img.shields.io/pypi/pyversions/self.svg?longCache=True)](https://pypi.org/pypi/self/)
[![](https://img.shields.io/pypi/v/self.svg?maxAge=3600)](https://pypi.org/pypi/self/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/self.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/self.py/)

#### Install
```bash
$ [sudo] pip install self
```

#### Functions
function|description
-|-
`self.self(method, self, *args, **kwargs)`|`@self` method decorator to return self object

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

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>