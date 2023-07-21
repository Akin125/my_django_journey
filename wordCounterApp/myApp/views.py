from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')


def retrieve(request):
    text_input = request.POST['textInput']
    # spliting and counting the texts

    number_of_words = len(text_input.split())

    context = {
        'number': number_of_words
    }

    return render(request, 'retrieve.html', context)
