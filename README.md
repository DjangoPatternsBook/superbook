# Chapter 9: Testing and Debugging

* Most of the testing section refers to:
	- `src/profiles/tests.py`
	- `src/app1/tests.py`
* Logging example can be seen here
	- `src/profiles/views.py` (SignInAndSignUp.get() logging line)
	- `logs/superbook.log` (logged lines will appear when you visit home page)
* Debugging template tag can be found by visiting <http://localhost:8000/debugtest/> in your browser. Code is located in:
	- `src/profiles/templatetags/debug.py`
	- `src/templates/debugtest.html`
