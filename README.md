# Reddit Bot with Groq AI Integration

## Overview
This project is a simple Reddit bot that automatically generates and posts content daily using Groq AI's text generation capabilities. Additionally, the bot can comment on other Reddit posts to enhance engagement. It integrates the Reddit API for authentication and posting, as well as the Groq API for generating AI-based content.

## Features
- **Daily Automated Posting:** Posts AI-generated content to a specified subreddit at user-scheduled times.
- **Groq AI Integration:** Uses Groq AI to generate engaging and relevant content.
- **Comment Generation:** Generates and posts comments on other Reddit posts.
- **Error Handling:** Includes logging for error tracking and debugging.
- **Scheduling:** Utilizes a lightweight scheduling library for timed operations.

## Prerequisites
- Python 3.7+
- Reddit API credentials (Client ID, Client Secret, Username, Password, User Agent)
- Groq API key

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install Required Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   Create a `.env` file in the project directory and populate it with the following:
   ```env
   REDDIT_CLIENT_ID=<your_client_id>
   REDDIT_CLIENT_SECRET=<your_client_secret>
   REDDIT_USERNAME=<your_reddit_username>
   REDDIT_PASSWORD=<your_reddit_password>
   REDDIT_USER_AGENT=<your_user_agent>
   GROQ_API_KEY=<your_groq_api_key>
   ```

4. **Run the Bot:**
   ```bash
   python main.py
   ```

## Project Structure
```
.
├── main.py                 # Main script for the Reddit bot
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .env                    # Environment variables (not included in the repository)
```

## How It Works

### Daily Posting
1. The bot generates content using Groq AI's text generation API.
2. Posts the generated content to the specified subreddit.
3. Logs each successful post or any errors encountered.

### Comment Generation
1. The bot retrieves the latest posts from a specified subreddit.
2. Generates comments for the posts using Groq AI.
3. Posts the comments and logs the activity.

## Configuration
- **Subreddit:** Update the `SUBREDDIT_NAME` in `main.py` to specify your target subreddit.
- **Posting Schedule:** Modify the schedule in `main.py` to adjust the posting frequency and timing.

## Error Handling
- **Groq API Errors:** Logs detailed error messages if the API call fails.
- **Reddit API Errors:** Handles Reddit API exceptions gracefully to prevent crashes.

## Example Usage
1. Start the bot.
2. Observe log messages in the console for scheduled posting and commenting activity.
3. Check your target subreddit for new posts and comments from the bot.

## Limitations
- The bot may hit API rate limits if run excessively.
- Ensure compliance with Reddit’s [Bot Policy](https://www.redditinc.com/policies/data-api-terms-of-service).

## Future Enhancements
- Add support for replying to comments.
- Improve content relevance using advanced prompts.
- Include sentiment analysis for better engagement.

## License
This project is licensed under the MIT License. See `LICENSE` for details.

## Acknowledgments
- [PRAW](https://praw.readthedocs.io/) for seamless Reddit API integration.
- [Groq AI](https://www.groq.com/) for powerful AI text generation.

