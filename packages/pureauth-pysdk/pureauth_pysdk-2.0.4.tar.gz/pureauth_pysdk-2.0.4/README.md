# PureAUTH PySDK
This SDK contains functionality to sync user data to the PureAUTH server as well as the OfflineAUTH functionality.

# Development setup
For development, follow the steps below.
1) Install poetry
2) Clone the repository
3) Run command: `poetry install`
4) Run command `poetry shell`
5) Build a development wheel by running `pip install --editable .` 
6) Import the project and use. `from pureauth_pysdk import Pureauth`

A Jupyter notebook for development is provided in the docs directory. To use it, first point the notebook to the correct poetry environment for the Jupyter kernel. 
Note: After any change in the project, you need to restart the Jupyter kernel to see the changes.
