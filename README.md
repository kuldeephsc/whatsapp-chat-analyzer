# WhatsApp Chat Analyzer

A tool to analyze WhatsApp chat data and generate useful insights such as message statistics, word clouds, most common words, and emoji analysis. Built with **Streamlit** for the user interface and **Flask** for the backend.

## Features

- **Message Statistics**: Total messages, words, media messages, and media links.
- **Busiest Users**: Find the most active users in a WhatsApp group.
- **Word Cloud**: Generate a word cloud of frequently used words.
- **Most Common Words**: Display the most common words used, excluding stopwords.
- **Emoji Analysis**: Visualize emoji usage with a pie chart.


## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/whatsapp-chat-analyzer.git
cd whatsapp-chat-analyzer
pip install -r requirements.txt
streamlit run main.py


whatsapp-chat-analyzer/
│
├── main.py             # Main Streamlit app
├── helper.py           # Helper functions for data analysis
├── preprocessor.py     # Preprocessing WhatsApp chat data
└── requirements.txt    # List of dependencies
