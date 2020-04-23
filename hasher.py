#!/usr/bin/python
import sys

def main():
    """
        needs a salt and list of files to hash them!'
        !!!! YOU NEED TO REMEMBER YOUR SALT TO RECOVER YOUR FILES !!!!
    """
    if len(sys.argv) < 2:
        print(f"(at least)2 arguments Expected {len(sys.argv)-1} given...")
        return
    inp = input("[>] SALT: ")
    try:
        SALT = int(inp)
    except:
        SALT = inp
    ErrorFlag = False
    if type(SALT) != int:
        ErrorFlag = True
    elif SALT < 0 or SALT > 255:
        ErrorFlag = True
    if ErrorFlag:
        print("SALT must be an integer in range [0-255]")
        return
    prefix = ''
    if sys.argv[1] == '-p' or sys.argv[1] == '-P':
        prefix = sys.argv[2]
        FILES = sys.argv[3:]
    else:
        FILES = sys.argv[1:]
    for candidateFile in FILES:
        try:
            r = open(candidateFile, 'rb')
            f = r.read()
            r.close()
            changed = open(prefix+candidateFile, 'wb')
            l = list(f)
            for i in range(len(l)):
                l[i] = l[i]^SALT
            changed.write(bytes(l))
            changed.close()
        except:
            pass


if __name__ == "__main__":
    main()
