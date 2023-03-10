'''
fabfile  -- deployment using Fabric
=================================================================

expecting local fabric.json with following content
    {
        "connect_kwargs": {
            "key_filename": sshkeyfilename (export OpenSSH key from puttygen)
        },
        "user": "appuser"
    }

execute as follows

    fab -H <target-host> deploy

or 

    fab -H <target1>,<target2> deploy

if you need to check out a particular branch

    fab -H <target-host> deploy --branchname=<branch>

'''

from fabric import task
from invoke import Exit

APP_NAME = 'webmodules'

@task
def deploy(c, branchname='main'):
    print(f'c.user={c.user} c.host={c.host} branchname={branchname}')

    venv_dir = f'/var/www/{c.host}/.venv'
    project_dir = f'/var/www/{c.host}/{APP_NAME}/{APP_NAME}'

    c.run(f'cd {project_dir} && git pull')
    
    if not c.run(f'cd {project_dir} && git show-ref --verify --quiet refs/heads/{branchname}', warn=True):
        raise Exit(f'branchname {branchname} does not exist')

    c.run(f'cd {project_dir} && git checkout {branchname}')
    
    # versions_dir = f'{project_dir}/migrations/versions'
    # if not c.run(f'test -d {versions_dir}', warn=True):
    #     c.run(f'mkdir {versions_dir}')

    # this needs to be run in container, after container is started
    # c.run(f'cd {project_dir} && source {venv_dir}/bin/activate && flask db upgrade')
