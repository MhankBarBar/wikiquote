from .. import utils

WORD_BLACKLIST = ['dikutip', 'Varian:', 'Diambil', 'Catatan:', 'artikel:']
MAIN_PAGE = 'Halaman Utama'
HEADINGS = ['pemeran', 'lihat juga', 'tautan eksternal', 'tentang']


def extract_quotes(tree, max_quotes):
    q_list = utils.extract_quotes_li(tree, max_quotes, HEADINGS, WORD_BLACKLIST)
    return [utils.remove_credit(q) for q in q_list]

def qotd(html_tree):
    raw_quote = html_tree.xpath('//p')[0].text_content().split('–')
    quote = raw_quote[0].strip()
    author = raw_quote[1].split('.,')[0]
    return quote, author
