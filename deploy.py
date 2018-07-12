import subprocess
from git import Repo


RepoPath = '/Users/missyou/deployTest'


def deploy():
    # 执行hugo打包命令
    # pack = subprocess.Popen("hugo --theme=prefer --baseUrl='https://missedyou.github.io/'", shell=True)
    # pack.wait()

    # 进入打包后的文件夹
    shell_list = ['cd %s'%RepoPath, 'git add .', "git commit -m 'deploy script test'", 'git push']
    a = subprocess.Popen(shell_list, shell=True)

# 暂时无法使用,, 有空研究下
def push_to_remote():
    repo = Repo(RepoPath)

    # 切换分支
    repo.heads.master.checkout()

    # 暂存区文件处理
    index = repo.index
    index.add(['.'])
    index.commit('deploy script test')

    # 推送到远程
    remote = repo.remote()
    remote.pull()
    remote.push()


if __name__ == '__main__':
    deploy()
    # push_to_remote()