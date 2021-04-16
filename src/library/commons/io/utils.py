import functools
import io
import os
import os.path
import sys


def run_test_case(test_fn, input_file, output_file, *args, **kwargs):
    # Store stdin/stdout
    stdin = sys.stdin
    stdout = sys.stdout

    # Create an StringIO that will receive stdout
    with io.StringIO() as output_stream, io.open(input_file) as input_stream:
        # Redirect stdin from the input_file
        sys.stdin = input_stream
        # Redirect stdout to the StringIO
        sys.stdout = output_stream
        # Load expected output
        with io.open(output_file) as file:
            expected = file.read()

        # Execute the subject function
        test_fn(*args, **kwargs)

        # Capture the output
        got = output_stream.getvalue()

    # Reset things
    sys.stdin = stdin
    sys.stdout = stdout

    # Assert!
    assert got == expected


def run_tests_with_io(test_folder):
    def decorator(test_fn):
        @functools.wraps(test_fn)
        def wrapper(*args, **kwargs):
            # Scan directories inside test folder
            for entry in os.listdir(test_folder):
                print('Checking dir "%s"' % entry)
                input_file = test_folder + '/' + entry + '/input.txt'
                output_file = test_folder + '/' + entry + '/output.txt'
                if os.path.isfile(input_file) and os.path.isfile(output_file):
                    print('Running test case "%s"' % entry)
                    run_test_case(test_fn, input_file, output_file, *args, **kwargs)
        return wrapper
    return decorator
