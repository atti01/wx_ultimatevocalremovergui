import unittest

# Assuming the test suite is set up using a list of test files
test_files = [
    'test_file1',
    'test_file2',
    'test_uvr',  # Add the new test file here
    # Add more test files as needed
]

def main():
    suite = unittest.TestSuite()

    for file in test_files:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(file))

    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    main()
