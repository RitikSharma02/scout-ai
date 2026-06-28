# Scout AI

A lightweight research agent that takes a query, searches the web and Wikipedia, and returns a structured response with a summary and sources. Built with Python, LangChain, and Gemini.

## Setup

Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/RitikSharma02/scout-ai.git
cd scout-ai
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file with your Google API key:

```
GOOGLE_API_KEY=your_key_here
```

## Usage

Run the agent:

```bash
python main.py
```

Enter your search query when prompted. The agent will process the request and output the findings along with the sources it used.

## License

MIT
