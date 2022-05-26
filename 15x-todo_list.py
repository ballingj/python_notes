# ####################################
#  Todo list to exercise use of lists and list method
#
#########################################

# Print header
print("""
  _____         _           
 |_   _|__   __| | ___  ___ 
   | |/ _ \ / _` |/ _ \/ __|
   | | (_) | (_| | (_) \__ \\
   |_|\___/ \__,_|\___/|___/

""")

# initialize todo and completed list
todos = []
todo_num = []
completed_list = []

# prompt
print("*"*40)
response = input("Enter a command.  Type 'h' for help:\n> ")

while response != 'q':
    # handle a response when 'h' | when 'q' | when an integer | or else add to todo list
    # handle 'h' 
    if response == 'h':
        print("""
        TODO LIST HELP
        Type 'q' to quit
        To add a todo to the list, type it and hit enter
        To complete a todo enter its number
        """)
    # handle q entry
    elif response == 'q':
        break
    # handle when an integer
    elif response.isnumeric():
        idx = int(response) -1
        # remove list and add to complete
        if idx >= len(todos):
            print("There is no Todo with that number!")
        else:
            item = todos[idx]
            todos.pop(idx)
            completed_list.append(item)
            for i, value in enumerate(todos, start=1):
                print(f"{i}) {value}")
    # add to todo list
    else:
        if response:
            todos.append(response)
            for i, value in enumerate(todos, start=1):
                print(f"{i}) {value}")
    print("*"*40)
    response = input("Enter a command.  Type 'h' for help:\n> ")
# handle q entry
if response == 'q':
    # print completed list
    print(f"Today you completed {len(completed_list)} todos:")
    for i in completed_list:
        print(f"* {i}")







