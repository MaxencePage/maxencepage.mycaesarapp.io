from django.shortcuts import render
from .caesar import caesar_encrypt, caesar_decrypt

def caesar_view(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        key = int(request.POST.get('key'))
        choice = request.POST.get('choice')

        if choice == 'encrypt':
            result = caesar_encrypt(text, key)
        else:
            result = caesar_decrypt(text, key)

        return render(request, 'result.html', {'result': result})

    return render(request, 'index.html')
