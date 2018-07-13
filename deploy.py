import subprocess

def deploy():
    add = subprocess.Popen("git add .", shell=True)
    add.wait()
    print('add over')

    # commit = subprocess.Popen("git commit -m 'test2'", shell=True)
    # commit.wait()
    # print('commit over')

    # push = subprocess.Popen("git push origin master", shell=True)
    # push.wait()
    # print('push over')


if __name__ == '__main__':
    deploy()