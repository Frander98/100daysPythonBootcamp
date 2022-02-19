def make_bold(a_function):
    def wrapper():
        a_function()
        return f"<b>{a_function()}</b>"

    return wrapper


def make_emphasis(a_function):
    def wrapper():
        a_function()
        return f"<em>{a_function()}</em>"

    return wrapper


def make_underlined(a_function):
    def wrapper():
        a_function()
        return f"<u>{a_function()}</u>"

    return wrapper
