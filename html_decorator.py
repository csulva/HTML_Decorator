def tag(tag):
    def html_decorator(func):
        def wrapper_func(text):
            return f'<{tag}>{func(text)}</{tag}>'
        return wrapper_func
    return html_decorator

@tag('p')
def greet(name):
    return f'Hello {name}'

@tag('div')
def write_code(code):
    return code

@tag('h2')
def write_header(text):
    return text

print(greet('Chris'))
print(write_code('class=funfunfun'))
print(write_header('Here is my header...'))