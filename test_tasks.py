import unittest
from app.database import add_task, get_tasks, init_db

class TestTasks(unittest.TestCase):

    def setUp(self):
        init_db()

    def test_add_task(self):
        add_task("Test Task")
        tasks = get_tasks()
        self.assertTrue(len(tasks) > 0)

if __name__ == "__main__":
    unittest.main()