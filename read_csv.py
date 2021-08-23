# -*- coding: utf-8 -*-
import csv
import web_driver

ar_csv = [] # Массив для сохранения файла
def add_row_csv(cnt, tovar_name, tovar_ves, tovar_shirina, tovar_visota, tovar_glubina, tovar_url):
    global ar_csv
    ar_csv.append([cnt, tovar_name, tovar_ves, tovar_shirina, tovar_visota, tovar_glubina, tovar_url])

def save_allrow_csv():
    with open('result_file.csv', mode = 'w', encoding='utf-8') as save_csv:
        employee_writer = csv.writer(save_csv, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for el in ar_csv:
            employee_writer.writerow(el)


with open('export_file.csv', 'r', newline='', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter="\t", quotechar='"')
    cnt = 0
    for row in spamreader:
        cnt += 1
        print(cnt,len(row),len(row[1]),len(row[2]),len(row[3]))
        #print(row[0])
        tovar_name = row[0].strip()
        tovar_ves = ""
        tovar_shirina = ""
        tovar_visota = ""
        tovar_glubina = ""
        tovar_url = ""
        if (cnt == 1): # Пропускаем первую страницу
            add_row_csv(cnt, tovar_name, tovar_ves, tovar_shirina, tovar_visota, tovar_glubina,tovar_url)
            continue
            
        if (cnt <= 7266): # Ранее загруженные товары Пропускаем
            add_row_csv(cnt, tovar_name, tovar_ves, tovar_shirina, tovar_visota, tovar_glubina,tovar_url)
            continue
            
        if (len(row[1]) == 0) and (len(row[2]) == 0) and (len(row[3]) == 0): # Пропускаем группу товаров
            print("Группа товаров",row[0])
            add_row_csv(cnt, tovar_name, tovar_ves, tovar_shirina, tovar_visota, tovar_glubina,tovar_url)
            continue
        #if cnt>=10: # ---------TEST MODE------------
        #    break
        str_tovar = row[0].strip()+" "+row[2].strip()
        tovar_info = web_driver.get_tovar_param(str_tovar)
        print(tovar_info)
        if not tovar_info == False :
            tovar_ves = str(tovar_info.get("ves"))
            tovar_shirina = str(tovar_info.get("shirina"))
            tovar_visota = str(tovar_info.get("visota"))
            tovar_glubina = str(tovar_info.get("glubina"))
            tovar_url = str(tovar_info.get("url"))
                
        add_row_csv(cnt, tovar_name, tovar_ves, tovar_shirina, tovar_visota, tovar_glubina,tovar_url)
        save_allrow_csv()
save_allrow_csv()    