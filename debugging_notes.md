# Testing Menu.py #

## Testing ``menu.py`` ##


0. First, I fixed the menu, so that it accepted lower case inputs, by adding
*'.upper()'* to the second *'if'* line
1. Load the users database.
   * No Error to fix
2. Add a new user and confirm you get a success message.
   * No Error to fix
3. Try to add the same user ID again and confirm you get an error message.
   * No Error to fix
4. Update the name of an existing user.
   * Changed the name of the function to *'modify_user()'*
   * Added a *'user_collection'* parameter to the *'modify_user()'* call
5. Try to update the name of a non-existing user and confirm you get an error
message.
   * No Error to fix
6. Search for an existing user and return that user's email, name and last
   name.
   * Received *"AttributeError: 'Users' object has no attribute 'name'"*
   * Changed *'if not result.name:'* to *'if not result.user_name:'*
7. Search for a non-existing user and return a message indicating that the user
does not exist.
   * Received *"AttributeError: 'NoneType' object has no attribute
   'user_name'"*
   * Changed *'if not result.user_name:'* to *'if result is None:'* 
8. Delete an existing user.
   * No Error to fix
9. Try to delete a non-existing user and confirm you get an error message.
   * No Error to fix
10. Save the users database.
11. Load the status database.
12. Add a new status and confirm you get a success message.
13. Try to add the same status ID again and confirm you get an error message.
14. Update the text of an existing status ID.
15. Try to update the text of a non-existing status ID and confirm you get an
error message.
16. Search for an existing status ID and return the ID of the user that created
the status and the status text.
17. Search for a non-existing status ID and return a message indicating that
the status ID does not exist.
18. Delete an existing status.
19. Try to delete a non-existing status and confirm you get an error message.
20. Save the status database.
21. Make sure menu options are case-insensitive (i.e., typing "a" or "A" works
in the same way).

# Implement logging capabilities on users.py and user_status.py #

1. You can use the standard Python logger or Loguru.
2. Both ``users.py`` and ``user_status.py`` will share a **single log file**
per session.
3. **Each class method** should have **at least one** log info message. For
example, "New status collection instance created".
4. Within each method, you should have **one log error message** before the
method returns ``False``.
5. You can also add logging to ``main.py`` and ``menu.py``, but it is not a
requirement.
6. Log filename: Each time ``menu.py`` is launched it will create a file called
``log_mm_dd_yyyy.log``, which will reflect the date on which the server is
being  launched. If there is already a file with that name, the log messages
will be appended to the existing log file, and not overwritten.