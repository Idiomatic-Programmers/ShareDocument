from django.contrib.auth.decorators import login_required
from django.shortcuts import render, resolve_url, redirect
from django.http import JsonResponse

from viewer.models import Document, DocumentDiskUsage


@login_required
def add_document(request):
    if request.method == "POST":
        document = request.FILES.get("document")
        title = request.POST.get("document_title")

        doc = Document()
        doc.name = title
        doc.document = document
        doc.uploaded_by = request.user
        doc.save()

        usage = DocumentDiskUsage()
        usage.document = doc
        usage.size = document.size
        usage.save()

        return JsonResponse({
            "share": resolve_url('accounts_share_document', key=doc.id),
        })

    return render(request, 'profile/profile.html')


@login_required
def share_document(request, key):
    document = Document.objects.get(id=key)

    context = {
        'document': document
    }

    return render(request, 'profile/share.html', context=context)


@login_required
def delete_document(request, key):
    document = Document.objects.get(id=key)
    document.delete()

    return redirect('all_documents')


@login_required
def all_documents(request):
    documents = Document.objects.all()

    context = {
        "documents": documents
    }

    return render(request, 'profile/all_documents.html', context=context)
