#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2015, James Earl Douglas <james@earldouglas.com>
#
# This file is part of Ansible.
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

DOCUMENTATION = """
module: marathon
short_description: Deploy applications to Marathon
description:
  - Deploy applications to Marathon

options:
  marathon_uri:
    required: true
    description:
      - Base URI of the Marathon master

  app_id:
    required: true
    description:
      - The Marathon appId, used via <marathon>/v2/apps/:app_id

  app_json:
    required: true
    description:
      - The Marathon app descriptor (app.json)

author: "James Earl Douglas (james@earldouglas.com)"
"""

EXAMPLES = """
# Deploy an application to Marathon
- name: Deploy to Marathon
  marathon:
    marathon_uri: https://example.com:8080/
    app_id: myApp
    app_json: "{{ lookup('file', '/path/to/app.json') }}"
"""

from ansible.module_utils.basic import *
from ansible.module_utils.urls import *
from json import dumps, loads

def request(url, method, data):

    response, info = fetch_url(module=module, url=url, data=data, method=method,
                               headers={'Content-Type':'application/json'})

    if info['status'] not in (200, 201, 204):
        msg = {
          "description": "request failed",
          "url": url,
          "method": method,
          "data": data,
          "info": info
        }
        module.fail_json(msg=dumps(msg))

    body = response.read()

    if body:
        return loads(body)
    else:
        return {}

def put(url, data):
    return request(url, method='PUT', data=data)

def main():

    global module
    module = AnsibleModule(
        argument_spec=dict(
            marathon_uri=dict(required=True),
            app_id=dict(required=True),
            app_json=dict(required=True),
        ),
    )

    marathon_uri = module.params['marathon_uri']
    app_id = module.params['app_id']

    app_json = module.params['app_json']
    if isinstance(app_json, dict):
        app_json = dumps(app_json)

    if not marathon_uri.endswith('/'):
        marathon_uri = marathon_uri+'/'

    marathon_uri = marathon_uri+'v2/apps/'+app_id+'?force=true'

    try:
        ret = put(marathon_uri, app_json)
    except Exception, e:
        msg = {
          "description": "could not PUT to Marathon",
          "marathon_uri": marathon_uri,
          "app_json": app_json,
          "exception": repr(e)
        }
        return module.fail_json(msg=dumps(msg))

    module.exit_json(changed=True, meta=ret)

main()
