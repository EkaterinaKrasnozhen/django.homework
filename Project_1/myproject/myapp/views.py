from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

my_name = 'Екатерина Красножен'

start_html = f'<h1>Привет! Меня зовут {my_name}.<h1> \
            <p>Вы находитесь на главной странице моего первого проекта Django.<p>'

about_html = f'<p><ol>Данный проект является учебным и призван закрепить следующие навыки:<p>\
                <li> Ознакомление </li> \
                <li> Изучение </li> \
                <li> Практика </li> \
                <ol> \
                <p>Контакты: gb.ru<p>'


def start(request):
    logger.info('start page accessed')        
    return HttpResponse(start_html)


def about(request):
    logger.info('about page accessed') 
    return HttpResponse(about_html)
