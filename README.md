# qa_practise

Задание:
1. Написать тест кейс со всеми видами селекторов.

- Реализовал в файле /tests/UI_test.py в функциях test_css_selectors и test_xpath_selectors
2. Недостатки, приемущества xpath и почему.

- К недостаткам можно отнести скорость и труднопонимаемость, 
- к преимуществам можно отнести возможность 
поиска от родителя к потомкам и наоборот и возможность использовать функции contains(), starts-with(), string-length(), not(), normalize-space() 
3. Какие паттерны тестирования на python вы знаете
- имелось в виду паттерны проектирования автотестов? 
- Page Object (реализован в коде form_page.py и тестов UI_test.py функция test_page_object)
 суть заключается в том, что в нем вся функциональность определенного веб-UI оборачивается в класс. Это хорошо для простых просмотров, где нет особых возможностей для взаимодействия – page object ясны и хорошо управляемы.
- Паттерн Screenplay
 Данный паттерн берет page objects и разбивает их на действительно крошечные кусочки. Некоторые тестировщики говорят о том, что это сделало их тесты более ремонтопригодными и надежными.
Еще одним существенным преимуществом является то, что он делает тестовые сценарии более удобочитаемыми.
- Presenter First
Это модификация model-view-controller (MVC) для организации кода и разработки с целью создания полностью протестированного программного обеспечения с использованием test-driven подхода к разработке (TDD).
- Factory/Page Factory
Возник этот паттерн потому, что иногда, чтобы инициализировать вашу страницу, необходимо сделать больше действий, чем просто сказать «new page» или open, или еще что-то. То есть у вас в этой странице скрыта еще какая-то дополнительная логика, и вы хотите ее куда-то зарегистрировать, инициализировать ее элементы и так далее.
- Page Element/Composite List of Items Link Menu Panel Checkbox

4.Какие фреймворки тестирования для python вы знаете
Pytest, PyUnit, Robot Framework, behave, playwright
5.Разница явных и неявных ожиданий. Примеры
Проилюстрируем на примере webdriver, так как playwright не способен так ярко это сделать (хотя в коде есть комменты по этому вопросу)
Явное ожидание — это код, которым вы определяете какое необходимое условие должно произойти для того, чтобы дальнейший код исполнился
```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://somedomain/url_that_delays_loading")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
    driver.quit()
```
Неявное ожидание указывает WebDriver'у опрашивать DOM определенное количество времени, когда пытается найти элемент или элементы, которые недоступны в тот момент.
from selenium import webdriver

```
driver = webdriver.Firefox()
driver.implicitly_wait(10) # seconds
driver.get("http://somedomain/url_that_delays_loading")
myDynamicElement = driver.find_element_by_id("myDynamicElement")
```
6.Тест Кейс на работу с БД
Реализован в db_test.py
7.Тест Кейс на работу с REST API
Реализован в API_test.py
8.Реализация записи видео/скринов в АТ фреймверке
Скрины реализованы в 19 строке UI_test.py
Запись видео в playwright реализовано так
```
context = browser.new_context(record_video_dir="videos/")
# Make sure to close, so that videos are saved.
context.close()
```
9.Allure
В приведенном репозитории вы можете увидеть аллюровский отчет в папке allure-reports/index.html
10.Мокирование сервисов/модулей/backend
Mock-объекты (тестовые дублеры) — это объекты, предназначенные для симуляции поведения реальных объектов во время тестирования.

Тестовые дублеры позволяют:

зафиксировать тестовое окружение, имитируя неважные, нереализованные, нестабильные или медленные внешние объекты (например, БД или сервер),
совершать проверки своих вызовов (обращений к функциям, свойствам).
Применение моков может решить несколько проблем:

— атомарность теста и его информативность (при падении теста не придется решать вопросы локализации дефекта, поскольку баг гнездится исключительно в тестируемом объекте, а не в тех системах, которые он использует);

— снижение его хрупкости вследствие зависимости от сторонних систем (внешних, не тестируемых сервисов и БД);

— позволит создавать необходимые тестовые условия, например, ошибки;

— дополнительным положительным эффектом является снижение времени прохождения теста.
11.Selenium/Selenide/Appium/playwright
- Selenium — это набор программ с открытым исходным кодом, которые применяют для тестирования веб-приложений и администрирования сайтов локально и в сети. Программы Selenium позволяют автоматизировать действия браузера. 
Selenium IDE — плагин для браузера Firefoх для записи действий пользователя.
Selenium RC — устаревшая библиотека для управления браузерами.
Selenium WebDriver — библиотека для управления браузерами.
Selenium Grid — кластер Selenium-серверов для управления браузерами на разных компьютерах в сети.
Selenium Server — сервер для управления браузером удаленно по сети

- Selenide - это обёртка вокруг Selenium WebDriver, позволяющая быстро и просто его использовать при написании тестов, сосредоточившись на логике
- Appium— это бесплатный кроссплатформенный инструмент с открытым исходным кодом, который помогает автоматизировать приложения как для Android, так и для iOS. Appium придерживается того же подхода, что и Selenium WebDriver, который получает HTTP-запросы в формате JSON от клиентов и преобразует их в зависимости от платформы, на которой он работает.
- Playwright — это библиотека автоматизации тестирования с открытым исходным кодом, разработанная Microsoft.
12.Опишите работу автотестировщика и CI/CD. Как она взаимосвязана
Автотесты должны быть встроены в пайплайн. Должен быть выделена отдельный стейдж для автотестов. Если стейдж красный, то деплоя или мёрдж коммита от разрабов нет (в идеале)

Решение:

приложение для теста
https://testpages.herokuapp.com/styled/basic-html-form-test.html