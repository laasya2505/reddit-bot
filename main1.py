import praw
import requests
import schedule
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Reddit API setup
reddit = praw.Reddit(
    client_id="Tt6cNK6WK3k1S3iTLKeuDA",
    client_secret="RmoyG-Xtgw6scry_r7PmQtfD_5Uv9A",
    username='Icy-Veterinarian3706',
    password='Laasya@2004',
    user_agent='Bot/1.0 by Icy-Veterinarian3706'
)

# Groq API setup
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"  
GROQ_API_KEY = "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"

# Content generator using Groq API
def generate_content_from_groq(prompt):
    headers = {
        "Authorization": f"Bearer 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",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.3-70b-versatile",  
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 150
    }

    try:
        response = requests.post(GROQ_API_URL, json=data, headers=headers)
        if response.status_code != 200:
            logging.error(f"Failed to communicate with Groq API: {response.status_code}, {response.text}")
            return None

        response_data = response.json()
        if not response_data or "choices" not in response_data:
            logging.error("Invalid or empty response received from Groq API")
            return None

        return response_data["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        logging.error(f"Error communicating with Groq API: {str(e)}")
        return None

# Post to Reddit function
def post_to_reddit(subreddit, title, content):
    try:
        reddit.subreddit(subreddit).submit(title, selftext=content)
        logging.info(f"Successfully posted to r/{subreddit}: {title}")
    except praw.exceptions.APIException as e:
        logging.error(f"Reddit API exception: {e}")
    except praw.exceptions.ClientException as e:
        logging.error(f"Reddit client exception: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

# Comment on Reddit posts
def comment_on_posts(subreddit, prompt):
    try:
        for post in reddit.subreddit(subreddit).hot(limit=5):  # Fetch top 5 hot posts
            comment_text = generate_content_from_groq(prompt)
            if comment_text:
                post.reply(comment_text)
                logging.info(f"Successfully commented on post: {post.title}")
            else:
                logging.error("Failed to generate comment. Skipping this post.")
    except praw.exceptions.APIException as e:
        logging.error(f"Reddit API exception: {e}")
    except praw.exceptions.ClientException as e:
        logging.error(f"Reddit client exception: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

# Daily task to post and comment
def daily_task():
    post_prompt = "about software development"
    post_content = generate_content_from_groq(post_prompt)

    if post_content:
        post_to_reddit("test", "Daily AI Post", post_content)

    comment_prompt = "Write a simple comment about the new technologies."
    comment_on_posts("test", comment_prompt)

# Schedule the task
schedule.every(10).seconds.do(daily_task)

# Keep the script running
logging.info("Reddit bot started. Waiting to post and comment at scheduled times.")
try:
    while True:
        schedule.run_pending()
        time.sleep(1)  # Avoid excessive CPU usage
except KeyboardInterrupt:
    logging.info("Bot stopped manually.")
