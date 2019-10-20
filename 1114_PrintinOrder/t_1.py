class Foo:
    def __init__(self):
        self.d = {}  # 字典法 多线程问题

    def first(self, printFirst: 'Callable[[], None]') -> None:
        self.d[0] = printFirst
        self.res()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.d[1] = printSecond
        self.res()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.d[2] = printThird
        self.res()

    def res(self) -> None:
        if len(self.d) == 3:
            self.d[0]()
            self.d[1]()
            self.d[2]()
