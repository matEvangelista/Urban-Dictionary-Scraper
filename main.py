from bs4 import BeautifulSoup
import requests


def define(word):
    """Function that returns a list of definitions and examples from urban dictionary"""

    examples = []
    definitions = []
    if more_than_one_page(word):
        # this string is absolutely necessary, since 'word&page=n' may change to 'WORD&page=n' or 'Word&page=n'
        string = returns_soup(word).find('div', class_="def-header").text
        for i in range(1, number_of_pages(word) + 1):
            if i == 1:
                soup = returns_soup(word)
                definitions += soup.find_all('div', class_='meaning')
                examples += replace_br(soup.find_all('div', class_='example'))
            else:
                soup = returns_soup(string + f'&page={i}')
                definitions += soup.find_all('div', class_='meaning')
                examples += replace_br(soup.find_all('div', class_='example'))
    else:
        soup = returns_soup(word)
        definitions += soup.find_all('div', class_='meaning')  # list of every definition found on the page
        examples += replace_br(soup.find_all('div', class_='example'))  # list of every example on the page

    # definitions and examples have the same length, it doesn't matter which one is picked
    result = [{'def': definitions[i].text, 'ex': examples[i].text} for i in range(len(definitions))]
    return result


def returns_soup(word):
    """Function that returns a Beautiful Soup of the page of a term"""

    word = word.strip()
    url = f'https://urbandictionary.com/define.php?term={word}'
    html_content = requests.get(url).content
    return BeautifulSoup(html_content, 'html.parser')


def replace_br(examples):
    """Function that replaces <br> with \n"""

    for example in examples:
        for br in example.find_all('br'):
            br.replace_with('\n')  # users often submit dialogs to their examples. Most of them have more than one line
            # By replacing <br> with \n, we assure that the program will return the examples as they're shown on the
            # website
    return examples


def more_than_one_page(word):
    """Function that returns the number of pages a word has"""
    soup = returns_soup(word)
    soup_buttons = soup.find_all('a')
    for button in soup_buttons:
        if "Last" in str(button):
            return True
    return False


def number_of_pages(word):
    """Funtion that returns the number of pages a term has"""
    soup = returns_soup(word)
    soup_buttons = soup.find_all('a')
    index = 0
    for i, button in enumerate(soup_buttons):
        if 'Last' in str(button):
            index = i
    button = str(soup_buttons[index])
    return int(button[(button.rfind('=') + 1):button.rfind('"')])

print(define('brazil'))
