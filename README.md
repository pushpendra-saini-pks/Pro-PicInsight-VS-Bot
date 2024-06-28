# Pro-PicInsight VS-Bot

Pro-PicInsight VS-Bot is an advanced chatbot application powered by the Gemini LLM (Large Language Model). It generates insightful and accurate responses based on both text prompts and images, providing real-time, user-friendly interactions.

## Features

- **Interactive Q&A Interface**: Ask questions and get responses based on text and images.
- **Real-Time Responses**: Powered by Google’s Gemini AI for fast and accurate answers.
- **User-Friendly Design**: Easy to use interface for seamless interaction.

## Demo

Check out the live demo: [Pro-PicInsight VS-Bot](https://pro-picinsight-vs-bot-her2wzlhp28qzxmbokesl8.streamlit.app/)

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Streamlit
- `google-generativeai` library
- `Pillow` library
- `python-dotenv` library

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/pushpendra-saini-pks/Pro-PicInsight-VS-Bot.git
    cd smart-c---assistant
    ```

2. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables**:

    Create a `.env` file in the root directory and add your Google API key:

    ```plaintext
    GOOGLE_API_KEY=your_google_api_key
    ```

### Running the Application

Run the Streamlit application:

```bash
streamlit run vision.py
