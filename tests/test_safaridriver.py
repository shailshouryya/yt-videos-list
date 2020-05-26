from test_shared import create_test_cases, run_test_case


def main():
    browsers   = ['safari']
    test_cases = create_test_cases(browsers)

    for test_case in test_cases:
        run_test_case(test_case)
        print('Moving on to the next driver...\n' + '⏬ '*11)


if __name__ == '__main__':
    main()
