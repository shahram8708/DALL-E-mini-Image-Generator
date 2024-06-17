# DALL-E-mini Image Generator

## Overview

The DALL-E-mini Image Generator is a web application built with Flask that allows users to generate images based on textual descriptions using OpenAI's DALL-E-mini model. This application provides a simple and intuitive interface where users can enter descriptive text, and upon submission, the backend interacts with the DALL-E-mini API to retrieve and display the corresponding image.

### Features

- **Text Input**: Users can input descriptive text to specify what they want to see in the generated image.
- **Image Generation**: Upon submitting the text description, the application sends a request to the DALL-E-mini API and displays the generated image.
- **Responsive Design**: The application is designed to be responsive, ensuring a seamless user experience across devices.

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Installation Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/shahram8708/DALL-E-mini-Image-Generator.git
   cd dalle-mini-image-generator
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:

   - Obtain an API key from OpenAI for accessing the DALL-E-mini API.
   - Create a `.env` file in the root directory and add your API key:

     ```plaintext
     OPENAI_API_KEY="your_openai_api_key_here"
     ```

5. Start the Flask server:

   ```bash
   flask run
   ```

6. Open your web browser and navigate to `http://localhost:5000` to use the application.

## Usage

1. Enter a descriptive text in the textarea provided on the homepage.
2. Click the "Generate Image" button to submit the text and initiate image generation.
3. The application will display the generated image below the input area.

## Technologies Used

- **Python**: Backend server-side scripting language.
- **Flask**: Micro web framework for Python used to build the web application.
- **HTML/CSS/JavaScript**: Frontend technologies for creating the user interface and handling user interactions.
- **OpenAI DALL-E-mini API**: AI model for generating images from textual descriptions.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- OpenAI for providing access to the DALL-E-mini model and API.
- Flask and requests libraries for simplifying backend development and HTTP requests.

## Author

- Shah Ram
- GitHub: [Shah Ram](https://github.com/shahram8708)
