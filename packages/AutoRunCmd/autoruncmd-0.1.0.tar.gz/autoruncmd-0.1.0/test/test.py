from autoruncmd import *

# INIT
name = ".pyautorun.test"
createConfig(name)

# ADD SCRIPT
name = ".pyautorun.test"
header = "tests"
script = "test=running test - addtoScript"
addtoScript(name, header, script)

# RUN SCRIPT
name = ".pyautorun.test"
header = "tests"
runScript(header, name)


# FIND SCRIPT
name = ".pyautorun.test"
line = "test"
header = "tests"
findLine(name, line, header)