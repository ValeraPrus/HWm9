exit_list = ['good bye', 'close', 'exit']

command_list = 'Command list:\n-hello\n-add ...\
          \n-change ...\n-phone ....\n-show_all\
          \n-good bye\n-close\n-exit'

phone_dict = {}


def main():
    handlers = {
        'hello': hello_func,
        'add': add_func,
        'change': change_func,
        'phone': phone_func,
        'show_all': show_all_func,
               }

    while True:
        user = input('>>> ').lower()
        user_date = user.split(' ')
        command_handler = user_date.pop(0)
        if user in exit_list:
            print(exit_func())
            break
        elif command_handler in handlers:
            print(handlers[command_handler](user_date))
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
    phone_dict.setdefault(user_date[0], user_date[1])
    return f'- New contact "{user_date[0]}" added'


@input_error
def change_func(user_date):
    del phone_dict[user_date[0]]
    phone_dict[user_date[0]] = user_date[1]
    return f'- Number of "{user_date[0]}" changed'


@input_error
def phone_func(user_date):
    return f'- {phone_dict[user_date[0]]}'


def exit_func():
    return '- Good bye!'


def hello_func(arg):
    return '- How can I help you?'


def show_all_func(arg):
    return phone_dict


if __name__ == '__main__':
    print(f'- Hello :)\n\n{command_list}')
    main()



