import journal


def main():
    journal_header()
    run_event_loop()


def journal_header():
    print('----------------------')
    print('     Journal App')
    print('----------------------')


def run_event_loop():
    x = None
    journal_list = journal.load()

    while x != 'e':
        x = input('[l]List journal [a]Add to journal [e]exit\n').lower().strip()

        if x == 'a':
            add_to_journal(journal_list)

        elif x == 'l':
            show_jornal(journal_list)

        elif x == 'e':
            print('Exit journal')

        else:
            print('Invalid Entry')

    journal.save(journal_list)

def add_to_journal(data):
    user_input = input('Add a note to your journal\n')
    data.append(user_input)


def show_jornal(data):
    for note in data:
        print(note)


main()
