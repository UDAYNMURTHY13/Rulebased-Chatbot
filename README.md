
# UDAY's Chatbot

This project implements a simple rule-based chatbot using Flask for the web interface.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Flask
- Virtual Environment (optional but recommended)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```

2. **Create and activate a virtual environment (optional but recommended):**

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up your environment variables:**

    - Ensure you have set the `GEMINI_API_KEY` environment variable with your API key.

    ```sh
    export GEMINI_API_KEY='your_api_key_here'
    ```

## Usage

1. **Run the Flask application:**

    ```sh
    python app.py
    ```

2. **Open your web browser and go to:**

    ```
    http://127.0.0.1:5000/
    ```

3. **Interact with the chatbot:**

    - Type your input in the chat interface and see the responses from the chatbot.

## Project Structure
│
├── app.py               # Main Flask application
├── chatbot.py           # Rule-based chatbot logic
├── templates/
│   └── index.html       # HTML template for the web interface
└── README.md            # This README file
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Flask: https://flask.palletsprojects.com/
- Python: https://www.python.org/

## Running the Project in Visual Studio Code

1. **Open the project in Visual Studio Code:**

    - Launch Visual Studio Code.
    - Open the cloned repository folder.

2. **Set up the Python interpreter:**

    - Open the Command Palette (`Ctrl+Shift+P`).
    - Type `Python: Select Interpreter` and select the Python interpreter from your virtual environment (e.g., `venv`).

3. **Configure environment variables:**

    - Create a `.env` file in the root of your project and add the following line:

        ```
        GEMINI_API_KEY=your_api_key_here
        ```

4. **Install the Python extension:**

    - If you haven't already, install the Python extension for Visual Studio Code.

5. **Run the Flask application:**

    - Open the terminal in Visual Studio Code (`Ctrl+` `).
    - Ensure your virtual environment is activated:

        ```sh
        source venv/bin/activate  # On Windows use `venv\Scripts\activate`
        ```

    - Run the application:

        ```sh
        python app.py
        ```

6. **Access the application:**

    - Open your web browser and navigate to `http://127.0.0.1:5000/`.

7. **Interacting with the Chatbot:**

    - Type your messages in the chat interface and interact with the chatbot.

## Important Notes

- Ensure that your `GEMINI_API_KEY` is valid and correctly set up in your environment.
- The `chatbot.py` file should contain the rule-based chatbot logic as defined in the provided code.

```

