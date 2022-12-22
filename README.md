Beacon Model Generation (BMG)
=============================

BMG is a python package and command-line utility used to generate C++ models.

Building the bmg binary
-----------------------

To build the bmg binary you will need to install pyinstaller first, then just run make:

```
make binary
```

The resulting binary will be called `dist/bmg`, use the following command to test it built correctly:

```
./dist/bmg --help
```


Testing
-------

To run the test suite:

```
make tests
```

Configuration File Format
-------------------------

The bmg configuration file consists of two main sections, settings and models.

### Settings


| Name    | Default | Description |
| ------- | ------- | ----------- |
| prefix  | BL      | String to prefix class names |
| imports | []      | A list of imports to add to each model header file |

### Models

The models section contains a list of models with the following attributes:

| Name | Default | Description |
| ---- | ------- | ----------- |
| name | | The name of the class |
| description | | A description of the class |
| attributes | [] | A list of attributes |

Each attribute has the following attributes:

| Name | Default | Description |
| ---- | ------- | ----------- |
| name | | The name of the attribute |
| type | | The type of the attribute |
| primary | false | If primary = true this attribute is unique |
| list | false | Sets attribute to a list of items with the specified type |
| containment | false | Implies that this attribute contains objects that are owned by the current object (used for object deletion policies) |


