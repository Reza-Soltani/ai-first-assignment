def read_test():
    input_file = open('irib.test', mode='r')
    is_url = 1
    urls = []
    contents = []
    for line in input_file:
        if is_url:
            urls.append(line)
        else:
            contents.append(line)
        is_url = 1 - is_url
    return urls, contents
