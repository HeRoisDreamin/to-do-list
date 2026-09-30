# A Simple Command-Line To-Do List app using Python Lists.

- This is a fundamental python project that leverages the in-built Python functions for operations in To-Do List.
- It uses Try-Except blocks for input validation at certain operations.
- Python libraries like "os" and "json" are imported for the implementation of fetching the previous list or saving the current runtime's list elements into "tasks.txt".

## Library Functions used:
  os.path.exists() function: Used for checking if a previous "tasks.txt" file existed or not
  json.load() fucntion: Used for loading the previous entered tasks into the current list in execution.
  json.dump() function: Used for overwriting the list "tasks" into tasks.txt file after "Save & Exit".
