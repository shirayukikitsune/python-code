def test_cases():
    files(
        name='test_cases',
        sources=['cases/**/*.txt'],
    )

    python_tests(
        dependencies=[
            'src/library/commons/io',
            ':test_cases',
        ]
    )
