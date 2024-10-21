import os

from dotenv import load_dotenv

load_dotenv()

# PROJECT
DEFAULT_PROJECT = os.getenv("MY_DEFAULT_PROJECT")
DEFAULT_PROCESSOR_LOCATION = os.getenv("MY_PROCESSOR_LOCATION")
DEFAULT_ORC_PROCESSOR = os.getenv("MY_ORC_PROCESSOR")

DEFAULT_GITHUB_TOKEN = os.getenv("MY_GITHUB_TOKEN")
