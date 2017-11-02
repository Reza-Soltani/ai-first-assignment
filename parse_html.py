def find_class_id_attribute(page):

    try:
        classes = [value
                   for element in page.find_all(class_=True)
                   for value in element["class"]]
    except:
        classes = []

    try:
        ids = [value for element in page.find_all(class_=True) for value in element["id"]]
    except:
        ids = []

    return classes, ids
