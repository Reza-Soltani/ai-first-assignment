<<<<<<< Updated upstream:utils.py
def read_script():
    input_file = open('isna_topic.test', 'r')
=======
def read_test():
    input_file = open('/Users/reza/PycharmProjects/css-selector/isna_topic.test', mode='r')
>>>>>>> Stashed changes:reader.py
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
