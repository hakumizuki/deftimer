import unittest
import time
from decotimer.timer import Timer

class TestTimer(unittest.TestCase):
    def test_should_initialize_timer(self):
        timer = Timer(user='user', description='description')
        self.assertEqual(timer.user, 'user')
        self.assertEqual(timer.description, 'description')
        self.assertEqual(timer.description, 'description')
        self.assertTrue(isinstance(timer.filename, str))
        self.assertTrue(timer._cpython is not None)


class TestTimerUseTimerDecorater(unittest.TestCase):
    def setUp(self):
        self.timer = Timer(user='user', description='description')

    def test_use_timer_decorator_without_actions(self):
        @self.timer.use_timer
        def some_process():
            a = 10**10
            b = a**10

        some_process()
        self.assertTrue(self.timer._start > 0)
        self.assertTrue(self.timer._end > 0)
        self.assertAlmostEqual(self.timer._global_time, 0.00, 2)
        self.assertAlmostEqual(self.timer._global_paused_time, 0.00, 2)
        self.assertAlmostEqual(self.timer._global_total, 0.00, 2)
        self.assertEqual(self.timer.pause_resume, [])
        self.assertEqual(self.timer.blocks, [])
        self.assertEqual(self.timer._paused_blocked_total, 0)

    def test_use_timer_decorator_with_pause_resume(self):
        self.pause_time = None
        self.resume_time = None

        @self.timer.use_timer
        def some_process():
            time.sleep(0.5)
            self.pause_time = time.time()
            self.timer.pause()
            time.sleep(0.5)
            self.timer.resume()
            self.resume_time = time.time()

        some_process()
        self.assertTrue(self.timer._start > 0)
        self.assertTrue(self.timer._end > 0)
        self.assertAlmostEqual(self.timer._global_time, 1.00, 1)
        self.assertAlmostEqual(self.timer._global_paused_time, 0.50, 2)
        self.assertAlmostEqual(self.timer._global_total, 0.5, 1)
        self.assertAlmostEqual(self.timer.pause_resume[0]['pause'], self.pause_time, 2)
        self.assertAlmostEqual(self.timer.pause_resume[0]['resume'], self.resume_time, 2)
        self.assertEqual(self.timer.blocks, [])
        self.assertAlmostEqual(self.timer._paused_blocked_total, 0.50, 2)

    def test_use_timer_decorator_with_one_block(self):
        self.block_start_time = None
        self.block_end_time = None

        @self.timer.use_timer
        def some_process():
            time.sleep(0.5)
            self.block_start_time = time.time()
            with self.timer.block(name='sleep', exclude=True):
                time.sleep(0.5)
            self.block_end_time = time.time()

        some_process()
        self.assertTrue(self.timer._start > 0)
        self.assertAlmostEqual(self.timer._end, self.block_end_time, 2)
        self.assertAlmostEqual(self.timer._global_time, 1.0, 1)
        self.assertAlmostEqual(self.timer._global_paused_time, 0.00, 2)
        self.assertAlmostEqual(self.timer._global_total, 0.5, 1)
        self.assertEqual(self.timer.pause_resume, [])
        self.assertAlmostEqual(self.timer.blocks[0]['time'], self.block_end_time - self.block_start_time, 2)
        self.assertAlmostEqual(self.timer._paused_blocked_total, 0.50, 1)
