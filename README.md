ansible-marathon is an [Ansible][1] module for deploying
applications to [Marathon][2].

## Example

*inventory.ini:*

```ini
localhost ansible_connection=local
```

*playbook.yml:*

```yaml
- name: Deploy to Marathon
  marathon:
    marathon_uri: https://localhost:8080/
    app_id: nodejs-rest-api
    app_json: "{{ lookup('file', '/path/to/app.json') }}"
```

*app.json:*

See [examples/nodejs-rest-api/nodejs-rest-api-v1.json][3] from
[capgemini:Apollo][4].

## Usage

```
$ pip install --user ansible-marathon
$ ansible-playbook -i inventory.ini -M ~/.local/lib/python2.7/site-packages/ansible_marathon playbook.yml
```

## Development

To release a new version of ansible-marathon:

1. Configure *~/.pypirc*:

    ```
    [server-login]
    username: YOUR_PYPI_USERNAME
    password: YOUR_PYPI_PASSWORD

    [pypi]
    repository: https://pypi.python.org/pypi

    [pypitest]
    repository: https://testpypi.python.org/pypi
    ```

1. Update the version number in *setup.py*
1. Commit all changes
1. Add a version tag to git: `git tag 0.1`
1. Publish to PyPI: `python setup.py sdist upload -r pypi`

[1]: http://docs.ansible.com/ansible/index.html
[2]: http://mesosphere.github.io/marathon/
[3]: https://github.com/capgemini/Apollo/blob/master/examples/nodejs-rest-api/nodejs-rest-api-v1.json
[4]: https://github.com/capgemini/Apollo/
