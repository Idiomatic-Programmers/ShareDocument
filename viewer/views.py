from django.shortcuts import render, redirect
from .models import Document


def document_security(request):
    context = {
        'error': False
    }

    if request.method == "POST":
        key = request.POST.get("document_key", None)
        try:
            Document.objects.get(id=key)
            return redirect('viewer_document', key=key)
        except Document.DoesNotExist as e:
            context['error'] = True

    return render(request, "viewer/homepage.html", context=context)


def document_viewer(request, key):
    try:
        document = Document.objects.get(id=key)
    except Document.DoesNotExist as e:
        return redirect('viewer_security')

    context = {
        "document_path": document.document.url,
        "title": document.name
    }

    return render(request, 'viewer/document.html', context=context)
