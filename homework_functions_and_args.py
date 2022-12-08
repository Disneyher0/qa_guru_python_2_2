def open_browser(browser_name):
    func_and_arg_names(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    func_and_arg_names(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    func_and_arg_names(find_registration_button_on_login_page, page_url, button_text)


def func_and_arg_names(function, *args):

    func_name = function.__name__.title().replace("_", " ")

    arg_name = ""
    temp_list = []
    for argument in args:
        if argument.startswith("http"):
            interim_arg_name = argument
            temp_list.append(interim_arg_name)
        else:
            interim_arg_name = argument.title().replace("_", " ")
            temp_list.append(interim_arg_name)
    arg_name += ", ".join(temp_list)

    print(f"function: {func_name} | argument(s): {arg_name}")


open_browser("Edge")
go_to_companyname_homepage("https://www.yandex.ru/")
find_registration_button_on_login_page("https://www.yandex.ru/", "search")