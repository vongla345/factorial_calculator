# Streamlit Factorial App

This is a simple Python web application built with **Streamlit** that allows users to:

- Log in with a username and password  
- Compute the factorial of a number  
- Easily deploy and run locally or on a server  

## Features

- Basic login authentication  
- Factorial calculator (for non-negative integers)  
- Deployable using `streamlit run`  
- User input validation  

## Project Structure

```bash
factorial_app/
├── factorial.py
├── main.py
├── user.py  
└── README.md
```

## Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/vongla345/factorial_calculator.git  
    cd factorial_calculator  
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt  
    ```
3. Run the app:

    ```bash
    streamlit run main.py
    ```

## Authentication

This app uses a simple .txt file for user authentication.

Example:
    admin 1234
    guest guest
You can modify the user credentials directly in the file.

## Functionality

After logging in, users can input a non-negative integer and get its factorial result instantly.

## Built With

- Python 3.x  
- Streamlit

## License

This project is open source and available under the MIT License.
