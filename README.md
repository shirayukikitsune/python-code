# Python Code

This monorepo contains the code for all activities during my graduation course

## Required tools

- [Python 3.8+][python]
- [Pants][pants-build] (included)
- [direnv][direnv]

### Setting up direnv:

1. [Install direnv](https://direnv.net/docs/installation.html)
    - MacOS: `brew install direnv`
    - Debian/Ubuntu: `sudo apt install direnv`
2. [Setup your shell](https://direnv.net/docs/hook.html)
    - BASH: `echo 'eval "$(direnv hook bash)"' >> ~/.bashrc`
    - ZSH: `echo 'eval "$(direnv hook zsh)"' >> ~/.zshrc`
3. Allow the direnv: `direnv allow`

## Folder structure

- `src` - this is where all Python files are located
  - `main` - this is where the activity code is found
    - `lp` - code for the programming languages course
  - `test` - this is where the tests for a solution are found

## How to run a specific solution

Just run the following bash command:

    ./pants run <path_to_project>

For example:

    ./pants src/main/lp/ambientacao/average_1

## How to test a specific solution

Just run the following command:

    ./pants test <path_to_test>

For example:

    ./pants test src/test/lp/ambientacao/average_1

[pants-build]: https://www.pantsbuild.org/
[python]: https://www.python.org/
[direnv]: https://direnv.net/