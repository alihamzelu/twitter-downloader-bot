# Twitter (X) Video Downloader Bot

A Telegram bot that allows users to download videos from Twitter (X) quickly and easily.

## Features

- Download videos from Twitter (X)
- Multiple video quality options
- Fast and user-friendly interface
- Automatic file cleanup after download
- Multi-user support
- Built with Python and pyTelegramBotAPI

## How It Works

1. Start the bot
2. Send a Twitter/X post link
3. Choose the desired video quality
4. Receive the downloaded video

## Supported Links

- https://x.com/
- https://twitter.com/

## Technologies Used

- Python
- pyTelegramBotAPI
- yt-dlp

## Installation

Clone the repository:

```bash
git clone <repository_url>
cd twitter-video-downloader-bot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
BOT_TOKEN=your_bot_token
```

Run the bot:

```bash
python main.py
```

## Project Structure

```text
.
├── handlers/
├── keyboards/
├── downloader/
├── utils/
├── main.py
└── requirements.txt
```

## License

This project is licensed under the MIT License.
