import os


class Register(object):
    @classmethod
    def add_process(cls, pid: int):
        with open('/tmp/worker', 'w') as f:
            f.write(str(pid))

    @classmethod
    def unregister_process(cls, pid: int):
        with open('/tmp/worker', 'w') as f:
            f.write(str(-1*pid))

    @classmethod
    def auto_register(cls):
        pid = os.getpid()
        cls.add_process(pid)

    @classmethod
    def auto_unregister(cls):
        pid = os.getpid()
        cls.unregister_process(pid)
