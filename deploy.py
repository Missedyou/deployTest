# -*- coding:utf-
import subprocess

def deploy():
    add = subprocess.Popen("git add .", shell=True)
    add.wait()
    print('add over')
    content = '格式化字符串测试'
    commit = subprocess.Popen("git commit -m %s"%content, shell=True)
    commit.wait()
    print('commit over')

    push = subprocess.Popen("git push origin master", shell=True)
    push.wait()
    print('push over')


if __name__ == '__main__':
    deploy()