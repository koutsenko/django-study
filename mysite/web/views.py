from datetime import datetime
from django.shortcuts import render, redirect


publications_data = {
    0: {
        'id': 0,
        'title': 'About lorem ipsum (RU)',
        'date': datetime.now(),
        'text': 'Многие думают, что Lorem Ipsum - взятый с потолка псевдо-латинский набор слов, но это не совсем так. '
                'Его корни уходят в один фрагмент классической латыни 45 года н.э., то есть более двух тысячелетий '
                'назад. Ричард МакКлинток, профессор латыни из колледжа Hampden-Sydney, штат Вирджиния, взял одно из '
                'самых странных слов в Lorem Ipsum, "consectetur", и занялся его поисками в классической латинской '
                'литературе. В результате он нашёл неоспоримый первоисточник Lorem Ipsum в разделах 1.10.32 и 1.10.33 '
                'книги "de Finibus Bonorum et Malorum" ("О пределах добра и зла"), написанной Цицероном в 45 году '
                'н.э. Этот трактат по теории этики был очень популярен в эпоху Возрождения. Первая строка Lorem '
                'Ipsum, "Lorem ipsum dolor sit amet..", происходит от одной из строк в разделе 1.10.32 '
    },
    1: {
        'id': 1,
        'title': 'Classic lorem (RU)',
        'date': datetime.now(),
        'text': 'Классический текст Lorem Ipsum, используемый с XVI века, приведён ниже. Также даны разделы 1.10.32 и '
                '1.10.33 "de Finibus Bonorum et Malorum" Цицерона и их английский перевод, сделанный H. Rackham, '
                '1914 год. '
    }
}


def hello(request):
    return render(request, 'main.html')


def contacts(request):
    return render(request, 'contacts.html')


def publication(request, pub_id):
    if pub_id not in publications_data.keys():
        return redirect('/')
    else:
        return render(request, 'publication.html', publications_data[pub_id])


def publications(request):
    pubs = publications_data.values()
    pubs_sorted = sorted(pubs, key=lambda pub: pub['date'], reverse=True)

    return render(request, 'publications.html', {
        'publications': pubs_sorted
    })
