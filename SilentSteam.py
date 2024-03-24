import sys
import os
import tkinter.filedialog as fd

if len(sys.argv) >= 2 and os.path.isdir(sys.argv[1]):
    folder = sys.argv[1]
else:
    folder = fd.askdirectory()

if not os.path.isdir(folder): sys.exit()

changed = 0

for file in os.listdir(folder):
    if file.endswith(".url"):
        with open(os.path.join(folder, file), "r") as url:
            lines = url.readlines()

        for index, line in enumerate(lines):
            if not line.startswith("URL=steam://rungameid/"):
                continue
            elif not line.endswith('" -silent', 22, -1):
                lines[index] = line[:-1] + '" -silent' + line[-1]

                with open(os.path.join(folder, file), "w") as url:
                    url.writelines(lines)

                changed += 1

                break

print(f"Updated {changed} shortcuts!")
