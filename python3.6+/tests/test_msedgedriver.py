from test_shared import create_test_cases, run_test_case


def main():
    browsers   = ['edge']
    test_cases = create_test_cases(browsers)

    for test_case in test_cases:
        run_test_case(test_case)


if __name__ == '__main__':
    main()
