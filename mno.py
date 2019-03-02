colors = [
    "000000",
    "0a0a0a",
    "191919",
    "333333",
    "4c4c4c",
    "666666",
    "7f7f7f",
    "999999",
    "b2b2b2",
    "cccccc",
    "e5e5e5",
    "f5f5f5",
    "ffffff",
]


def convert():
    lht = open("themes/lht.json", "r")
    drk = open("themes/drk.json", "w")

    lines = []

    for line in lht.readlines():
        if any(clr in line for clr in colors):
            lht_clr = "".join(list(line.split("#")[1])[:6])
            lht_clr_ndx = colors.index(lht_clr)

            drk_clr_ndx = (int(lht_clr_ndx) * -1) - 1
            drk_clr = colors[drk_clr_ndx]

            line = line.replace(lht_clr, drk_clr)
            lines.append(line)
        else:
            lines.append(line)

    drk.write("".join(lines))


if __name__ == "__main__":
    convert()
