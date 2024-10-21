from anyio import run_process


async def exec_shell(cmd):
    """异步执行shell命令，返回stdout和stderr，
    cmd可传数组或者字符串，如: ['ls', '-al'] 或 'ls -al'"""
    ret = await run_process(cmd, check=False)
    return ret.stdout.decode("utf-8").strip(), ret.stderr.decode("utf-8").strip()


def print_succ(content):  # 绿色
    print(f"\033[32m{content}\033[0m")


def print_err(content):  # 红色
    print(f"\033[31m{content}\033[0m")
