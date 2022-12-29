
def shipping_label(*names, **address):
    receiver = ""
    for name in names:
        receiver += name + " "
    print(receiver)

    the_address = ""
    for detail in address.values():
        the_address += str(detail) + ", "

    print(the_address)
    # OR
    if 'floor' in address:
        first_line = f"{address.get('floor')} flr House no. {address.get('house')} {address.get('zone')}"
    else:
        first_line = f"{address.get('house')} {address.get('zone')}"
    second_line = f"{address.get('city')}, {address.get('province')} {address.get('zip')}"
    print(first_line)
    print(second_line)


shipping_label("Genifer", "Abalos", house=1, zone="Zone 7", city="Tuguegarao", province="Cagayan", zip=3500)
shipping_label("Genifer", "Aurelio", "Abalos", floor="Second", house=1, zone="Zone 7", city="Tuguegarao", province="Cagayan", zip=3500)


def shipping():
    print("Hey!")