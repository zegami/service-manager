#!/usr/bin/python

from bottle import route, run
from bottle import static_file

assets_response="""
{
  "_id": "hmrc-assets-frontend",
  "_rev": "2-f75f94a1d50370c34eb6fd4f27fefa51",
  "name": "hmrc-assets-frontend",
  "description": "Frontend assets for the tax platform",
  "dist-tags": {
    "latest": "0.0.1"
  },
  "versions": {
    "0.0.0": {
      "name": "hmrc-assets-frontend",
      "version": "0.0.0",
      "description": "Frontend assets for the tax platform",
      "repository": {
        "type": "git",
        "url": "https://github.com/hmrc/assets-frontend.git"
      },
      "contributors": [
        {
          "name": "Rory Powis",
          "email": "rory.powis@digital.cabinet-office.gov.uk"
        },
        {
          "name": "Richard Vinall",
          "email": "richard.vinall@digital.cabinet-office.gov.uk"
        },
        {
          "name": "Anthony Munene",
          "email": "anthony.munene@digital.cabinet-office.gov.uk"
        }
      ],
      "license": "MIT",
      "bugs": {
        "url": "https://github.com/hmrc/assets-frontend/issues"
      },
      "homepage": "https://github.com/hmrc/assets-frontend",
      "gitHead": "84f6ffb38df815a071af379434ee7a2c77e8636e",
      "_id": "hmrc-assets-frontend@0.0.0",
      "scripts": {},
      "_shasum": "e4743b8987f99f7a170a46b82885f7ef9ac429e1",
      "_from": ".",
      "_npmVersion": "2.0.0",
      "_npmUser": {
        "name": "rory.powis",
        "email": "rory.powis@digital.cabinet-office.gov.uk"
      },
      "maintainers": [
        {
          "name": "rory.powis",
          "email": "rory.powis@digital.cabinet-office.gov.uk"
        }
      ],
      "dist": {
        "shasum": "e4743b8987f99f7a170a46b82885f7ef9ac429e1",
        "tarball": "http://registry.npmjs.org/hmrc-assets-frontend/-/hmrc-assets-frontend-0.0.0.tgz"
      },
      "directories": {}
    },
    "0.0.1": {
      "name": "hmrc-assets-frontend",
      "version": "0.0.1",
      "description": "Frontend assets for the tax platform",
      "repository": {
        "type": "git",
        "url": "https://github.com/hmrc/assets-frontend.git"
      },
      "contributors": [
        {
          "name": "Rory Powis",
          "email": "rory.powis@digital.cabinet-office.gov.uk"
        },
        {
          "name": "Richard Vinall",
          "email": "richard.vinall@digital.cabinet-office.gov.uk"
        },
        {
          "name": "Anthony Munene",
          "email": "anthony.munene@digital.cabinet-office.gov.uk"
        }
      ],
      "license": "MIT",
      "bugs": {
        "url": "https://github.com/hmrc/assets-frontend/issues"
      },
      "homepage": "https://github.com/hmrc/assets-frontend",
      "gitHead": "84f6ffb38df815a071af379434ee7a2c77e8636e",
      "_id": "hmrc-assets-frontend@0.0.1",
      "scripts": {},
      "_shasum": "e4743b8987f99f7a170a46b82885f7ef9ac429e1",
      "_from": ".",
      "_npmVersion": "2.0.0",
      "_npmUser": {
        "name": "rory.powis",
        "email": "rory.powis@digital.cabinet-office.gov.uk"
      },
      "maintainers": [
        {
          "name": "rory.powis",
          "email": "rory.powis@digital.cabinet-office.gov.uk"
        }
      ],
      "dist": {
        "shasum": "e4743b8987f99f7a170a46b82885f7ef9ac429e1",
        "tarball": "http://registry.npmjs.org/hmrc-assets-frontend/-/hmrc-assets-frontend-0.0.1.tgz"
      },
      "directories": {}
    }
  },
  "readme": "",
  "maintainers": [
    {
      "name": "rory.powis",
      "email": "rory.powis@digital.cabinet-office.gov.uk"
    }
  ],
  "time": {
    "modified": "2014-11-12T14:39:21.207Z",
    "created": "2014-11-12T14:39:21.207Z",
    "0.0.1": "2014-11-12T14:39:21.207Z"
  },
  "homepage": "https://github.com/hmrc/assets-frontend",
  "repository": {
    "type": "git",
    "url": "https://github.com/hmrc/assets-frontend.git"
  },
  "contributors": [
    {
      "name": "Rory Powis",
      "email": "rory.powis@digital.cabinet-office.gov.uk"
    },
    {
      "name": "Richard Vinall",
      "email": "richard.vinall@digital.cabinet-office.gov.uk"
    },
    {
      "name": "Anthony Munene",
      "email": "anthony.munene@digital.cabinet-office.gov.uk"
    }
  ],
  "bugs": {
    "url": "https://github.com/hmrc/assets-frontend/issues"
  },
  "license": "MIT",
  "readmeFilename": "README.md",
  "_attachments": {}
}
"""

@route('/ping')
def ping():
    return "pong"

@route("/hmrc-assets-frontend")
@route("/hmrc-assets-frontend/")
def search_xml():
    return assets_response

@route('/<filepath:path>')
def server_static(filepath):
    print './static/' + filepath
    return static_file(filepath, root="./static/")

run(host='localhost', port=8061, debug=True)
