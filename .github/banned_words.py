import re
from pathlib import Path

PATH = ['{0}/content'.format(Path(__file__).parent.parent),'{0}/api'.format(Path(__file__).parent.parent)]


ignore_characters = ['http',
                'zoomable',
                '.multisafepay',
                'multisafepay.',
                '##',
                '-',
                '"',
                '**',
                '`',
                "'"]

with open('.github/banned_words.txt', 'r') as f:
    banned_words = f.read().split('\n')


def main():
    status = False
    for path in PATH:
      for filename in walk(path):
          words_list = open_file(filename)
          for word in words_list:
              if not word:
                  continue
              if any(char in word for char in ignore_characters):
                  continue
              word = re.sub('[^a-zA-Z0-9 \n\.]', '', word)
              for banned_word in banned_words:
                  match = re.search(r'\b{0}\b'.format(str(banned_word)), word)
                  if match is not None:
                      status = True
                      print('In file {0} the following banned word is used : {1}'.format(filename, match.group()))
    return status


ignore_files = []


def walk(start):
    paths = []
    for filename in Path(start).glob('**/*.md'):
        if any(path in str(filename) for path in ignore_files):
            continue
        paths.append(filename)
    return paths

def content_without_frontmatter(lines):
    look_up='---'
    look_up_list=[]

    for (num, line) in enumerate(lines,1):
        if look_up in line:
            look_up_list.append(num)

            if len(look_up_list) == 2:
                break

    if len(look_up_list) == 2:
        lines = lines[look_up_list[1]:]

    return lines

def open_file(file):
    with open(file, 'r') as file_content:
        return list(filter(None, content_without_frontmatter(file_content.read().splitlines())))


if __name__ == "__main__":
    if main():
        raise ValueError