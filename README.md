# Debugging in vscode:
-----------------------------
created a file sample.py to see debugging


* in your .py file, set breakpoints by clicking in the gutter to the left of the line numbers
* open the debug view by clicking on the bug icon in the left sidebar or pressing `Ctrl+Shift+D`
* options appear at the top of the debug view, click on the green play button to start debugging
* on the left side you will be able to view the variables and their values change as we step through the code
* use the toolbar at the top of the debug view to step through the code, continue running, or stop debugging
* in the left sidebar, you can add items to the watch list to keep an eye on specific variables or expressions
* you can also view the call stack to see the sequence of function calls leading to the current breakpoint
* to inspect the value of a variable, hover over it in the editor or add it to the watch list

# exception handling:

in the demo.py file;

* normal code with errors

* use try-except blocks to handle exceptions gracefully

* in the try block, write the code that may raise an exception

* in the except block, specify the type of exception you want to catch and write the code to handle it

* you can have multiple except blocks to handle different types of exceptions

* you can also use a generic except block to catch any exception, but it's generally better to catch specific exceptions

* creating custom exceptions by defining a new class that inherits from the built-in Exception class