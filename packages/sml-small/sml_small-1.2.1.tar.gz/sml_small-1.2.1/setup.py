# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sml_small',
 'sml_small.editing',
 'sml_small.editing.thousand_pounds',
 'sml_small.editing.totals_and_components',
 'sml_small.utils']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.3.5,<2.0.0']

setup_kwargs = {
    'name': 'sml-small',
    'version': '1.2.1',
    'description': 'SML Small (Python Pandas methods)',
    'long_description': '# SML-PYTHON-SMALL\n\n##### Statistical Methods Library for Python Pandas methods used in the **S**tatistical **P**roduction **P**latform (SPP).\n\nThis library contains pandas statistical methods that are only suitable for use on small datasets which can safely be processed in-memory.\n\nFor further information about the methods contained in this module see the [method specifications](https://github.com/ONSdigital/Statistical-Method-Specifications)\n\nFor user documentation and example data relating to the methods in this module see the [supporting information](https://github.com/ONSdigital/sml-supporting-info)\n\n### Automated testing\nIn order to ensure code quality, there is a manual test script provided __run_py_tools.sh__ which will run linting, code formatting checks, and the pytest suite. \n\nIt is often easy to forget to check code formatting before pushing to the remote repository, so there is the option of running the testing script automatically by using the git hook __pre-push__. This means that when __git push__ is run, the test script will be run first, and will abort the push if any of the tests fail.\n\nGit hooks cannot be pushed to the remote repository so if you would like this script to be run automatically you will need to follow these steps:\n\n - Check that the __.git__ directory is present in your repository by running __ls -a__ in the terminal\n - Run __cd .git/hooks__ and open the file marked __pre-push.sample__ in a code editor\n - Replace the content of this file with the following code:\n ```bash\n#!/bin/sh\nGREEN=\'\\033[1;32m\'\nRED=\'\\033[1;31m\'\nYELLOW=\'\\033[1;33m\'\nNC=\'\\033[0m\'\n\ngit stash clear # in case there is nothing to stash,\n# then the stash needs to be empty, else previously \n# stashed changes will be incorrectly restored\n\ngit stash\ntesting_script="./run_py_tools.sh"\n\n\nif "$testing_script"; then\n    echo "${GREEN}./run_py_tools script passes, proceeding with push...${NC}"\n    git add . # commit any changes made by the pytools script\n    git commit -m "run_py_tools auto-formatting"\n    git stash apply\n    echo "${YELLOW}NOTE: If any commits were made by the auto-formatting tool, then they will not be automatically pushed. You will need to run git push again (or git push --no-verify if you don\'t want to run the test suite again).${NC}"\n    # uncomment the line below if you would like the commits to be pushed automatically.\n    # git push --no-verify # NOTE: this will cause git to throw an error, but the functionality is correct.\n    exit 0\nelse\n    echo "${RED}./run_py_tools script fails, push aborted.${NC}"\n    git checkout . # revert any changes made by the pytools script\n    git stash apply\n    exit 1\nfi\n\n```\n- Save the file and __rename it to pre-push__ (i.e. remove the .sample suffix from the filename)\n- Run __cd ../..__ to change the current working directory back to the root directory of the sml-python-small repository\n- Open a poetry shell and run __git push__ to check if the testing tools work (it doesn\'t matter if there is nothing to push, the pre-push hook will still run).\n- After all of the tests have run, you should see something like this:\n```bash\n================================================================================= 443 passed in 12.58s ==================================================================================\nTest Results:\nblack --check --diff sml_small tests    : Success\nflake8 sml_small tests                  : Success\nisort --check-only .                    : Success\nbandit -c pyproject.toml -r .           : Success\n./run_py_tools script passes, proceeding with push...\nEverything up-to-date\n```\n- If any of the linting tests or pytest files fail then the push will be aborted.\n\n#### Troubleshooting\n - In order to push, you need to run the __git push__ command in a poetry shell, otherwise all of the tests will fail.\n - You also need to ensure that your current working directory in the terminal is within the sml-python-small repository.\n - While the script is running, any non-committed changes will be stashed. This means that any work after the commit has been made may seem to disappear for a moment during the tests. After the file has finished running, the stashed changes will be automatically restored. This is to ensure that the tests are being run on the code within the commits, rather than any non-committed changes.\n - If for any reason the script exits unexpectedly, you can restore the stashed changes manually by running the following command:\n```bash\ngit stash apply\n```\n - If any changes are made by the auto-formatting tool, then these will automatically be committed, but it is not possible to automatically push these changes. You can check by running __git log__. If the most recent commit is titled \'run_py_tools auto-formatting\', then you will need to run __git push__ again (or __git push --no-verify__ if you don\'t want to run the test suite again).\n - If you would like these commits to be pushed automatically, then you can uncomment the __git push --no-verify__ line in the code. This is optional, since pushing during the pre-push hook will cause git to throw an error, however the functionality is correct.',
    'author': 'None',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
