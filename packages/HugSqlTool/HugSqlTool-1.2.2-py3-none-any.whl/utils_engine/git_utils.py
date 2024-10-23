import subprocess


def get_git_user_name():
    user_name = 'None'
    try:
        work = subprocess.Popen(['git', 'config', 'user.name'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = work.communicate()
        if work.returncode != 0:
            print(format(stderr))
        if isinstance(stdout, str):
            user_name = stdout
        elif isinstance(stdout, bytes):
            user_name = stdout.decode('utf-8')
        else:
            print(format(stdout))

    except Exception as err:
        print(format(err.message))
    return user_name


if __name__ == '__main__':
    name = get_git_user_name()
    print(name)
