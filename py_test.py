print("hello python")
def get_formatted_name(first_name,last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("first_name: ")
    if f_name == 'q' :
        break

    l_name = input("last_name: ")
    if l_name == 'q' :
        break

    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHello," + formatted_name + "!")

    print("\nend!")


