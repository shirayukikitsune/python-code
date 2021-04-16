def test_cases(**kwargs):
    folder = kwargs["test_folder"]
    files(
        name='test_cases',
        sources=['../../../../../tests/' + folder + '/**/*.txt'],
    )

    python_tests(
        dependencies=[
            'src/library/commons/io',
            ':test_cases',
        ]
    )
