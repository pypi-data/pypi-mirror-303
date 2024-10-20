from queue import Queue
from DrissionPage._base.driver import Driver
from time import perf_counter, sleep

class Listen_Console:
    def __init__(self,page) -> None:
        """
        :param page: ChromiumBase对象
        """
        self._page = page
        self._address = page.address
        self._target_id = page._target_id
        self._driver = None

        self._caught = None

        self.listening = False

    def start(self):
        """
        开启console-api监听
        """
        self.clear()
        self._driver = Driver(self._target_id, "page", self._address)
        self._driver.run("Console.enable")
        self._set_callback()
        self.listening = True


    def stop(self):
        """停止监听，清空已监听到的列表"""
        if self.listening:
            self.pause()
            self.clear()
        self._driver.stop()
        self._driver = None

    def pause(self, clear=True):
        """暂停监听
        :param clear: 是否清空已获取队列
        :return: None
        """
        if self.listening:
            self._driver.set_callback('Console.messageAdded', None)
            self.listening = False
        if clear:
            self.clear()

    def clear(self):
        self._caught = Queue(maxsize=0)

    def steps(self, count=None, timeout=None, gap=1):
        caught = 0
        end = perf_counter() + timeout if timeout else None
        while True:
            if timeout and perf_counter() > end:
                return
            if self._caught.qsize() >= gap:
                yield self._caught.get_nowait() if gap == 1 else [
                    self._caught.get_nowait() for _ in range(gap)
                ]
                if timeout:
                    end = perf_counter() + timeout
                if count:
                    caught += gap
                    if caught >= count:
                        return
            sleep(0.05)

    def _set_callback(self):
        self._driver.set_callback("Console.messageAdded", self._console)

    def _console(self, **kwargs):
        self._caught.put(kwargs)
