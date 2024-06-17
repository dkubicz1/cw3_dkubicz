import unittest
from todo import add_task, get_tasks

class TestTodoApp(unittest.TestCase):
    def setUp(self):
        # Reset the tasks list before each test
        global tasks
        tasks = []

    def test_add_task(self):
        self.assertEqual(add_task("Buy milk"), "Buy milk")
        self.assertEqual(len(get_tasks()), 1)

    def test_get_tasks(self):
        add_task("Buy milk")
        add_task("Walk the dog")
        self.assertEqual(get_tasks(), ["Buy milk", "Walk the dog"])

if __name__ == "__main__":
    unittest.main()
