from src import config
import re

reset = config.placeholders["<RESET>"]
blue = config.placeholders["<BLUE>"]
yellow = config.placeholders["<YELLOW>"]
red = config.placeholders["<RED>"]
green = config.placeholders["<GREEN>"]
cyan = config.placeholders["<CYAN>"]
magenta = config.placeholders["<MAGENTA>"]


static = {}


def first_word_in_string(string):
    # match any 'word': ([^\s]+)
    partially = [k for k in re.finditer("([^\s]+)", string, re.MULTILINE)][0]
    return partially.group(), partially.span()


def search():
    pass

def sync():
    pass

def install():
    pass

def upgrade():
    pass

def remove():
    pass

def info():
    pass

def main(query, manager="pacman"):

    text = ""
    first = 0
    last = 0



    patterns = ["core", "extra", "community"]

    # from re import finditer

    print(232434234234)

    finds = []
    for pattern in patterns:
        # text = query[first:last]
        for match in re.finditer(pattern+"/", query, re.MULTILINE):
            finds.append(match.span())

        # de = re.findall(pattern, query, re.MULTILINE)
        # print(de)


    for i, find in enumerate(finds):
        if i >= len(finds)-1:
            continue
            print("Error round here")

        next_one = finds[i+1]


        # first_it = re.finditer("([^\s]+)", query[find[1]:next_one[0]], re.MULTILINE)
        # name = [k for k in first_it][0].group()

        name, place = first_word_in_string(query[find[1]:next_one[0]])
        # print(name)
        #
        # stuff =
        #
        # print(stuff)
        #
        # exit()
        current_pos = find[1]+place[1]
        version, place = first_word_in_string(query[current_pos:next_one[0]])
        # version =
        # print(version)
        current_pos += place[1]

        # anything else
        _el = query[current_pos:next_one[0]]
        _else_splitted = _el.split("\n")
        try:
            _else, place = first_word_in_string(_else_splitted[0])
        except:
            _else = False

        description = "".join(_else_splitted[1:])
        description = description.split(" ")
        description = [k for k in description if k not in "   "]
        description = " ".join(description)
        # print(_else)
        # text += query[first:last]
        now_first, now_last = find

        local_text = query[last:now_first]
        text += local_text

        # print(last, now_first)

        first = now_first
        last = now_last

        grupp = query[first:last]

        if not grupp in static:
            static[grupp] = []

        static[grupp].append([name, version, _else, description])

        text += blue + grupp + reset
        # print(text)

        # print(grupp, name, version, _else, description)

    # print(static)

    ress = ""

    for gr in static:
        ress += "\n" + magenta + gr + reset + "\n"
        for program in static[gr]:
            # print(program)

            is_installed = ("[installed]" == program[2])
            # print()
            ress += f"[{' '*(is_installed == False)+f'{green}*{reset}'*is_installed}] {blue}{program[0]} {cyan}{program[1]}{reset} - {program[3]}\n"


    return ress.split("\n")



    result = "{0}Hello World{1}".format(blue, reset)
    return [result, result]


if __name__ == "__main__":

    main(2)
