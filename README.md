SQLAlchemy-Informix-IfxPy
=========================

A SQLAlchemy dialect to support Informix database connections using IfxPyDBI

This dialect supports the IfxPy project:
    <https://github.com/OpenInformix/IfxPy>

### Current Status

Alpha. Possibly useful, but may not even work.

This project was a quick hack based on the original SQLAlchemy-Informix driver.
I have not tried to use it since 2018 and at the time I think it was working
for SELECT statements only.

### Potential problems

Although PipEnv thinks you should be able to install ifxpy version 3.0.3 with
`pipenv sync`, it currently fails. I used `pipenv shell` and then
`pip install ifxpy` and got version 3.0.1.
There's already an issue for this.

To run the SQLAlchemy tests, I believe you need an Informix database set up
with logging enabled. To create one, go to Informix `dbaccess`, create a
database, give it a name, and make sure you pick LOG > Log, then create it.

Once you have the database created, you might be able to run the tests using
a command like this:

```
python -m pytest -v \
     --requirements sqlalchemy_ifxpy.requirements:Requirements \
     --dburi informix+ifxpy://USER@HOST/TESTDATABASE
```
with USER, HOST, and TESTDATABASE being replaced with the appropriate info
for your environment and the database you created.

I don't have an Informix database available for testing so I don't know how
it will do.

Pull requests are welcome. I am unlikely to be able to do anything to
support this.
