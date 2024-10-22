# chessdata-pyclient
Python library for interacting with foxden / CHESS data services

# Installation
1. In an environment of your choosing, run `pip install chessdata-pyclient`
2. Set the environment variable `$REQUESTS_CA_BUNDLE` to a path to a CA bundle to use (for SSL).
3. Set `$PATH` to include the path to a `foxden` CLI executable (so that `chessdata-pyclient` can run `foxden token create <scope>`)
4. Set `$KRB5CCNAME` to be the full path to a file containing a valid kerberos ticket. It is up to the user to make sure the ticket is not expired.

# Examples
- Search the CHESS metadata database for records on tomography scans taken at ID3A:
  ```python
  from chessdata import query
  records = query('{"beamline":"3a" "technique":"tomography"}')
  ```
- Search the CHESS spec scans database for all scan records from the "pi-nnnn-x" BTR:
  ```python
  from chessdata import query
  records = query('{"btr": "pi-nnnn-x"}', url='https://foxden-scans.classe.cornell.edu:8390')
  ```