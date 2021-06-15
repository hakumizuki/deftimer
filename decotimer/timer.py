import time
from inspect import getframeinfo, currentframe
from contextlib import contextmanager
from .exceptions import TimerError
# TODO: linenoの使い方を考える
# TODO: BlocksをSortして表示するオプション
# TODO: block()をsleep()で誤差検査

class Timer:
    """Timer class"""
    _start = None
    _end = None
    _global_time = None
    _global_paused_time = None
    _global_total = None
    pause_resume = None
    blocks = None
    _paused_blocked_total = None
    # Optional arguments
    user = None
    description = None
    # States
    _paused = False
    _stopped = False
    _cpython = None
    # File info
    filename = None


    def __init__(self, user='', description=''):
        """Initializer
        @params _*: float, time parameters for calculation
        @param pause_resume: List of intervals generated by pause and resume methods. Used for calculating _global_paused_time
        [
            {
                'pause': float,
                'resume': float
            }
        ]

        @param blocks: List of blocks generated by block method
        [
            {
                'name': str,
                'time': float,
                'line': int
            }
        ]

        @params user, description: str, Optional info
        """
        self._start = 0
        self._end = 0
        self._global_time = 0
        self._global_paused_time = 0
        self._global_total = 0
        self.pause_resume = []
        self.blocks = []
        self._paused_blocked_total = 0

        self.user = user
        self.description = description

        self._get_fileinfo()
        assert self._cpython is not None

    def use_timer(self, func, detail=True):
        """Main wrapper"""
        def wrapper(*args, **kwargs):
            # Start timer
            self._start = time.time()
            func(*args, **kwargs)
            if not self._stopped:
                self._end = time.time()
            if self._paused:
                raise TimerError(self._paused, 'You must call resume() after calling pause()')
            # Calculation and Result
            self._calculate_result()
            self._show_detail_result() if detail else self._show_short_result()
        return wrapper

    def pause(self):
        """Pause timer
        @usage:
        timer.pause()
        process()
        """
        if self._stopped:
            raise TimerError(_stopped, 'You cannot call pause() after calling stop()')

        if self._paused:
            raise TimerError(_paused, 'Paused twice in a row')

        self.pause_resume.append({
            'pause': time.time(),
            'resume': None
        })
        self._paused = True

    def resume(self):
        if self._stopped:
            raise TimerError(_stopped, 'You cannot call resume() after calling stop()')

        if not self._paused:
            raise TimerError(self._paused, 'You cannot call resume() before calling pause()')

        self.pause_resume[-1]['resume'] = time.time()
        self._paused = False

    def stop(self):
        """Stop timer"""
        if self._stopped:
            raise TimerError(_stopped, 'Stopped twice')
        self._end = time.time()

    @contextmanager
    def block(self, name=None, exclude=False):
        """block context manager
        @param name: str or None, Block name
        @param exclude: bool, Determine if you exclude the process time from global timer or not
        @usage:
        with timer.block(name='email', exclude=True):
            email(to='example@example.com')
        """
        # Block detected
        self.blocks.append({
            'name': name,
            'line': None,
            'time': None
        })
        block_start = time.time()
        try:
            yield
        finally:
            if exclude:
                self.blocks[-1]['time'] = 'Skipped'
            else:
                self.blocks[-1]['time'] = time.time() - block_start
            # TODO: self.blocks[-1]['line'] = self._get_lineno()
            self.blocks[-1]['line'] = 'Coming soon...'

    ##############################
    # Timer Class Static methods #
    ##############################
    @staticmethod
    def timer(func):
        """Simple timer function
        @usage:
        timer.timer(func)
        """
        s = time.time()
        func()
        e = time.time()
        print('-----------------------------------------')
        print(f'Program ran in --> {e - s} s')
        print('-----------------------------------------')

    #############################
    # Timer Class Class methods #
    #############################
    @classmethod
    def params(cls):
        """Show class info"""
        print('Thx for using Timer:) montanha.masu536@gmail.com')
        print('__class__: ', cls.__class__)
        print('__dict__', cls.__dict__)

    ###############################
    # Timer Class Private methods #
    ###############################
    def _calculate_result(self):
        self._global_time = self._end - self._start
        for item in self.pause_resume:
            self._global_paused_time += item['resume'] - item['pause']

        self._global_total += self._global_time
        for item in self.blocks:
            if isinstance(item['time'], float): # exclude excluded -> 'Skipped'
                self._global_total -= item['time']
                self._paused_blocked_total += item['time']
        
        self._paused_blocked_total += self._global_paused_time

    def _show_detail_result(self):
        """Show full info"""
        print()
        print('-----------------------------------------')
        print(f'Result                --> {self._global_total} s')
        print(f'Whole program ran in  --> {self._global_time} s')
        print(f'Paused                --> {self._global_paused_time} s, {len(self.pause_resume)}times')
        print(f'Blocks                --> {self.blocks}')
        print(f'Paused + Blocked      --> {self._paused_blocked_total} s')
        print('-----------------------------------------')


    def _show_short_result(self):
        """Show short info"""
        print()
        print('-----------------------------------------')
        print(f'Result  --> {self._global_total} s')
        print(f'blocks  -->\n{self.blocks}')
        print('-----------------------------------------')

    def _get_fileinfo(self):
        """Call this method first
        @desc:
        It checks if the program can get frame or not. If not, it sets _cpython param to False. When _cpython is False, you cannot get fileinfo or line number.
        """
        frame = None
        try:
            frame = currentframe()
            self.filename = getframeinfo(frame).filename
            self._cpython = True
        except Exception:
            self._cpython = False
            self.filename = 'ONLY available on CPython interpreter.'

    def _get_lineno(self):
        """Available on CPython Only"""
        if not self._cpython:
            return 'ONLY available on CPython interpreter.'
        return getframeinfo(currentframe()).lineno