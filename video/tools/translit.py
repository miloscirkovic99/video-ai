"""Spell Serbian Latin text in the orthography of a related language so a
native voice of that language pronounces it close to Serbian."""
import re


def to_slovenian(text: str) -> str:
    # Slovenian already reads c, č, š, ž, dž, lj, nj, h and syllabic r like Serbian.
    return (text.replace("ć", "č").replace("Ć", "Č")
                .replace("đ", "dž").replace("Đ", "Dž"))


def to_czech(text: str) -> str:
    t = text.replace("ć", "č").replace("Ć", "Č").replace("đ", "dž").replace("Đ", "Dž")
    t = t.replace("nj", "ň").replace("Nj", "Ň")
    t = re.sub(r"(?<![cs])h", "ch", t)          # Serbian h = [x] = Czech ch
    t = t.replace("H", "Ch")
    # Czech softens d/t/n before i; Serbian does not, so use hard y.
    t = re.sub(r"([dtnDTN])i", lambda m: m.group(1) + "y", t)
    return t


def to_slovak(text: str) -> str:
    t = text.replace("ć", "č").replace("Ć", "Č").replace("đ", "dž").replace("Đ", "Dž")
    t = t.replace("lj", "ľ").replace("Lj", "Ľ").replace("nj", "ň").replace("Nj", "Ň")
    t = re.sub(r"(?<![cs])h", "ch", t)
    t = re.sub(r"([dtnlDTNL])i", lambda m: m.group(1) + "y", t)
    return t
