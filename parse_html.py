def find_class_id_attribute(page):
    classes = [value
               for element in page.find_all(class_=True)
               for value in element["class"]]

    ids = [value
           for element in page.find_all(class_=True)
           if element.has_attr('id')
           for value in element["id"]]
    tags = [tag.name for tag in page.findChildren()]

    classes = list(set(classes))
    ids = list(set(ids))
    tags = list(set(tags))

    return classes, ids, tags
