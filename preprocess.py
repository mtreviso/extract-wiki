import re
import string
import unicodedata

from selectolax.parser import HTMLParser


def lowercase(text):
    return text.lower()


def trim(text):
    return re.sub(r'[\r\t\ ]+', ' ', text).strip()


def remove_newlines(text):
    return re.sub(r'\n', ' ', text)


def remove_double_newlines(text):
    return re.sub(r'\n\n', ' ', text)


def remove_accents(text):
    return ''.join([c for c in unicodedata.normalize('NFKD', text) if not unicodedata.combining(c)])


def remove_tags(text):
    return HTMLParser(text).body.text(separator='\n')


def remove_punctuation(text, less='.;!?\"'):
    p = ''.join([c if c not in less else '' for c in string.punctuation])
    return text.translate(text.maketrans('', '', p))


def transform_punctuation_to_dot(text):
    t = re.sub(r'(\.+)|(\!+)|(\?+)|(\;+)|(\" )', '.', text)
    t = re.sub(r'\"+', '', t)
    return re.sub(r'\.+', ' . ', t)


def transform_numbers(text):
    return re.sub(r'\d', '0', text)


def transform_decimals(text):
    return re.sub(r'\d+[\.\,]\d+', 'DECIMAL', text)


def transform_urls(text):
    return re.sub(r'(http|https)://[^\s]+', 'URL', text)


def transform_emails(text):
    return re.sub(r'[^\s]+@[^\s]+', 'EMAIL', text)


def transform_dollar(text):
    return re.sub(r'\d+[\.\,]?[0.9]*\ ?[a-zA-Z]*[\$\£\€]', 'DOLLAR', text)


def transform_hours(text):
    text = re.sub(r'(\d+([hms]\d*)+|\d+([\:\-]\d*)[hms])+', 'HOUR', text)
    return re.sub(r'HOUR([\:\-]?HOUR)*', 'HOUR', text)


def transform_dates(text):
    return re.sub(r'\d+[\/\-\:]\d+([\/\-\:]\d+)?', 'DATE', text)


def fix_quotes(word):
    """from: https://github.com/erickrf/nlpnet/blob/master/nlpnet/utils.py"""
    word = re.sub(r"(?u)(^|\W)[‘’′`']", r'\1"', word)
    word = re.sub(r"(?u)[‘’`′'](\W|$)", r'"\1', word)
    word = re.sub(r'(?u)[‘’`′“”]', '"', word)
    return word


def fix_mistyped_tokens(word):
    """from: https://github.com/erickrf/nlpnet/blob/master/nlpnet/utils.py"""
    # tries to fix mistyped tokens (common in Wikipedia-pt) as ,, '' ..
    word = re.sub(r'(?<!\.)\.\.(?!\.)', '.', word)  # take care with ellipses
    word = re.sub(r'([,";:])\1,', r'\1', word)
    # inserts space after leading hyphen. It happens sometimes in cases like:
    # blablabla -that is, bloblobloblo
    word = re.sub(r' -(?=[^\W\d_])', ' - ', word)
    # replaces special ellipsis character
    word = word.replace(u'…', '...')
    return word
