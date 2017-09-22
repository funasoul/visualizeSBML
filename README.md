# visualizeSBML
visualize SBML model with cytoscape.js

## Screenshot
![screenshot](https://raw.githubusercontent.com/funasoul/visualizeSBML/images/visualizeSBML.png)

## Requirements
- [libSBML](http://sbml.org/Software/libSBML) with python binding.

[FunalabPorts](https://github.com/funasoul/FunalabPorts) might be your help :-)

## Download
Just clone from this repository.
```sh
git clone https://github.com/funasoul/visualizeSBML.git
cd visualizeSBML
```

## How to use
1. Convert SBML to JSON
```sh
python sbml2json.py MAPK.xml
```
will generate `model.json`.

2. Launch HTTP server on your machine
```sh
python -m CGIHTTPServer       # for Python2
python -m http.server --cgi   # for Python3
```

3. Access your web server (`http://localhost:8000`)
```sh
open http://localhost:8000
```

Have fun!
