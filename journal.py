import os


def load():
    data = []

    if os.path.exists(get_pathname()):
        with open(get_pathname()) as file:
            for entry in file.readlines():
                data.append(entry.rstrip())

    return data


def save(journal_data):
    print('... Saving in {}'.format(get_pathname()))

    with open(get_pathname(), 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')

def get_pathname():
    return os.path.abspath(os.path.join('.' , 'journals', 'TODO' + '.txt'))

def journal_entry():
    pass