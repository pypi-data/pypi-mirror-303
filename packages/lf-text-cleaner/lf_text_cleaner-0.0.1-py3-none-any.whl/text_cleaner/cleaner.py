import re


def no_this_words(text, remove_list):
    for word in remove_list:
        text = text.replace(word, "").lower()
    return text.strip()


def remove_numbers(text):
    return re.sub(r"\b\d+\b", " ", text)


def remove_double_whitespace(text):
    return re.sub(r'\s+', ' ', text).strip()


def remove_special_characters(text):
    return re.sub(r'[!@#$%^&]', '', text)


def no_links(text):
    url_pattern = r'(https?:\/\/\S+|www\.\S+|t\.me\S*)'
    return re.sub(url_pattern, '', text, flags=re.MULTILINE | re.IGNORECASE).strip()


def remove_hashtags(text):
    return re.sub(r"#\S*", "", text)


def remove_hashtags_with_text(text):
    return re.sub(r'#\w+', '', text).strip()


def remove_mentions(text):
    return re.sub(r"@\S*", "", text)


def remove_emojis(text):
    emoj1 = re.compile(
        r'[\u274B\uFD3E\u00A9\u00AE\u203C\u2049\u2122\u2139\u2194-\u2199\u21A9\u21AA\u231A\u231B\u2328\u23CF'
        r'\u23E9-\u23F3\u23F8-\u23FA\u24C2\u25AA-\u25AB\u25B6\u25C0\u25FB-\u25FE\u2600-\u2604\u260E\u2611'
        r'\u2614\u2615\u2618\u261D\u2620\u2622\u2623\u2626\u262A\u262E\u262F\u2638\u2639\u263A\u2640'
        r'\u2642\u2648-\u2653\u265F\u2660\u2663\u2665\u2666\u2668\u267B\u267E\u267F\u2692-\u269C\u26A0'
        r'-\u26FD\u2702-\u27BF\u2934\u2935\u2B05-\u2B07\u2B1B\u2B1C\u2B50\u2B55\u3030\u303D\u3297\u3299]')
    emoj2 = re.compile(r'[#\*0-9]️⃣')
    emoj3 = re.compile(r'[\U0001F000-\U0001FADF]')

    text = re.sub(emoj1, '', text)
    text = re.sub(emoj2, '', text)
    text = re.sub(emoj3, '', text)
    return text


def clean(text, options):
    text = text.lower()
    clean_actions = {
        'no_digits': remove_numbers,
        'no_emoji': remove_emojis,
        'no_links': no_links,
        'remove_hashtags': remove_hashtags,
        'remove_hashtags_with_text': remove_hashtags_with_text,
        'remove_mentions': remove_mentions,
        'remove_special': remove_special_characters,
        'remove_words': lambda text: no_this_words(text, options[
            'remove_word_list']) if 'remove_word_list' in options else text,
    }
    for option, action in clean_actions.items():
        if options.get(option, False):
            text = action(text)

    text = remove_double_whitespace(text)

    return text
