journal_list = []


def main():
    journal_header()
    run_event_loop()


def journal_header():
    print('----------------------')
    print('     Journal App')
    print('----------------------')


def run_event_loop():
    x = None

    while x != 'e':
        x = input('[l]List journal [a]Add to journal [e]exit\n').lower().strip()

        if x == 'a':
            add_to_journal()

        elif x == 'l':
            show_jornal()

        elif x == 'e':
            print('Exit journal')

        else:
            print('Invalid Entry')


def add_to_journal():
    user_input = input('Add a note to your journal\n')
    journal_list.append(user_input)


def show_jornal():
    for note in journal_list:
        print(note)


main()
