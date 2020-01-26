"""task 1 / time 14:20.7"""


def manager_distribute(user_ids, contacts):
    counter = 0
    for contact in contacts:
        if counter == len(user_ids):  # 5
            counter = 0
        contact['manager_id'] = user_ids[counter]
        counter += 1
    return contacts


if __name__ == "__main__":
    user_ids = [11, 12, 13, 14, 15]  # task data
    contacts = [
        {'name': 'John Doe', 'id': 1, 'manager_id': ''},
        {'name': 'Vasiya Pupkin', 'id': 2, 'manager_id': ''},
        {'name': 'John Pupkin', 'id': 3, 'manager_id': ''},
        {'name': 'Vasya Doe', 'id': 4, 'manager_id': ''},
        {'name': 'John Smith', 'id': 5, 'manager_id': ''},
        {'name': 'Homer Simpson', 'id': 6, 'manager_id': ''},
        {'name': 'Winnie the Pooh', 'id': 7, 'manager_id': ''},
        {'name': 'Bender Rodriguez', 'id': 8, 'manager_id': ''},
        {'name': 'Philip J. Fry', 'id': 9, 'manager_id': ''},
        {'name': 'Fox Mulder', 'id': 10, 'manager_id': ''},
        {'name': 'Parry Mason', 'id': 11, 'manager_id': ''}
    ]  # task data
    new_contacts = manager_distribute(user_ids, contacts)
    print(new_contacts)