# visualizeSBML
visualize SBML model with cytoscape.js

## Requirements
- [libSBML](http://sbml.org/Software/libSBML) with python binding.

[FunalabPorts](https://github.com/funasoul/FunalabPorts) might be your help :-)

## How to use
1. Convert SBML to JSON
```sh
python sbml2json.py MAPK.xml
```
will generate `model.json`.

2. Upload this repository to your web server.
```sh
cd ..
rsync -auvz visualizeSBML $your_web_server:public_html/
```

3. Access your web server (ex. `https://$your_web_server/$your_id/visualizeSBML/`)

Have fun!
