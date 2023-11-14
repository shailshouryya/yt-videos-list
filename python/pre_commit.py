import os
import subprocess

from typing import List

import mypy.main
import pylint.lint


MYPY_FLAGS = [
    '--strict',
    '--show-error-context',
    '--show-column-numbers',
    '--show-error-end',
    '--pretty',
    '--show-absolute-path',
    ]


def main(
) -> None:
    changed_py_files = subprocess.getoutput('git diff --name-only --staged "*.py"').splitlines()
    lint_changed_py_files(changed_py_files)
    locations_to_test = collect_mypy_information(changed_py_files)
    run_mypy_commands(locations_to_test)


def lint_changed_py_files(
    changed_py_files: List[str],
) -> None:
    config_path    = os.path.join('python', '.pylintrc')
    pylint_options = f'--rcfile={config_path}'
    for changed_py_file in changed_py_files:
        # pylint.run_pylint(pylint_options + [changed_py_file])
        # # calls pylint.lint.Run(argv or sys.argv[1:])
        # # but does not allow specifying the reporter, exit, do_exit
        # # arguments to pylint.lint.Run.__init__
        pylint.lint.Run(args=[pylint_options, changed_py_file], exit=False)


def collect_mypy_information(
    changed_py_files: List[str],
) -> List[List[str]]:
    # the pre-commit file located in ./.git/hooks/pre-commit
    # calls this (pre_commit.py) module from the
    # top level yt-videos-list directory,
    # so this module needs to reference the
    # yt-videos-list/python directory
    # via `python.dev` and `python.yt_videos_list`
    # in order to find the
    # dev and yt_videos_list packages
    packages_to_test: List[List[str]] = [
        ['-p', 'python.dev'],
        ['-p', 'python.yt_videos_list'],
    ]
    individual_files_to_test: List[List[str]] = [
        [changed_py_file]
        for changed_py_file in changed_py_files
    ]
    locations_to_test = [
        *packages_to_test,
        *individual_files_to_test
    ]
    return locations_to_test



def run_mypy_commands(
    locations_to_test:      List[List[str]],
) -> None:
    for location_to_test in locations_to_test:
        mypy_arguments = MYPY_FLAGS + location_to_test
        print(f'''mypy {' '.join(mypy_arguments)}''')
        try:
            mypy.main.main(args=mypy_arguments, clean_exit=True)
        except SystemExit:
            # when mypy finds any errors in the program file(s) it analyzed,
            # it calls sys.exit(either_0_or_1) after it finishes
            # running the mypy command - this prevents
            # anything else from running after the current mypy command,
            # which is problematic in a situation like this where we
            # may have more things we want to do after running a
            # mypy command that finds some errors (such as running more
            # mypy commands on other modified files)
            # in this case, we just ignore the SystemExit and continue
            # analyzing locations_to_test (if there are still items to
            # analyze)
            continue


if __name__ == '__main__':
    main()
