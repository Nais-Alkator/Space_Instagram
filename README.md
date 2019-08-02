# Space Instagram
Проект предназначен для скачивания картинок на космическую тематику и размещения их в Instagram.
### Как использовать
Для работы скрипта необходим установленный интерпретатор Python3. Затем загрузите зависимости с помощью "pip" (либо "pip3", в случае конфликтов с Python2):  

    pip install -r requirements.txt

Проект основан на использовании:  

1)[SpaceX API](https://documenter.getpostman.com/view/2025350/RWaEzAiG?version=latest#bc65ba60-decf-4289-bb04-4ca9df01b9c1)  
2)[Hubble API](http://hubblesite.org)  
3)[Instagram Bot](https://github.com/instagrambot/instabot)

Также проект разделен на 3 соответствующих скрипта:  

1)fetch_spacex.py, отвечающий за скачивание фотографий с SpaceX API  

2)fetch_hubble.py, предназначенный для скачивание группы(коллекций) фотографий с Hubble API  

3)posting_to_instagram.py, опубликовывающий изображения в Instagram. Скрипт использует параметры окружения INSTAGRAM_LOGIN и INSTAGRAM_PASSWORD. Храните эти чувствительные данные в файле `.env`.  

### Пример использования

Запустите через командную. строку один из вышеуказанных скриптов, исходя из того, что вам необходимо.  

Скрипты fetch_hubble.py и posting_to_instagram используют встроенную библиотеку argparse, поэтому агрументы передаются в командной строке.  

Допустим, вам необходимо скачать коллекцию фотографий "spacecraft" из Hubble API и опубликовать их в своем профиле Instagram. 
Для этого пропишите в командной стоке:

    python fetch_hubble.py spacecraft
    python posting_to_instagram.py directory
  
Без указания конкретной коллекции фотографий, скрипт `fetch_hubble.py` скачает коллекцию по умолчанию - "holiday_cards".  

Второй пример. Необходимо скачать изображения последнего запуска ракет SpaceX и опубликовать их в своем профиле Instagram, загрузив их через свою директорию. 
Для этого пропишите в командной строке:  

    python fetch_spacex.py 
    python posting_to_instagram.py images 

Также, скрипты `fetch_spacex.py` и `fetch_hubble.py` автоматически создают директорию "images", если она не была создана вами ранее. А `posting_to_instagram.py` автоматически загрузит изображения из директории по умолчанию "images", если директория не была передана в качестве аргумента командной строки. 

### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org)
