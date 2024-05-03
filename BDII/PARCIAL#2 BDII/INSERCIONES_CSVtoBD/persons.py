import pandas as pd

datos = pd.read_csv("persons.csv", sep="|")

datos.columns = datos.columns.str.replace("|", "_")

sql_datos_cabecera="insert into persons VALUES ("


def return_insert(values):
    txt_data = ""
    for i in values[:-1]:  
        if str(i) == "nan":
            txt_data = txt_data + "\'\',"
        elif isinstance(i, (int, float)):
            txt_data = txt_data + str(i) + ","
        else:
            txt_data = txt_data + "\'" + str(i) + "\',"
    
    if str(values[-1]) == "nan":
        txt_data = txt_data + "TO_DATE(\'\', 'yyyy/mm/dd'),"
    elif isinstance(values[-1], (int, float)):
        txt_data = txt_data + "TO_DATE(" + str(values[-1]) + ", 'yyyy/mm/dd'),"
    else:
        txt_data = txt_data + "TO_DATE(\'" + str(values[-1]) + "\', 'yyyy/mm/dd'),"

    return txt_data



SQL_FINAL = ""
for indice, fila in datos.iterrows():
    txt = return_insert(fila.values)
    txt = txt[0:-1]  

    SQL_FINAL = SQL_FINAL + sql_datos_cabecera + str(indice+1) + "," + txt + ");\n"


with open("persons.sql", "w", encoding="UTF-8") as f:
    f.write(SQL_FINAL)

