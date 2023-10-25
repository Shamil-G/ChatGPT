import g4f
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def get_request(req: str):
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": req}],
        stream=True
    )
    return response


def get_request4(req: str):
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": req}],
        # , stream=True
    )
    return response


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print('-----------------------------------------------------------------')
    result = get_request(["Вызывается функция Oracle, которая должна возвращать VARCHAR2(32000),",
                          "однако получаю ошибку ora-06512 и ora-06502 при возврате результата"])
    for message in result:
        print(message, flush=True, end='')
    # result = get_request4(["Вызывается функция Oracle, которая должна возвращать VARCHAR2(32000),",
    #                       "однако получаю ошибку ora-06512 и ora-06502 при возврате результата"])
    print('***-----------------------------------------------------------------')
    for message in result:
        print(message, flush=True, end='')
    print('+++-----------------------------------------------------------------')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
