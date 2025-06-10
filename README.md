# test-suma README.md

# Test Suma

This project contains a simple implementation of a function that sums two numbers, along with automated tests to verify its correctness.

## Project Structure

```
test-suma
├── test_suma.py          # Contains the sum function and its tests
├── requirements.txt      # Lists the dependencies for the project
├── .github
│   └── workflows
│       └── python-tests.yaml  # GitHub Actions workflow for running tests
└── README.md             # Documentation for the project
```

## Installation

To set up the project, you need to install the required dependencies. You can do this by running:

```
pip install -r requirements.txt
```

## Usage

The main function in this project is `sumar(a, b)`, which takes two numbers as input and returns their sum. 

You can run the tests using pytest:

```
pytest test_suma.py
```

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.