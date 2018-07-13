# -*- coding:utf-
import subprocess
import sys, os

def deploy():
    add = subprocess.Popen("git add .", shell=True)
    add.wait()
    print('add over')
    
    commit_content = str(sys.argv[1])

    commit = subprocess.Popen("git commit -m %s"%commit_content, shell=True)
    commit.wait()
    print('commit over')

    push = subprocess.Popen("git push origin master", shell=True)
    push.wait()
    print('push over')


if __name__ == '__main__':
    deploy()