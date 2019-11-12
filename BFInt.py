prog = ['+', '>', '+', '+', '<', '+', '+', '$']
progHead = 0
tape = [0, 0]
head = 0
head = int(head)
while True:
    if prog[progHead] == '+':
        tape[head] = tape[head] + 1
        progHead = progHead + 1
    if prog[progHead] == '-':
        tape[head] = tape[head] - 1
        prog[progHead] = prog[progHead] - 1
    if prog[progHead] == '>':
        head = head + 1
        progHead = progHead + 1
    if prog[progHead] == '<':
        head = head - 1
        progHead = progHead + 1
    if prog[progHead] == '$':
        break
for x in range(len(tape)):
    print(tape[x])