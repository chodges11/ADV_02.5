"""
main driver for a simple social network project
"""
# pylint: disable = import-error
# pylint: disable = unused-variable
# pylint:disable=unspecified-encoding

import csv
import users as u
import user_status as us


def init_user_collection():
    """
    Creates and returns a new instance of UserCollection
    """
    new_user_collection = u.UserCollection()
    return new_user_collection


def init_status_collection():
    """
    Creates and returns a new instance of UserStatusCollection
    """
    new_status_collection = us.UserStatusCollection()
    return new_status_collection


def load_users(filename, user_collection):
    """
    Opens a CSV file with user data and
    adds it to an existing instance of
    UserCollection

    Requirements:
    - If a user_id already exists, it
    will ignore it and continue to the
    next.
    - Returns False if there are any errors
    (such as empty fields in the source CSV file)
    - Otherwise, it returns True.
    """
    try:
        with open(filename, 'r') as read_obj:
            csv_dict_reader = csv.DictReader(read_obj)
            for row in csv_dict_reader:
                user = u.Users(user_id=row["USER_ID"],
                               email=row["EMAIL"],
                               user_name=row["NAME"],
                               user_last_name=row["LASTNAME"]
                               )
                if user.user_id in user_collection.database:
                    continue
                user_collection.add_user(user.user_id,
                                         user.email,
                                         user.user_name,
                                         user.user_last_name
                                         )
        return True

    except OSError as error:
        print(f"{type(error)}: {error}")
        return False


def save_users(filename, user_collection):
    """
    Saves all users in user_collection into
    a CSV file

    Requirements:
    - If there is an existing file, it will
    overwrite it.
    - Returns False if there are any errors
    (such as an invalid filename).
    - Otherwise, it returns True.
    """

    try:
        with open(filename, 'w', newline='') as csvfile:
            csv_columns = ['USER_ID', 'EMAIL', 'NAME', 'LASTNAME']
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            list_user = list(user_collection.database.values())
            counter = 0
            for element in list_user:
                csvfile.write(list_user[counter].user_id + ",")
                csvfile.write(list_user[counter].email + ",")
                csvfile.write(list_user[counter].user_name + ",")
                csvfile.write(list_user[counter].user_last_name + "\n")
                counter += 1
        return True

    except OSError as error:
        print(f"{type(error)}: {error}")
        return False


def load_status_updates(filename, status_collection):
    """
    Opens a CSV file with status data and adds it to an existing
    instance of UserStatusCollection

    Requirements:
    - If a status_id already exists, it will ignore it and continue to
      the next.
    - Returns False if there are any errors(such as empty fields in the
      source CSV file)
    - Otherwise, it returns True.
    """
    try:
        with open(filename, 'r') as read_obj:
            csv_dict_reader = csv.DictReader(read_obj)
            for row in csv_dict_reader:
                user = us.UserStatus(status_id=row["STATUS_ID"],
                                     user_id=row["USER_ID"],
                                     status_text=row["STATUS_TEXT"],
                                     )
                if user.user_id in status_collection.database:
                    continue
                status_collection.add_status(user.status_id,
                                             user.user_id,
                                             user.status_text,
                                             )
        return True

    except OSError as error:
        print(f"{type(error)}: {error}")
        return False


def save_status_updates(filename, status_collection):
    """
    Saves all statuses in status_collection into a CSV file

    Requirements:
    - If there is an existing file, it will overwrite it.
    - Returns False if there are any errors(such an invalid filename).
    - Otherwise, it returns True.
    """

    try:
        with open(filename, 'w',  newline='') as csvfile:
            csv_columns = ['STATUS_ID', 'USER_ID', 'STATUS_TEXT']
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            list_status = list(status_collection.database.values())
            counter = 0
            for element in list_status:
                csvfile.write(list_status[counter].status_id + ",")
                csvfile.write(list_status[counter].user_id + ",")
                csvfile.write(list_status[counter].status_text + "\n")
                counter += 1
        return True

    except OSError as error:
        print(f"{type(error)}: {error}")
        return False


def add_user(user_id, email, user_name, user_last_name, user_collection):
    """
    Creates a new instance of User and stores it in user_collection
    (which is an instance of UserCollection)

    Requirements:
    - user_id cannot already exist in user_collection.
    - Returns False if there are any errors (for example, if
      user_collection.add_user() returns False).
    - Otherwise, it returns True.
    """
    while user_collection.add_user(user_id,
                                   email,
                                   user_name,
                                   user_last_name
                                   ):
        return True
    return False


def update_user(user_id, email, user_name, user_last_name, user_collection):
    """
    Updates the values of an existing user

    Requirements:
    - Returns False if there are any errors.
    - Otherwise, it returns True.
    """
    while user_collection.update_user(user_id,
                                      email,
                                      user_name,
                                      user_last_name
                                      ):
        return True
    return False


def delete_user(user_id, user_collection):
    """
    Deletes a user from user_collection.

    Requirements:
    - Returns False if there are any errors (such as user_id not found)
    - Otherwise, it returns True.
    """
    while user_collection.delete_user(user_id):
        return True
    return False


def search_user(user_id, user_collection):
    """
    Searches for a user in user_collection(which is an instance of
    UserCollection).

    Requirements:
    - If the user is found, returns the corresponding User instance.
    - Otherwise, it returns None.
    """
    user_search_results = user_collection.search_user(user_id)
    if user_search_results.user_id is not None:
        return user_search_results

    return None


def add_status(status_id, user_id, status_text, status_collection):
    """
    Creates a new instance of UserStatus and stores it in
    status_collection(which is an instance of UserStatusCollection)

    Requirements:
    - status_id cannot already exist in status_collection.
    - Returns False if there are any errors (for example, if
      user_collection.add_status() returns False).
    - Otherwise, it returns True.
    """
    new_user_status = us.UserStatus(status_id,
                                    user_id,
                                    status_text
                                    )
    while status_collection.add_status(new_user_status.status_id,
                                       new_user_status.user_id,
                                       new_user_status.status_text
                                       ):
        return True
    return False


def update_status(status_id, user_id, status_text, status_collection):
    """
    Updates the values of an existing status_id

    Requirements:
    - Returns False if there are any errors.
    - Otherwise, it returns True.
    """
    while status_collection.update_status(status_id,
                                          user_id,
                                          status_text
                                          ):
        return True
    return False


def delete_status(status_id, status_collection):
    """
    Deletes a status_id from user_collection.

    Requirements:
    - Returns False if there are any errors (such as status_id not found)
    - Otherwise, it returns True.
    """
    while status_collection.delete_status(status_id):
        return True
    return False


def search_status(status_id, status_collection):
    """
    Searches for a status in status_collection

    Requirements:
    - If the status is found, returns the corresponding
    UserStatus instance.
    - Otherwise, it returns None.
    """
    status_search_results = status_collection.search_status(status_id)
    if status_search_results.status_id is not None:
        return status_search_results
    return None
