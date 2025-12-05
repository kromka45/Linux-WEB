import click
import os

DOMYSLNY_DESKTOP = r"C:\Users\Kromka\Desktop"


def resolve_path(path):
    if os.path.isabs(path):
        return path
    return os.path.join(DOMYSLNY_DESKTOP, path)


def extract_mod_name(path_line):
    """
    Przykład:
    C:\..\addons\ADSSway-Conf-LOW_65735... → ADSSway-Conf-LOW_
    """
    base = os.path.basename(path_line.strip())
    parts = base.split("_")
    if len(parts) > 1:
        return parts[0] + "_"
    return base


@click.command()
@click.argument("plik1", type=str)
@click.argument("plik2", type=str)
@click.argument("wynik", type=str)
def compare_files(plik1, plik2, wynik):

    plik1 = resolve_path(plik1)
    plik2 = resolve_path(plik2)
    wynik = resolve_path(wynik)

    if not os.path.exists(plik1):
        return click.echo(f"❌ Plik nie istnieje: {plik1}")
    if not os.path.exists(plik2):
        return click.echo(f"❌ Plik nie istnieje: {plik2}")

    with open(plik1, "r", encoding="utf-8") as f1:
        set1 = {line.strip() for line in f1}
    with open(plik2, "r", encoding="utf-8") as f2:
        set2 = {line.strip() for line in f2}

    roznice = set1.symmetric_difference(set2)

    with open(wynik, "w", encoding="utf-8") as out:
        for linia in sorted(roznice):
            mod = extract_mod_name(linia)
            out.write(mod + "\n")

    click.echo(f"✔ Gotowe! Wynik zapisany: {wynik}")


if __name__ == "__main__":
    compare_files()
