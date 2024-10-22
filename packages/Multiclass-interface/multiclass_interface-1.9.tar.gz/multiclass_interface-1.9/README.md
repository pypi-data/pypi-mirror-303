# Multiclass interface

`multiclass_interface` is a package that allows you to interact with multiple objects as if it was a single object.

The interfaced objects can be executed:

- in the same thread `MultiClassInterface`
- in individual threads, `MultiThreadClassInterface`
- in individual processes
    - using `multiprocessing`: `MultiProcessClassInterface`
    - using `mpi4py`: `MPIClassInterface`

Furthermore, the `ProcessClass` can be used to interface an object in a different process as if it was in the current process. This feature is useful when running an object that needs to interface a dll/so in its own memory space.


## Installation

`pip install multiclass_interface`

## Usage
See https://hawc2.pages.windenergy.dtu.dk/HAWC2Lib/MulticlassInterface.html

## Support
Please use the issue tracker to report problems, ideas for improvments etc.

Merge requests are very welcome
