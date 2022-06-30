<!-- PROJECT LOGO -->
<p align="center">
  <a href="https://getphyllo.com">
    <img src="https://uploads-ssl.webflow.com/624eb8b8eb3aed6e1e68a7d2/625017e821a753ee6ea97551_Group%2048095812.svg" alt="Logo" width="120">
  </a>

  <h2 align="center">Python Sample by Phyllo</h2>
  <p align="center">
    Phyllo backend implementation sample / boilerplate in Python
    <br />
    <a href=""><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://demo.getphyllo.com">View Demo</a>
    ·
    <a href="https://github.com/getphyllo/phyllo-python-sample/issues">Report Bug</a>
    ·
    <a href="https://github.com/getphyllo/phyllo-python-sample/issues">Request Feature</a>
  </p>
</p>

<div align="center">(insert badges here)</div>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [About the Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Dependencies](#dependencies)
  - [Installing](#installing)
  - [Usage](#usage)
    - [Run locally](#run-project-locally)
    - [Run tests](#run-tests)
  - [Help](#help)
- [Versioning](#versioning)
  - [Version History](#version-history)
- [Contributing](#contributing)
- [Support](#support)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [About Authors](#about-authors)

<!-- ABOUT THE PROJECT -->

## About the Project

This app is a sample implementation of a basic client for our APIs. In its current form, this is just a pass through - meaning all the requests you send to it are sent to our APIs without any modifications and all the responses received from our APIs are sent to you without any modifications. This demonstrates an ideal technical integration with Phyllo. You can use this to see how things work, to help you with your local dev work, or even as a starting boilerplate to customize by adding your business logic.

### Built With

- [Python](https://www.python.org/)
- [Fast API](https://fastapi.tiangolo.com/)

<!-- GETTING STARTED -->

## Getting Started

Simply clone or fork this repo and follow the instructions.

## Dependencies

- Python 3.9 or above (check your OS-specific instructions at https://www.python.org/downloads/)
- pip

  ```
  python -m ensurepip --upgrade
  ```

- Your Phyllo API credentials should be populated in the `.env` file in the root directory, take reference from the `.env.example` file.

## Installing

1. Clone the repo.
2. Install `pipenv` package to make a virtual environment for the project.

   ```sh
   pip install pipenv
   ```

3. Setup and enter the virtual environment.

   ```sh
   pipenv install
   pipenv shell
   ```

4. Run the `main` file inside to app to start the project.

   ```sh
   python app/main.py
   ```

5. The project should be up and running on port 9000.

## Usage

### Run locally

You can make requests to any API endpoints by using the same path as described in [our API documentation](https://docs.getphyllo.com/docs/api-reference/api/ref) with the base URL as your localhost. For example, to [create a user](https://docs.getphyllo.com/docs/api-reference/api/ref/operations/create-a-v-1-user), you could send a `POST` request to `localhost:9000/v1/users` and it would behave the same as our API does.

#### Run webhooks locally

- To test webhooks, run the `webhook_main` file inside the `app/webhook` directory.

  ```
  python app/webhook/webhook_main.py
  ```

- The webhook server should be up and running on port 9003.
- Create a public URL for port 9003 using `ngrok` (or a similar [tunneling tool](https://github.com/anderspitman/awesome-tunneling)) and register the obtained URL in the sandbox.
- Send [mock requests to the webhook](https://docs.getphyllo.com/docs/api-reference/api/ref/operations/create-a-v-1-webhook-send) to check if everything works as expected.
- If you are doing frontend development, you would keep getting auto-generated webhooks when you connect accounts.

### Run tests

- Run the `main` file inside the `unit_tests` directory to run the unit tests.

  ```
  python unit_tests/main.py
  ```

### Help

See the [open issues](https://github.com/getphyllo/phyllo-python-sample/issues) for a list of proposed features (and known issues).

To get any help regarding this app, please join our Discord community using this invite link.

<!-- CHANGELOG -->

## Versioning

We use [SemVer](https://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/getphyllo/phyllo-python-sample/tags).

### Version history

See [CHANGELOG](./CHANGELOG.md).

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**. Sincere thanks to all our [contributors](https://github.com/getphyllo/phyllo-python-sample/graphs/contributors)!

You are requested to follow the contribution guidelines specified in [CONTRIBUTING.md](./CONTRIBUTING.md) :smile:.

## Support

Contributions, issues, and feature requests are welcome!
Give a ⭐️ if you like this project!

If you like what we do here at Phyllo, help us spread the word through a tweet or a post.

<!-- LICENSE -->

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## Acknowledgments

This repo is inspired by:

- [dyte](https://github.com/dyte-in/backend-sample-app)
- [akshaybhalotia](https://github.com/akshaybhalotia/readme-template)

## About Authors

`phyllo-python-sample` is created & maintained by Phyllo, Inc. You can find us on Twitter - [@getphyllo](https://twitter.com/getphyllo) or join our Discord community using this invite link.

The names and logos for Phyllo are trademarks of Phyllo, Inc.

We :heart: open-source software! See [our other projects](https://github.com/getphyllo) and check out [our products](https://getphyllo.com).
