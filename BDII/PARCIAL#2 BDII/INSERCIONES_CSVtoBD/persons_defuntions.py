import pandas as pd

datos = pd.read_csv("persons_defuntions.csv", sep="|")

datos.columns = datos.columns.str.replace("|", "_")

sql_datos_cabecera="insert into persons_defuntions VALUES ("


def return_insert(values):
    txt_data = ""
    for i in range(len(values)):  # Recorremos todos los valores
        if i == 0:  # Si es el segundo valor
            if str(values[i]) == "nan":
                txt_data = txt_data + "TO_DATE(\'\', 'yyyy/mm/dd'),"
            elif isinstance(values[i], (int, float)):
                txt_data = txt_data + "TO_DATE(" + str(values[i]) + ", 'yyyy/mm/dd'),"
            else:
                txt_data = txt_data + "TO_DATE(\'" + str(values[i]) + "\', 'yyyy/mm/dd'),"
        else:
            if str(values[i]) == "nan":
                txt_data = txt_data + "\'\',"
            elif isinstance(values[i], (int, float)):
                txt_data = txt_data + str(values[i]) + ","
            else:
                txt_data = txt_data + "\'" + str(values[i]) + "\',"

    return txt_data



SQL_FINAL = ""
for indice, fila in datos.iterrows():
    txt = return_insert(fila.values)
    txt = txt[0:-1]  # Eliminar la última coma

    SQL_FINAL = SQL_FINAL + sql_datos_cabecera + str(indice+1) + "," + txt + ");\n"


with open("persons_defuntions.sql", "w", encoding="UTF-8") as f:
    f.write(SQL_FINAL)
