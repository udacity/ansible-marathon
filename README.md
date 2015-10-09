ansible-marathon is an [Ansible][ansible] module for deploying
applications to [Marathon][marathon].

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

See [examples/nodejs-rest-api/nodejs-rest-api-v1.json][app.json] from
[capgemini:Apollo][apollo].

## Usage

```
$ ansible-playbook -i inventory.ini -M /path/to/ansible-marathon playbook.yml
```

[ansible]: http://docs.ansible.com/ansible/index.html
[marathon]: http://mesosphere.github.io/marathon/
[app.json]: https://github.com/capgemini/Apollo/blob/master/examples/nodejs-rest-api/nodejs-rest-api-v1.json
[apollo]: https://github.com/capgemini/Apollo/
