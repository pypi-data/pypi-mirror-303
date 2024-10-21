import unittest
from aerialog import Logger

class TestOutput(unittest.TestCase):
    def test_output(self):
        logger = Logger()
        logger.fatal("This is a fatal message.")
        logger.error("This is an error message.")
        logger.warn("This is a warning message.")
        logger.info("This is an info message.")
        logger.debug("This is a debug message.")
        logger.silly("This is a silly message.")

        logger.set_file("test.log")
        logger.fatal("This is a fatal message.")
        logger.error("This is an error message.")
        logger.warn("This is a warning message.")
        logger.info("This is an info message.")
        logger.debug("This is a debug message.")
        logger.silly("This is a silly message.")
        logger.remove_file()
        
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()