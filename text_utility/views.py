from django.shortcuts import render


def index(request):
    return render(request, template_name='index.html')


def analyze(request):
    text = request.POST.get('text', '')

    remove_punctuations_check = request.POST.get('remove_punctuations', 'off')
    capitalize_first_check = request.POST.get('capitalize_first', 'off')
    remove_spaces_check = request.POST.get('remove_spaces', 'off')

    if remove_punctuations_check == 'on':
        text = __remove_punctuations(text)
    if capitalize_first_check == 'on':
        text = __capitalize_first(text)
    if remove_spaces_check == 'on':
        text = __remove_spaces(text)

    params = {
        'analyzed_text': text
    }

    return render(request, template_name='analyze.html', context=params)


def __capitalize_first(text):
    split = text.split()
    output = ''

    for i in range(len(split)):
        split[i] = split[i][0].capitalize() + split[i][1:]
        output = output + split[i] + ' '

    return output.strip()


def __remove_punctuations(text):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    output = ''
    for char in text:
        if char not in punctuations:
            output = output + char

    return output


def __remove_spaces(text):
    return text.replace(" ", "")
