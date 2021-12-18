#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# -*- coding: utf-8 -*-
#
# Last modified: Sat, 23 Sep 2017 01:11:27 +0900
#
import os
import json
import sbml2json
import cgi, cgitb

cgitb.enable()

form = cgi.FieldStorage()
fileitem = form["sbml_file"]

# Test if the file was uploaded
if fileitem.filename:
    # strip leading path from file name
    # to avoid directory traversal attacks
    fn = os.path.basename(fileitem.filename)
    open("files/" + fn, "wb").write(fileitem.file.read())
    message = 'The file "' + fn + '" was uploaded successfully'
    sbml2json.add_sbml_objects("files/" + fn)
    string_json = json.dumps(sbml2json.sbml_json)
    message = string_json

else:
    message = "No file was uploaded"

print(
    """\
Content-Type: text/javascript\n\n

%s
"""
    % (message,)
)
