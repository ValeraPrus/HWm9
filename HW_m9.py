exit_list = ['good bye', 'close', 'exit']

command_list = 'Command list:\n-hello\n-add ...\
          \n-change ...\n-phone ....\n-show all\
          \n-good bye\n-close\n-exit'

phone_dict = {}


def main():
    while True:
        user = input('>>> ').lower()
        user_date = user.split(' ')
        user_date.pop(0)
        if user in exit_list:
            print(exit_func())
            break
        elif 'hello' in user:
            print(hello_func())
        elif 'add ' in user:
            print(add_func(user_date))
        elif 'change ' in user:
            print(change_func(user_date))
        elif 'phone ' in user:
            print(phone_func(user_date))
        elif 'show all' in user:
            print(show_all_func())
        else:
            print('- Wrong command')


def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except IndexError:
            return '- Give me name and phone please'
        except KeyError:
            return '- Name not found'

    return inner


@input_error
def add_func(user_date):
    if not user_date[0] in phone_dict:
        phone_dict[user_date[0]] = user_date[1]
        return f'- New contact "{user_date[0]}" added'
    else:
        return f'- Name "{user_date[0]}" has already created'


@input_error
def change_func(user_date):
    if user_date[0] in phone_dict:
        phone_dict[user_date[0]] = user_date[1]
        return f'- Number of "{user_date[0]}" changed'
    else:
        return f'- Name "{user_date[0]}" not found'


@input_error
def phone_func(user_date):
    return f'- {phone_dict[user_date[0]]}'


def exit_func():
    return '- Good bye!'


def hello_func():
    return '- How can I help you?'


def show_all_func():
    return phone_dict


if __name__ == '__main__':
    print(f'- Hello :)\n\n{command_list}')
    main()


