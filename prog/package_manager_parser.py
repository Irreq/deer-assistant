from src import config
from src.display import generate
import re, subprocess

reset = config.placeholders["<RESET>"]
blue = config.placeholders["<BLUE>"]
yellow = config.placeholders["<YELLOW>"]
red = config.placeholders["<RED>"]
green = config.placeholders["<GREEN>"]
cyan = config.placeholders["<CYAN>"]
magenta = config.placeholders["<MAGENTA>"]





def first_word_in_string(string):
    # match any 'word': ([^\s]+)
    partially = [k for k in re.finditer("([^\s]+)", string, re.MULTILINE)][0]
    return partially.group(), partially.span()


def search(query):

    #print(f"{red}WARNING{reset} This function is under construction and is being really buggy")

    static = {}

    text = ""
    first = 0
    last = 0


    # manager = config.system[0]

    manager, methods = config.system[1]["package_manager"]

    # manager = "scratch"
    # methods = {"search": "scratch search $"}

    output = subprocess.getoutput(methods["search"].replace("$", query))

    # Pacman
    if manager == "pacman":
        # Hardcoded pacman parser

        """Pacman output from 'pacman -Ss PROGRAM' (in no particular order):
        ========================================================================

        core/bash 5.1.012-1 [installed]
            The GNU Bourne Again shell
        core/coreutils 9.0-2 [installed]
            The basic file, shell and text manipulation utilities of the GNU...
        extra/easy-rsa 3.0.8-2
            Simple shell based CA utility
        community/b4 0.8.0-2
            Helper utility to work with patches made available via a public...

        ========================================================================
        """

        categories = []
        # Filter the search results into three categories
        for pattern in ["core", "extra", "community"]:
            for match in re.finditer(pattern+"/", output, re.MULTILINE):
                categories.append(match.span())

        for i, find in enumerate(categories):

            # MUST FIX THIS ERROR SO THAT PACKAGES WON'T GO MISSING DURING SEARCH
            # AT THE MOMENT IT SKIPS SOME PACKAGES
            if i >= len(categories)-1:
                continue
                print("Error round here")

            next_word = categories[i+1]

            # Match the name of the program
            name, place = first_word_in_string(output[find[1]:next_word[0]])
            current_pos = find[1]+place[1]

            # Match the version of the program (comes directly after the name)
            version, place = first_word_in_string(output[current_pos:next_word[0]])

            current_pos += place[1]

            # Anything else, can be an already installed flag
            _el = output[current_pos:next_word[0]]
            _else_splitted = _el.split("\n")
            try:
                _else, place = first_word_in_string(_else_splitted[0])
            except:
                _else = False

            description = "".join(_else_splitted[1:])
            description = description.split(" ")
            description = [k for k in description if k not in "   "]
            description = " ".join(description)

            now_first, now_last = find

            local_text = output[last:now_first]
            text += local_text

            first = now_first
            last = now_last

            grupp = output[first:last]

            if not grupp in static:
                static[grupp] = []

            static[grupp].append([name, version, _else, description])

            text += blue + grupp + reset

        
        ress = ""

        if categories == []:
            ress += "No packages found for: " + query

        for gr in static:
            ress += "\n" + magenta + gr + reset + "\n"
            for program in static[gr]:
                is_installed = ("[installed]" == program[2])
                ress += f"[{' '*(is_installed == False)+f'{green}*{reset}'*is_installed}] {blue}{program[0]} {cyan}{program[1]}{reset} - {program[3]}\n"

        return ress.split("\n")


    elif manager == "scratch":
        # return f"{red}WARNING{reset} This function is under construction and is being prematurely halted\n".split("\n")
        # Hardcoded scratchpkg parser

        """scratchpkg output from 'scratch search PROGRAM' (in no particular order):
        ========================================================================

        [*] (main) cython3 0.29.24-1: C-Extensions for Python3
        [ ] (main) imath 3.1.3-1: C++ and python library of 2D and 3D vector, ..
        [ ] (main) pypanel 2.4-1: Lightweight panel/taskbar written in Python...
        [ ] (multilib) python3-32 3.9.7-1: Next generation of the python high...
        ========================================================================
        """



        categories = []
        # Filter the search results into three categories
        for pattern in ["\(main\)", "(multilib)", "community"]:
            for match in re.finditer(pattern, output, re.MULTILINE):
                categories.append(match.span())

        # print(categories)

        for i, find in enumerate(categories):

            # MUST FIX THIS ERROR SO THAT PACKAGES WON'T GO MISSING DURING SEARCH
            # AT THE MOMENT IT SKIPS SOME PACKAGES
            if i >= len(categories)-1:
                continue
                print("Error round here")

            # find += (5, 5)

            next_word = categories[i+1]

            # print(output[find[1]+5:next_word[0]]+"\n")

            # Match the name of the program +5 is to account for colors
            name, place = first_word_in_string(output[find[1]+5:next_word[0]])
            current_pos = find[1]+place[1]

            # print(name)
            # continue

            # Match the version of the program (comes directly after the name)
            version, place = first_word_in_string(output[current_pos:next_word[0]])

            current_pos += place[1]

            # Anything else, can be an already installed flag
            _el = output[current_pos:next_word[0]]
            _else_splitted = _el.split("\n")
            try:
                _else, place = first_word_in_string(_else_splitted[0])
            except:
                _else = False

            description = "".join(_else_splitted[1:])
            description = description.split(" ")
            description = [k for k in description if k not in "   "]
            description = " ".join(description)

            now_first, now_last = find

            local_text = output[last:now_first]
            text += local_text

            first = now_first
            last = now_last

            grupp = output[first:last]

            if not grupp in static:
                static[grupp] = []

            static[grupp].append([name, version, _else, description])

            text += blue + grupp + reset

        ress = ""

        for gr in static:
            ress += "\n" + magenta + gr + reset + "\n"
            for program in static[gr]:
                is_installed = ("[installed]" == program[2])
                ress += f"[{' '*(is_installed == False)+f'{green}*{reset}'*is_installed}] {blue}{program[0]} {cyan}{program[1]}{reset} - {program[3]}\n"

        return ress.split("\n")

        # print(output)

        print(categories)

        text = output.split("\n")

        exit()

        return text

    else:
        text = f"""

                                    <YELLOW><UNDERLINE>Notice<RESET>

No package manager was given, please specify which one you wan't to use:


"""

        text += "".join(['                 [<BLUE>{0}<RESET>] - <BLUE>{1}<RESET>\n'.format(i, v) for i, v in enumerate(["pacman", "scratch", "xbps"])])

        text = generate(text.split("\n"))

    return text

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

def main(query):

    return search(query)













if __name__ == "__main__":

    main(2)
