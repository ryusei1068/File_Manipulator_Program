import sys


def read_content(inputpath):
    with open(inputpath) as f:
        return f.read()


def write_content(ouputpath, content, option):
    with open(ouputpath, option) as f:
        f.write(content)


def reverse_content(*args):
    verify_arguments(2, *args)
    args = args[0]

    inputpath = args[0]
    outputpath = args[1]

    if not verify_file_extend(inputpath, len(inputpath) - 4, '.txt') or not verify_file_extend(outputpath, len(outputpath) - 4, '.txt'):
        sys.stdout.buffer.write(b'you can use file extend that .txt')
        sys.exit(1)

    content = read_content(inputpath)
    write_content(outputpath, content[::-1], 'w')


def copy_content(*args):
    verify_arguments(2, *args)
    args = args[0]

    inputpath = args[0]
    outputpath = args[1]

    if not verify_file_extend(inputpath, len(inputpath) - 4, '.txt') or not verify_file_extend(outputpath, len(outputpath) - 4, '.txt'):
        sys.stdout.buffer.write(b'you can use file extend that .txt')
        sys.exit(1)

    content = read_content(inputpath)
    write_content(outputpath, content, 'w')


def duplicate_contens(*args):
    verify_arguments(2, *args)
    args = args[0]

    inputpath = args[0]
    if not verify_file_extend(inputpath, len(inputpath) - 4, '.txt'):
        sys.stdout.buffer.write(b'you can use file extend that .txt')
        sys.exit()

    n = args[1]
    if not n.isdigit():
        sys.stdout.buffer.write(b'input digit')
        sys.exit()

    content = read_content(inputpath)
    for _ in range(0, int(n)):
        write_content(inputpath, content, 'a')


def replace_string(*args):
    verify_arguments(3, *args)
    args = args[0]

    inputpath = args[0]
    if not verify_file_extend(inputpath, len(inputpath) - 4, '.txt'):
        sys.stdout.buffer.write(b'you can use file extend that .txt')
        sys.exit(1)

    needle = args[1]
    newstring = args[2]

    content = read_content(args[0])
    write_content(inputpath,  content.replace(needle, newstring), 'w')


def verify_arguments(n, *args):
    if n != len(*args):
        sys.stdout.buffer.write(b'valid number of arguments')
        sys.exit(1)


def verify_file_extend(path, start, extend):
    return path.find(extend, start) != -1


def main():
    args = sys.argv[1:]

    if len(args) <= 1:
        sys.stdout.buffer.write(b'valid your input\nex: python3 file_manipulator.py reverse test.txt output.txt')
        sys.exit(1)

    hash_map = {}
    hash_map['reverse'] = reverse_content
    hash_map['copy'] = copy_content
    hash_map['duplicate-contents'] = duplicate_contens
    hash_map['replace-string'] = replace_string

    if args[0] in hash_map.keys():
        hash_map[args[0]](args[1:])
    else:
        print("not found, ", args[0])

if __name__ == "__main__":
    main()
