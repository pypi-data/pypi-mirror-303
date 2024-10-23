# INIT
'''
>>> pyauto init .pyautorun.test

        PyAuto Run

Config file created @ E:\github\pyautorun\test 
Use: pyauto run
To run the script

Happy Coding!
'''

# Add
'''
>>> pyauto add -h tests -s "test = tested sucessfully" -c .pyautorun.test 

        PyAuto Run

Config file: .pyautorun.test
Added command: tests.test = tested sucessfully
New header and script added @ .pyautorun.test 

Use: pyauto run
To run the script

Happy Coding!
'''

# FIND
'''
>>> pyauto find -l test -h tests -c .pyautorun.test

        PyAuto Run

Found 'test = tested sucessfully' @ line 4 in tests

Happy Coding!
'''

# RUN
'''
>>> pyauto run tests -c .pyautorun.test

        PyAuto Run

Config file: .pyautorun.test
Header Name: tests

Header found @ line 3: [py.tests]
Number of commands executing: 1

Commands:
tested sucessfully

Executing Commands...
Executing: tested sucessfully

'tested' is not recognized as an internal or external command,
operable program or batch file.

Happy Coding!
'''