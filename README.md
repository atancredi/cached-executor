# cached-executor
Python utility to keep in memory some data (usually very large data that needs to be reloaded into RAM every program execution) and reload dinamically an external module that uses it.
In this way it is possible to edit a script operating on a large dataset without reloading it in memory every change.