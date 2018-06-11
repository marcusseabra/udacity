"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in the range as described above,
  write that line to the output_good file
- if the value of the field is not a valid year as described above,
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

You can write helper functions for checking the data and writing the files, but we will call only the
'process_file' with 3 arguments (inputfile, output_good, output_bad).
"""
import csv
import pprint
import re

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'
ANO_INICIAL = 1886
ANO_FINAL = 2014

def process_file(input_file, output_good, output_bad):

    linhas_interesse = []
    linhas_descarte = []
    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        # Recurso de expressao regular para busca de DBPedia em strings de interesse
        p = re.compile('DBPedia', re.IGNORECASE)
        for linhas in reader:
            # Verifica a existencia da expressao regular na string, no caso, a coluna URI
            # Busca pela string DBPedia no conteudo da coluna
            if p.search(linhas["URI"]):
                ano = str(linhas["productionStartYear"])
                # Valida a existencia de um numero (ano) na string
                n = re.compile('\d')
                if n.match(ano[:4]):
                    ano_interesse = int(ano[:4])
                    if ano_interesse >= ANO_INICIAL and ano_interesse <= ANO_FINAL:
                        linhas["productionStartYear"] = ano_interesse
                        linhas_interesse.append(linhas)
                    else:
                        linhas_descarte.append(linhas)
                else:
                    linhas_descarte.append(linhas)

    # This is just an example on how you can use csv.DictWriter
    # Remember that you have to output 2 files

    with open(output_good, "w") as g:
        writer = csv.DictWriter(g, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in linhas_interesse:
            writer.writerow(row)

    with open(output_bad, "w") as g:
        writer = csv.DictWriter(g, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in linhas_descarte:
            writer.writerow(row)

def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()
