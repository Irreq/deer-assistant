import re

# pattern = r"^(.*?)\/(.*?)\s+(\d+\.\d+\.\d+(?:-\d+)?)(?:\s+\[(?installed)\])?\s+(.*)"
pattern = r"^\s*([^/\s]+)\/([^/\s]+)\s+(\S+)(?:\s+\[([^\]]+)\])?\s+(.*)"
pattern = r"^\s*([^/\s]+)\/([^/\s]+)\s+(\S+)(?:\s+\[([^\]]+)\])?\s+(.*)"
pattern = r"^(\S+)\/(\S+)\s+(\S+)(?:\s+\(([^)]+)\))?(?:\s+\(([^)]+)\))?\s+(.*)"

pattern = r"^(\S+)\/(\S+)\s+(\S+)\s+(?:\(([^)]+)\))?\s+(?:\(([^)]+)\))?\s+(?:\(([^)]+)\))?\s+(.*)"
import sys

import subprocess

if len(sys.argv) != 2:
    print("No name specified!")
    exit(1)


update_pattern = r"^(\S+)"

updates = subprocess.getoutput(f"checkupdates")

updates = list(re.findall(update_pattern, updates))



example = subprocess.getoutput(f"yay -Ss {sys.argv[1]}")
# example = subprocess.getoutput(f"pacman -Q {sys.argv[1]}")
# print(example)

# match = re.findall(pattern, example)


results = {

}

# pattern = r"^\s*([^/\s]+)\/([^/\s]+)\s+(\S+)(?:\s+\[(installed)\])?\s+(.*)"


matches = re.findall(pattern, example, re.MULTILINE)
# Colour codes: https://en.wikipedia.org/wiki/ANSI_escape_code
form = {"special": ([0, 10], ""),
        "normal": ([30, 38], ""),
        "normal_inverted": ([40, 48], " inverted"),
        "bright": ([90, 98], " bright"),
        "bright_inverted": ([100, 108], " bright inverted"),
        }

special = ["reset", "bold", "faint", "italic", "underline", "slow blink", "fast blink", "invert", "hide", "strike", "default"]
colors = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]

placeholders = {}

# Generate colors
for item in form:
    if item == "special":
        for n, k in enumerate(special):
            placeholders["<"+k.upper()+">"] = "\x1b[%sm" % n
    else:
        for i, v in enumerate(range(*form[item][0])):
            placeholders["<"+colors[i].upper()+form[item][1].upper()+">"] = "\x1b[%sm" % v




    

# exit()
# for match in matches:
#     package = match[0]
#     name = match[1]
#     version = match[2]
#     description = match[5]
#     status = match[4] if match[3] is None else match[3]

#     print("Package:", package)
#     print("Name:", name)
#     print("Version:", version)
#     print("Description:", description)
#     print("Status:", status)
#     print()
for match in matches:
    # print(match)
    # repository = match[0]
    # name = match[1]
    # version = match[2]
    # # is_installed = match[3] == "installed"
    # is_installed = "installed" in match[3]
    # description = match[4]

    repository = match[0]
    name = match[1]
    version = match[2]
    data = match[3]
    # is_installed = "installed" in match[4].lower()
    status = " "

    if name in updates:
        status = placeholders["<BLUE BRIGHT>"] + "U"
    elif "installed" in match[4].lower():
        status = placeholders["<GREEN BRIGHT>"] + "I"
    elif "orphan" in match[4].lower():
        status = placeholders["<RED BRIGHT>"] + "R"
    
    description = match[6]

    item = (name, version, description, status)

    if repository in results:
        results[repository].append(item)
    else:
        results[repository] = [item]


def test():
    print("\nIgnore index\n")
    for i, thing in enumerate(placeholders):
        print(i, thing, placeholders[thing]+"Hello World!"+placeholders["<RESET>"])

# test()

names = []


out = ""

length = 25
count = 0
for repo in results:
    out += placeholders["<YELLOW BRIGHT>"] + repo + placeholders["<RESET>"] + "/\n"

    for (name, version, description, status) in results[repo]:
        this = placeholders["<MAGENTA>"] + " " + str(count) + placeholders["<RESET>"] + " "
        this += " "*(3 - len(str(count)))
        this += f"[{status+placeholders['<RESET>']}] "

        this += name

        this += " "*(length - len(name))

        this += placeholders["<WHITE>"] + placeholders["<ITALIC>"] + description[:50] + placeholders["<RESET>"] + " "

        this += placeholders["<BLUE BRIGHT>"] + version + placeholders["<RESET>"]

        this += "\n"

        names.append(name)

        out += this
        count += 1
    out += "\n"

        


print(out)

num = 0


while True:
    a = input()

    if a == "":
        # print("Empty")
        exit(0)
        break

    try:
        num = int(a)
        if 0 <= num < count:
            print(subprocess.getoutput(f"yay -Si {names[num]}"))
        else:
            print("Invalid Number")
            continue
    except:
        print("Invalid Number")

# print(names[num])

