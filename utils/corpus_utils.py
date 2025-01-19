import nltk
import logging
from logging import Logger
from utils.logging_utils import get_dummy_logger

def check_corpus_downloaded(
        corpus_id: str, 
        logger: Logger = get_dummy_logger(),
        ) -> bool:
    try:
        nltk.data.find(f"corpora/{corpus_id}")
        logger.info(f"{corpus_id} is downloaded.")
        return True
    except LookupError:
        logger.info(f"{corpus_id} not found!")
        return False

if __name__ == "__main__":
    check_corpus_downloaded("movie_reviews")