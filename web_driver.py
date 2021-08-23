# -*- coding: utf-8 -*-
import time
#import sys
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

options = Options() # Не показывать экран браузера
options.add_argument('--headless') # Не показывать экран браузера
#browser = webdriver.Firefox() # Показывать экран браузера
browser = webdriver.Firefox(options=options) # НЕ показывать экран браузера

def get_tovar_param(tovar_name):
    browser.get('https://www..ru/')
    assert 'Wildberries' in browser.title
    elem = browser.find_element_by_class_name('search-catalog__input')  # Find the search box
    elem.send_keys(tovar_name + Keys.RETURN)
    time.sleep(5)
    #with open("test.html", "w", encoding='utf-8') as f:
    #    f.write(browser.page_source)
        #print(browser.page_source)
    # Поиск строки: По Вашему запросу ничего не найдено. searching-results__text
    with open("test.html", "w", encoding='utf-8') as f:
        f.write(browser.page_source)
    try:
        elem = browser.find_element_by_css_selector('p.searching-results__text')
    except Exception as err:
        print(err)
        elem = False
    if not elem == False :
        str_p = str(elem.text).strip()
        if str_p == "По Вашему запросу ничего не найдено.":
            print(str_p)
            #browser.quit()
            return False
    # Поиск первой ссылки на товар
    list_a = browser.find_elements_by_class_name('product-card__main')
    tovar_link = ""
    if len(list_a)>0 :
        tovar_link = ""
        for elm_a in list_a:
            print(elm_a.get_attribute('href'))
            tovar_link = str(elm_a.get_attribute('href'))
            break
    if tovar_link == False:
        print("Error find link")
        #browser.quit() # Завершить программу
        return False
    print("Ссылка на товар",tovar_link)
    try:
        browser.get(tovar_link) # Открываем в браузере ссылку
    except Exception as err:
        print("Error open link",err)
        #browser.quit() # Завершить программу
        return False
        
    time.sleep(5) # Ждем загрузку
    
    list_elem = browser.find_elements_by_class_name('collapsible__toggle') # Поиск кнопки развернуть 
    if len(list_a)>0 :
        for elm_a in list_elem:
            print(elm_a.text)
            if str(elm_a.text) == "Развернуть характеристики" :
                elm_a.click()

    list_a = browser.find_elements_by_class_name('product-params__row')
    if len(list_a)>0 :
        tovar_ves = "" # Вес товара
        tovar_shirina = "" # Ширина товара
        tovar_visota = "" # Высота товара
        tovar_glubina = "" # Глубина товара
        for elm_a in list_a:
            tovar_param = str(elm_a.text)
            print(tovar_param)
            str_find = "Вес товара с упаковкой (г)"
            if tovar_param.find(str_find)>-1:
                tovar_ves = tovar_param.replace(str_find,"").strip()
            str_find = "Ширина упаковки"
            if tovar_param.find(str_find)>-1:
                tovar_shirina = tovar_param.replace(str_find,"").strip()
            str_find = "Высота упаковки"
            if tovar_param.find(str_find)>-1:
                tovar_visota = tovar_param.replace(str_find,"").strip()
            str_find = "Глубина упаковки"
            if tovar_param.find(str_find)>-1:
                tovar_glubina = tovar_param.replace(str_find,"").strip()
        #with open("test.html", "w", encoding='utf-8') as f:
        #   f.write(browser.page_source)
        #product-params__row
        print("Вес, ширина, высота, глубина",tovar_ves,tovar_shirina,tovar_visota,tovar_glubina)
        #browser.quit()
        return {'ves':tovar_ves,'shirina':tovar_shirina,'visota':tovar_visota,'glubina':tovar_glubina,'url':tovar_link}
    else:
        #browser.quit()
        return False

#tovar_info = get_tovar_param('Forest-шампунь для волос Genwood, 1000 мл.	GW/SG1 	Estel')
#print(tovar_info)