import csv
import re

def generer_csv_propre():
    with open('DumpFile.txt', 'r', encoding='utf-8') as f:
        lignes = f.readlines()

    with open('Donnee_Reseau.csv', 'w', newline='', encoding='utf-8-sig') as f_csv:
        writer = csv.writer(f_csv, delimiter=';')
        writer.writerow(['Heure', 'Source', 'Destination', 'Info'])

        for ligne in lignes:
            # Motif général : accepte IP OU noms de machines
            match = re.search(
                r'(\d{2}:\d{2}:\d{2}\.\d+)\sIP\s([\w\.-]+)\s>\s([\w\.-]+):\s(.*)',
                ligne
            )

            if match:
                writer.writerow([
                    match.group(1),  # Heure
                    match.group(2),  # Source
                    match.group(3),  # Destination
                    match.group(4)   # Infos du paquet
                ])

generer_csv_propre()
print("Donnee_Reseau.csv créé.")