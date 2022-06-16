<!-- PROJECT LOGO -->
<p align="center">
  <a href="https://axy.one">
    <img src="https://uploads-ssl.webflow.com/624eb8b8eb3aed6e1e68a7d2/625017e821a753ee6ea97551_Group%2048095812.svg" alt="Logo" width="80">
  </a>

  <p align="center">
    Phyllo Backend sample App
    <br />
    <br />
    <br />
    <a href="https://github.com/getphyllo/phyllo-python-sample">View Demo</a>
    ·
    <a href="https://github.com/getphyllo/phyllo-python-sample/issues">Report Bug</a>
    ·
    <a href="https://github.com/getphyllo/phyllo-python-sample/issues">Request Feature</a>
  </p>


<!-- TABLE OF CONTENTS -->

## Table of Contents

- [About the Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Dependencies](#dependencies)
  - [Installing](#installing)
  - [Usage](#usage)
    - [Run tests](#run-tests)
    - [Run Webhook](#webhook)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

<!-- ABOUT THE PROJECT -->

## About The Project
This app is a sample implementation of a basic client for our APIs as open-source code on GitHub to be able to strongly demonstrate the ideal technical integration with Phyllo

### Built With

- Python
- Fast Api

<!-- GETTING STARTED -->

## Getting Started


Simply clone or fork this repo and follow instructions.


## Dependencies
- Python 3.9
- pip

## Installing

#### Pre-requisties
- Your envionment variable should be populated in .env file in root directory, (take refrence from .env.example)

1. Clone the repo
2. Install pipenv package to make virtualenv for the project.
```sh
pip install pipenv
```
3. Setup virutalenv and Enter into virtual env
```sh
pipenv install
pipenv shell
```


4. Run the `main` file inside to app to start project
```sh
Python app/main.py
```

5. Now project should be up and running on port: 9000


### Run tests

- Run `main` file inside unit_test directory to run the Unit tests.
```
python unit_test/main.py
```

### Webhook 
- To test webhook, run `webhook_main` file inside Webhook directory
- webhook server should be up and running on port: 9003
- Create a public url for port: 9003 using `ngrok` and register the obtained url in sandbox.
- 


<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/akshaybhalotia/readme-template/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**. Sincere thanks to all our contributors. Thank you, [contributors](https://github.com/akshaybhalotia/readme-template/graphs/contributors)!

You are requested to follow the contribution guidelines specified in [CONTRIBUTING.md](./CONTRIBUTING.md) 

<!-- LICENSE -->

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

