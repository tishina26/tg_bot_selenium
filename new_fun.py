import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import UnexpectedAlertPresentException
import telebot
from selenium.webdriver.common.keys import Keys

bot = telebot.TeleBot('5129230592:AAE0Jw1ikNmgTSBgQ4svS5bWCBrxFsy_o4k')

from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

set_page_load_timeout(30)

@bot.message_handler(content_types=['text'])
def main(driver, log, pas, days_kck, id):
    driver.get('http://www.lowadi.com')
    time.sleep(3)
    def check_exists_by_xpath(webdriver, xpath):
        try:
            webdriver.find_element_by_xpath(xpath)
        except:
            return False
        '''except NoSuchElementException:
            return False
        except StaleElementReferenceException:
            return False'''
        return True

    def check_alert(webdriver):
        try:
            #selenium.chooseOkOnNextConfirmation()
            #driver.Keyboard.PressKey(Keys.ENTER);
            #driver.send_keys(u'\ue007')
            Alert(driver).accept()
        except:
            return False
        return  True

    def check_exists_by_id(webdriver, id):
        try:
            webdriver.find_element_by_id(id)
        except:
            return False
        '''except NoSuchElementException:
            return False
        except StaleElementReferenceException:
            return False'''
        return True

    def check_click(webdriver):
        try:
            webdriver.click()
        except:
            return False
        '''except ElementNotInteractableException:
            return False
        except StaleElementReferenceException:
            return False
        except ElementClickInterceptedException:
            return False'''
        return True

    def register_to_kck(money):
        if money < 1000:
            print("No money for kck")
            exit(0)
        time.sleep(1.5)

        #kck = driver.find_element_by_id("cheval-inscription")
        string1 = "/html/body/div[9]/main/section/section/div[4]/div/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/a/span[1]"
        # string1 = ""
        string2 = "/html/body/div[8]/main/section/section/div[4]/div/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/a/span[1]"
        string3 = "/html/body/div[7]/main/section/section/div[4]/div/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/a/span[1]"
        if check_exists_by_xpath(driver, string1):
            kck = driver.find_element_by_xpath(string1)
        elif check_exists_by_xpath(driver, string2):
            kck = driver.find_element_by_xpath(string2)
        elif check_exists_by_xpath(driver, string3):
            kck = driver.find_element_by_xpath(string3)
        else:
            print("не нашел, как  нажать на зарегаться в кск")
        #kck = driver.find_element_by_xpath("/html/body/div[8]/main/section/section/div[4]/div/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/a/span[1]")
        time.sleep(1.5)
        kck.click()
        time.sleep(1.5)

        # настраиваем параметры кск - фураж, овес
        begin = time.time()
        while (check_exists_by_id(driver, "fourrageCheckbox")) == False:
            time.sleep(0.5)
            kck.click()
            end = time.time()
            if int(end) - int(begin) > 20:
                print("слишком долго ждем тыканья кнопочки рег в кск")
                return a
        driver.find_element_by_id("fourrageCheckbox").click()
        driver.find_element_by_id("avoineCheckbox").click()
        driver.find_element_by_id("avoineCheckbox").submit()
        time.sleep(1.5)


        # на случай, если не окажется мест, а то ну блин, обидно((
        managed_kck = 0

        begin = time.time()
        while managed_kck == 0:
            end = time.time()
            if int(end) - int(begin) > 30:
                return a
            # выделяем сколько дней
            # !!!!!! НАДО СДЕЛАТЬ МАССИВ СТРИНГОВ С НАЗВАНИЯМИ ДНЕЙ И ПЕРЕД ЗАПУСКОМ ВЫБИРАТЬ НУЖНОЕ!!
            day10 = driver.find_element_by_xpath("//a[text()='10 дней']")
            day10.click()
            time.sleep(1.5)

            # ищем, сколько стоят эти дни
            # РАЗНОЕ TD НАДО ТОЖЕ МАССИВ СТРИНГОВ БЛ****
            table = driver.find_element_by_id("table-0")
            begin = time.time()
            if days_kck == 10:
                string = "//tbody/tr[1]/td[8]/button"
            while check_exists_by_xpath(table, string) == False:
                end = time.time()
                if int(end) - int(begin) > 10:
                    return a
                time.sleep(0.2)
            table = table.find_element_by_xpath(string)
            cnt = int(table.text.replace(" ", ""))

            # проверка, хватает ли средств и тыкаем
            # методом проб и ошибок - если нет средств, то до сюда и не дойдет, проверка есть в начале, но т к робит - не трогаю
            if (money >= cnt):
                table.click()


                time.sleep(1.5)
                check_alert(driver)
                check_alert(driver)
                time.sleep(1.5)


                while check_exists_by_id(driver, "errorsBox") == False:
                    #проверка на то дебильное всплывающее окно
                    #check_alert(driver)
                    #table.click()
                    time.sleep(0.5)

                close_window = driver.find_element_by_id("errorsBox")
                # если не сробит, можно делать на проверку, есть ли кнопка СПАТЬ ну или любая другая, посмотрим
                begin = time.time()
                while check_exists_by_id(driver, "boutonPanser") == False and close_window.get_attribute("style") == "display: none;":
                    end = time.time()
                    if int(end) - int(begin) > 10:
                        return a
                    time.sleep(0.5)
                if check_exists_by_id(driver, "boutonPanser") == True or check_exists_by_id(driver, "boutonPanser") == True:
                    managed_kck = 1
                else:
                    time.sleep(1)
                    close_window = driver.find_element_by_id("errorsBox")
                    close_window = close_window.find_element_by_xpath("//div/div/table/tbody/tr/td[1]/a")
                    time.sleep(1)
                    close_window.click()
                    time.sleep(1)
                    driver.find_element_by_id("avoineCheckbox").submit()
            else:
                print("\n\n\nNO MONEY TO REGISTER TO KCK\n\n\n")

        return

    def traine_horse():
        return

    def walk_horse():
        flag_mountaine = 1 # нужно гулять в горах
        time.sleep(1)

        # проверка на то, если вдруг все погуляли, тогда вкладка ПРОГУЛКА закрыта и выдает ошибку
        if check_exists_by_id(driver, "walk-head-title"):
            walking_open = driver.find_element_by_id("walk-head-title")
            time.sleep(0.5)
            string = walking_open.get_attribute("class")
            if string == "collapse module-style-6-title module-title":
                time.sleep(0.3)
                if check_exists_by_id(driver, "training-body-content"):
                    traine_horse()
                    time.sleep(0.5)
                return

        # проверка на лес
        if check_exists_by_id(driver, "boutonBalade-foret"):
            forest = driver.find_element_by_id("boutonBalade-foret")
            time.sleep(0.5)
            string = forest.get_attribute("class")
            time.sleep(0.1)
            # print(string)
            if string == "tab-action tab-action-select action action-style-4 balade-foret action-disabled":
                return
            time.sleep(0.1)
            begin = time.time()
            while check_click(forest) == False:
                end = time.time()
                if int(end) - int(begin) > 10:
                    return a
                time.sleep(0.01)
            time.sleep(1)
            list_numbers = driver.find_element_by_id("walkforetSlider")
            list_numbers = list_numbers.find_element_by_tag_name("ol")
            list_hours = list_numbers.find_elements_by_tag_name("li")
            index = 0

            # index - 1 это последний возможный нажатый индекс (ищем его)
            for i in list_hours:
                time.sleep(0.1)
                class_of_li = i.get_attribute("class")
                if (class_of_li == "green disabled") or (class_of_li == "green hiddenNumber disabled"):
                    time.sleep(0.5)
                    if (index - 2 > 0):
                        list_hours[index-2].click()
                    break
                index = index + 1
            time.sleep(1)

            # проверим, улучшатся ли тогда навыки? (на основании выездки)
            viesdka = driver.find_element_by_id("walk-foret-dressage").text
            if viesdka != "":
                if (viesdka[0] == '+'):
                    viesdka = viesdka[1:]
                viesdka = float(viesdka)


                if viesdka != 0:
                    driver.find_element_by_id("walk-foret-submit").click()
                    time.sleep(0.5)
                    flag_mountaine = 0 # в горах гулять не нужно - погуляли в лесу
                    return

            # надо закрыть крестиком окошко лес, чтобы появились горы (не уверена, что всегда есть крестик, может возникнуть бесконечный цикл)
            begin = time.time()
            while check_exists_by_id(driver, "walk-tab-balade-foret") == False:
                end = time.time()
                if int(end) - int(begin) > 10:
                    return a
                time.sleep(0.01)
            print("can close i sure нет бесконечного цикла, то есть есть крестик на лесе, надо бы нажать его")

            # исключительно потому, что не уверена насчет беск. цикла
            if (True):
                print("i'm here")
                time.sleep(0.2)
                close_forest = driver.find_element_by_id("walk-tab-balade-foret")
                time.sleep(0.2)
                #string = "/ html / body / div[7] / main / section / section / div[4] / div / div[3] / div[2] / div / div / div / div / div / div[2] / table / tbody / tr[1] / td[2] / a/img"
                #/ html / body / div[8] / main / section / section / div[4] / div / div[3] / div[2] / div / div / div / div / div / div[2] / table / tbody / tr[1] / td[2] / a / img
                #while check_exists_by_xpath(driver, string) == False:
                #    time.sleep(0.5)

                #string3 = "//table/tbody/tr[1]/td[2]/a/img"
                string3 = "/html/body/div[9]/main/section/section/div[4]/div/div[3]/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[2]/a/img"
                string2 = "/html/body/div[7]/main/section/section/div[4]/div/div[3]/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[2]/a"
                #string1 = "/html/body/div[8]/main/section/section/div[4]/div/div[3]/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[2]/a"
                string1 = "//div[@id='walk-tab-balade-foret']//img[@alt='consoleclose']"

                time.sleep(1.5)
                if check_exists_by_xpath(driver, string1) == True or  check_exists_by_xpath(driver, string1) == True:
                    close_forest = driver.find_element_by_xpath(string1)
                    #close_forest = close_forest.find_element_by_xpath("/ html / body / div[8] / main / section / section / div[4] / div / div[3] / div[2] / div / div / div / div / div / div[2] / table / tbody / tr[1] / td[2] / a / img")
                    time.sleep(0.5)
                    print("try to close forest1")
                    begin = time.time()
                    while (check_click(close_forest) == False):
                        end = time.time()
                        if int(end) - int(begin) > 10:
                            print("more 10 s")
                            return a
                        time.sleep(0.5)
                    print("closed forest")
                elif check_exists_by_xpath(driver, string2) == True or  check_exists_by_xpath(driver, string2) == True:
                    close_forest = driver.find_element_by_xpath(string2)
                    #close_forest = close_forest.find_element_by_xpath("/ html / body / div[8] / main / section / section / div[4] / div / div[3] / div[2] / div / div / div / div / div / div[2] / table / tbody / tr[1] / td[2] / a / img")
                    time.sleep(0.5)
                    print("try to close forest2")
                    begin = time.time()
                    while (check_click(close_forest) == False):
                        end = time.time()
                        if int(end) - int(begin) > 10:
                            return a
                        time.sleep(0.5)
                    print("closed forest")
                elif check_exists_by_xpath(driver, string3) == True or  check_exists_by_xpath(driver, string3) == True:
                    close_forest = driver.find_element_by_xpath(string3)
                    #close_forest = close_forest.find_element_by_xpath("/ html / body / div[8] / main / section / section / div[4] / div / div[3] / div[2] / div / div / div / div / div / div[2] / table / tbody / tr[1] / td[2] / a / img")
                    time.sleep(0.7)
                    #"/html/body/div[8]/main/section/section/div[4]/div/div[3]/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[2]/a/img
                    print("try to close forest3")
                    begin = time.time()
                    while (check_click(close_forest) == False):
                        end = time.time()
                        if int(end) - int(begin) > 10:
                            return a
                        time.sleep(0.5)
                    print("closed forest")
                else:
                    print("бля, не закрыли лес фак")

        time.sleep(1)
        flag_traine = 1 # приступим к тренировкам?

        if (flag_mountaine == 1) and (check_exists_by_id(driver, "boutonBalade-montagne")):
            mount = driver.find_element_by_id("boutonBalade-montagne")
            time.sleep(1)
            begin = time.time()
            while check_click(mount) == False:
                end = time.time()
                if int(end) - int(begin) > 10:
                    return a
                time.sleep(0.05)
            time.sleep(1)

            # список всех получасов
            list_numbers = driver.find_element_by_id("walkmontagneSlider")
            list_numbers = list_numbers.find_element_by_tag_name("ol")
            list_hours = list_numbers.find_elements_by_tag_name("li")
            index = 0

            # index - 1 это последний возможный нажатый индекс(ищем)
            for i in list_hours:
                time.sleep(0.1)
                class_of_li = i.get_attribute("class")
                if (class_of_li == "green disabled") or (class_of_li == "green hiddenNumber disabled"):
                    time.sleep(0.5)
                    if (index - 2 > 0):
                        list_hours[index - 2].click()
                    break
                index = index + 1
            time.sleep(0.5)

            # проверим, улучшатся ли тогда навыки? На основе скорости
            scorost = driver.find_element_by_id("walk-montagne-vitesse").text
            if (scorost != ""):
                if (scorost[0] == '+'):
                    scorost = scorost[1:]
                scorost = float(scorost)

                if scorost != 0:
                    driver.find_element_by_id("walk-montagne-submit").click()
                    flag_traine = 0  # в горах гулять не нужно - погуляли в лесу
                    return
            else:
                scorost = 0
                flag_traine = 0

        # в ином случае надо тренировки начать, поднастроить надо,хз, робит ли
        time.sleep(2)
        if (flag_traine == 1) and (check_exists_by_id(driver, "training-body-content")):
            traine_horse()
            time.sleep(0.5)
        time.sleep(0.5)

        return

    def play_lit_horse():
        if check_exists_by_id(driver, "boutonJouer"):
            play = driver.find_element_by_id("boutonJouer")

            # вдруг нельзя поиграть
            if play.get_attribute("class") == "action action-style-4 jouer action-disabled":
                return
            time.sleep(0.2)

            play.click()
            time.sleep(0.2)

            # список всех получасиков
            list_numbers = driver.find_element_by_id("centerPlaySlider")
            list_numbers = list_numbers.find_element_by_tag_name("ol")
            list_hours = list_numbers.find_elements_by_tag_name("li")
            #index = 0
            # index - 1 это последний возможный нажатый индекс (ищем)
            for index in range(0, 22):
                #time.sleep(0.1)
                class_of_li = ""
                if index < 21:
                    i = list_hours[index]
                    class_of_li = i.get_attribute("class")
                    #print(index, class_of_li)
                #print(index)

                # нашли первый закрытый для нажатий
                if index == 21 or (class_of_li == "green disabled") or (class_of_li == "green hiddenNumber disabled"):
                    #print("нашли границу")
                    #time.sleep(0.1)
                    if (index > 0):
                        #print("click" , index)
                        list_hours[index-1].click()
                    else:
                        #print("no ", index)
                        # закрыть окно с игрой
                        #close_window = driver.find_element_by_id("care-tab-play")
                        #time.sleep(0.8)
                        string1 = "/html/body/div[9]/main/section/section/div[4]/div/div[1]/div[2]/div/div/div[1]/div/div[1]/div[3]/table/tbody/tr[1]/td[2]/a/img"
                        string2 = "/html/body/div[8]/main/section/section/div[4]/div/div[1]/div[2]/div/div/div[1]/div/div[1]/div[3]/table/tbody/tr[1]/td[2]/a/img"
                        string3 = "/html/body/div[7]/main/section/section/div[4]/div/div[1]/div[2]/div/div/div[1]/div/div[1]/div[3]/table/tbody/tr[1]/td[2]/a/img"
                        if check_exists_by_xpath(driver, string1):
                            close_window = driver.find_element_by_xpath(string1)
                        elif check_exists_by_xpath(driver, string2):
                            close_window = driver.find_element_by_xpath(string2)
                        elif check_exists_by_xpath(driver, string3):
                            close_window = driver.find_element_by_xpath(string3)
                        else:
                            print("не нашел, как закрыть окно с играми")
                            return a
                        time.sleep(0.1)
                        #print("start closing - what's the problem")
                        begin = time.time()
                        while check_click(close_window) == False:
                            end = time.time()
                            if int(end) - int(begin) > 10:
                                return a
                            time.sleep(0.2)
                        return
                    break
                #index = index + 1

            time.sleep(0.5)
            driver.find_element_by_id("formCenterPlaySubmit").click()
            time.sleep(0.5)

            # обязательно кормим морковкой, иначе плохо будет
            try:
                driver.find_element_by_id("boutonCarotte").click()
            except:
                return
            time.sleep(0.2)

        return

    def feed_horse():
        # вдруг можем дать молока
        if (check_exists_by_id(driver, "boutonAllaiter")):
            driver.find_element_by_id("boutonAllaiter").click()
            return
        time.sleep(0.5)
        # если есть окно с покормить, вообще лучше потом заменить на while, но ето потом
        if (check_exists_by_id(driver, "boutonNourrir") == True) or (check_exists_by_id(driver, "boutonNourrir") == True):
            feed_window = driver.find_element_by_id("boutonNourrir")
            time.sleep(0.2)
            begin = time.time()
            while (check_click(feed_window) == False):
                end = time.time()
                if int(end) - int(begin) > 10:
                    return a
                time.sleep(0.01)

            # глобальная проверка, а вдруг мы уже покормились?))
            # найдем, сколько уже было дано фуража
            was_feed = driver.find_element_by_id("feeding")
            was_feed = was_feed.find_element_by_xpath("//table[1]/tbody/tr[2]/td[1]/span[2]").text
            if int(was_feed[0]) != 0:
                close_fourage = driver.find_element_by_id("care-tab-feed")
                close_fourage = close_fourage.find_element_by_xpath("//table/tbody/tr[1]/td[2]/a")
                begin = time.time()
                while (check_click(close_fourage) == False):
                    end = time.time()
                    if int(end) - int(begin) > 10:
                        return a
                    time.sleep(0.01)
                return

            # сколько дать фуража
            max_fourrage = driver.find_element_by_id("feeding")
            max_fourrage = max_fourrage.find_element_by_xpath("//table[1]/tbody/tr[2]/td[1]/span[2]/strong")
            max_fourrage = max_fourrage.text
            if (max_fourrage[-1] == ' '):
                max_fourrage = max_fourrage[:-1]

            max_fourrage = int(max_fourrage)
            time.sleep(0.2)

            # кормим фуражом
            tmp_fourrage = driver.find_element_by_id("haySlider")
            tmp_fourrage = tmp_fourrage.find_element_by_tag_name("ol")
            tmp_fourrage = tmp_fourrage.find_elements_by_tag_name("li")
            tmp_fourrage = tmp_fourrage[max_fourrage]
            time.sleep(0.2)
            tmp_fourrage.click()
            time.sleep(0.2)

            # теперь овёс
            # сколько дать овса
            max_avoine = driver.find_element_by_id("feeding")
            time.sleep(0.2)
            # возможно это ребенок и ему не нужен овес, проверим, есть ли окно с овсом
            if check_exists_by_xpath(max_avoine, "//table[1]/tbody/tr[4]/td[1]/span[2]/strong") == True:
                max_avoine = max_avoine.find_element_by_xpath("//table[1]/tbody/tr[4]/td[1]/span[2]/strong")
                max_avoine = max_avoine.text
                time.sleep(0.1)
                if (max_avoine[-1] == ' '):
                    max_avoine = max_avoine[:-1]
                max_avoine = int(max_avoine)

                time.sleep(0.2)
                # кормим овсом
                if max_avoine != 0:
                    tmp_avoine = driver.find_element_by_id("oatsSlider")
                    tmp_avoine = tmp_avoine.find_element_by_tag_name("ol")
                    tmp_avoine = tmp_avoine.find_elements_by_tag_name("li")
                    tmp_avoine = tmp_avoine[max_avoine]
                    print(max_avoine)
                    time.sleep(0.2)
                    begin = time.time()
                    while check_click(tmp_avoine) == False:
                        end = time.time()
                        if int(end) - int(begin) > 10:
                            return a
                        time.sleep(0.5)

            time.sleep(0.5)

            # и наконец, кормим, юхуу
            driver.find_element_by_id("feed-button").click()
        time.sleep(0.5)

        return

    def check_baby():
        time.sleep(0.2)
        #print("checking")
        if check_exists_by_id(driver, "boutonVeterinaire") == True or check_exists_by_id(driver, "boutonVeterinaire") == True:
            wdriver = driver.find_element_by_id("boutonVeterinaire")
            time.sleep(0.5)
            wdriver.click()
            time.sleep(2)
            wdriver = driver.find_element_by_id("poulain-1")
            time.sleep(0.5)
            wdriver.click()
            time.sleep(0.5)
            wdriver.send_keys("Крез Младший")
            #wdriver = driver.find_element_by_id("boutonChoisirNom")
            wdriver.submit()
        #else:
            #print("не нашел деточек")


    def take_care():
        time.sleep(0.2)
        money = driver.find_element_by_id("reserve")
        money = int(money.text.replace(" ", ""))
        if check_exists_by_id(driver, "cheval-inscription"):
            register_to_kck(money)
        time.sleep(0.3)
        clear = driver.find_element_by_id("boutonPanser") # чистим
        clear.click()
        time.sleep(0.4)
        # делаем миссию
        if check_exists_by_id(driver, "boutonMissionEquus"):
            driver.find_element_by_id("boutonMissionEquus").click()
        if check_exists_by_id(driver, "boutonMissionMontagne"):
            driver.find_element_by_id("boutonMissionMontagne").click()
        if check_exists_by_id(driver, "boutonMissionForet"):
            driver.find_element_by_id("boutonMissionForet").click()
        if check_exists_by_id(driver, "boutonMissionPlage"):
            driver.find_element_by_id("boutonMissionPlage").click()

        walk_horse()
        time.sleep(0.4)

        play_lit_horse()
        time.sleep(0.4)

        feed_horse()
        begin = time.time()
        while check_click(driver.find_element_by_id("boutonBoire")) == False: # поим
            end = time.time()
            if int(end) - int(begin) > 10:
                return a
            time.sleep(0.1)
        time.sleep(0.2)
        begin = time.time()
        while check_click(driver.find_element_by_id("boutonCaresser")) == False: # ласка
            end = time.time()
            if int(end) - int(begin) > 10:
                return a
            time.sleep(0.01)

        # пытаемся накормить морковкой и комбикормом
        carrot = driver.find_element_by_id("center-tab-main")
        feeded_Mash = 0
        if check_exists_by_xpath(carrot, "//div[@class='fullwidth']/table/tbody/tr[4]/td/div/div/div[2]/span[3]"):
            carrot = carrot.find_element_by_xpath("//div[@class='fullwidth']/table/tbody/tr[4]/td/div/div/div[2]/span[3]")
            # print("loser  ", carrot.get_attribute("data-tooltip"))
            if carrot.get_attribute("data-tooltip") == "Этот конноспортивный комплекс предлагает морковь":
                begin = time.time()
                while check_click(driver.find_element_by_id("boutonCarotte")) == False:
                    end = time.time()
                    if int(end) - int(begin) > 10:
                        return a
                    time.sleep(0.01)
            elif carrot.get_attribute("data-tooltip") == "Этот конноспортивный комплекс предлагает комбикорма":
                if check_exists_by_id(driver, "boutonMash") == True or check_exists_by_id(driver, "boutonMash") == True:
                    begin = time.time()
                    while check_click(driver.find_element_by_id("boutonMash")) == False:
                        end = time.time()
                        if int(end) - int(begin) > 10:
                            return a
                        time.sleep(0.01)
                    feeded_Mash = 1

        time.sleep(0.6)

        if (feeded_Mash == 0) and (check_exists_by_xpath(carrot, "//div[@class='fullwidth']/table/tbody/tr[4]/td/div/div/div[2]/span[4]") == True):
            time.sleep(0.3)
            mash = carrot.find_element_by_xpath("//div[@class='fullwidth']/table/tbody/tr[4]/td/div/div/div[2]/span[4]")
            # print("okey, try  ", mash.get_attribute("data-tooltip"))
            if mash.get_attribute("data-tooltip") == "Этот конноспортивный комплекс предлагает комбикорма":
                if check_exists_by_id(driver, "boutonMash") == True or check_exists_by_id(driver, "boutonMash") == True:
                    begin = time.time()
                    while check_click(driver.find_element_by_id("boutonMash")) == False:
                        end = time.time()
                        if int(end) - int(begin) > 10:
                            return a
                        time.sleep(0.01)
        time.sleep(0.5)

        # теперь баиньки
        sleep = driver.find_element_by_id("boutonCoucher")
        sleep.click()
        #time.sleep(0.2)

        return

    # отказаться от файлов cookie
    search_box = driver.find_element_by_class_name('sowcle-form')
    search_box = search_box.find_element_by_xpath("//div[@class='grid-cell odd middle  pr--1']")
    search_box = search_box.find_element_by_tag_name('button')
    while check_click(search_box) == False:
        time.sleep(0.5)

    print("no cookie")

    time.sleep(0.5)

    # нажали ВОЙТИ
    search_box = driver.find_element_by_id('header-login-label')
    while check_click(search_box) == False:
        time.sleep(0.5)
    time.sleep(1)

    # ввели логин
    search_box = driver.find_element_by_id('login')
    # search_box.send_keys('lovely_pony')
    search_box.send_keys(log)
    time.sleep(1)

    # ввели пароль
    search_box = driver.find_element_by_id('password')
    # search_box.send_keys('Ktyjxrf123')
    search_box.send_keys(pas)
    time.sleep(0.5)
    search_box.submit()

    time.sleep(1)

    # нажали КОНЕВОДСТВО
    level1 = driver.find_element_by_id("header-menu")
    level1 = level1.find_element_by_xpath("//div[@class='menu menu-style-1 float-left grid-table']")
    level1 = level1.find_element_by_xpath("//li[@class='level-1 item-menu-elevage float-left']")
    level1 = level1.find_element_by_xpath("//strong[@class='level-1']")
    while check_click(level1) == False:
        time.sleep(0.1)

    bot.send_message(id, "succesfully logged in")

    # нажали ЛОШАДИ
    level1 = level1.find_element_by_xpath("//a[@href='/elevage/chevaux/']")
    time.sleep(0.5)
    while check_click(level1) == False:
        time.sleep(0.1)
    time.sleep(1.5)

    # перейдем во второй конезавод (ЗАКОММЕНТИТЬ, ЕСЛИ ОСТАТЬСЯ В ОБЩИХ ЛОШАДЯХ)

    '''
    next_house = driver.find_element_by_id("select-tab-1497539")
    time.sleep(0.5)
    next_house.click()
    time.sleep(0.6)
    '''

    # ищем общее количество лошадей

    tmp = driver.find_element_by_id("linkBlocRecherche")
    time.sleep(0.1)
    tmp.click()
    time.sleep(0.5)
    tmp = driver.find_element_by_id("horseSearchLink-criteres")
    time.sleep(0.5)
    tmp.click()
    time.sleep(0.5)
    tmp = driver.find_element_by_id("horseSearchCoucheCheckbox")
    time.sleep(0.5)
    tmp.click()
    time.sleep(0.5)
    tmp7 = tmp
    tmp7.click()
    tmp1 = driver.find_element_by_id("horseSearchSubmit")
    time.sleep(0.5)
    # ДВА РАЗА НАЖМЕМ, А ТО БЫЛИ КОСЯКИ
    while check_click(tmp1) == False:
        time.sleep(0.1)
    #while check_click(tmp1) == False:
    #    time.sleep(0.5)

    while check_exists_by_id(driver, "tab-select-all-horses") == False:
        time.sleep(0.5)
    time.sleep(0.5)
    tmp2 = driver.find_element_by_id("tab-select-all-horses")
    while check_exists_by_xpath(tmp2, "//span[@class='count']") == False:
        time.sleep(0.5)
    tmp2 = tmp2.find_element_by_xpath("//span[@class='count']")
    cnt_all_horses = tmp2.text[1:-1]
    cnt_all_horses = int(cnt_all_horses)
    print("THERE ARE", cnt_all_horses, "HORSES AT ALL")
    bot.send_message(id, "THERE ARE " + str(cnt_all_horses) + " HORSES AT ALL")

    time.sleep(0.5)
    if cnt_all_horses == 0:
        print("all horses were done")
        bot.send_message(id, "done")
        return 0
        #exit(0)

    # нашли первую лошадку
    horse1 = driver.find_element_by_id("horseList")
    horse1 = horse1.find_element_by_xpath("//div[@class='damier-table grid-table width-100']")
    horse1 = horse1.find_element_by_xpath("//a[@class='horsename']")

    #horse1 = driver.find_element_by_xpath("//a[@href='/elevage/chevaux/cheval?id=72135709']")

    horse1.click()

    def change_name():
        time.sleep(0.2)
        plus = driver.find_element_by_id("widget--1")
        plus.find_element_by_tag_name("button").click()
        time.sleep(0.1)
        plus.find_element_by_xpath("//div[@class='options-menu']/ul/li[1]/a").click()
        time.sleep(0.1)
        name = driver.find_element_by_id("horseNameName")
        name.send_keys(Keys.CONTROL + "a");
        name.send_keys("Крез Младший")
        name.submit()
        return

    for i in range(0, cnt_all_horses):
        time.sleep(0.4)

        # следующая лошадка (ну да, первую в конце обработаем, ахах)
        next = driver.find_element_by_id("nav-next")
        time.sleep(0.3)
        while check_click(next) == False:
            time.sleep(0.1)
        time.sleep(0.1)

        # проверка на беременность, ахах

        #cnt_all_horses = check_any() + 1
        #time.sleep(0.5)

        # заботимся
        time_before = int(time.time())

        time.sleep(0.2)
        check_baby()
        #time.sleep(0.4)

        #change_name()

        time.sleep(0.2)
        take_care()
        time.sleep(0.2)
        time_after = int(time.time())


        # немного статистики, а то скучно
        print("FINISHED", i + 1, " OF ", cnt_all_horses, " IT'S ", int((i + 1) / cnt_all_horses * 100), "%")
        bot.send_message(id, "FINISHED " + str(i + 1) + " OF " + str(cnt_all_horses) + " IT'S " + str(int((i + 1) / cnt_all_horses * 100)) + "%" + "spent " + str(time_after - time_before) + " seconds")

        print("spent ", time_after - time_before, " seconds")
        #bot.send_message(id, "spent " + str(time_after - time_before) + " seconds")

