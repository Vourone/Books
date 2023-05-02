# Compose a program that writes the Hello, World message 10 times.

import stdio

# Write 'Hello World' to standard input.
i=0
while i<10:
    stdio.writeln('%i. Hello, World' % (i+1))
    i += 1