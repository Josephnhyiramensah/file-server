from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from django.http import FileResponse
from .models import Document
from .forms import DocumentForm

@login_required
def document_list(request):
    query = request.GET.get('q')
    if query:
        documents = Document.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    else:
        documents = Document.objects.all()
    
    if request.method == 'POST':
        if 'email' in request.POST:
            # Handle email sending
            document_id = request.POST.get('document_id')
            document = Document.objects.get(id=document_id)
            recipient_email = request.POST['email']
            send_mail(
                'Document from File Server',
                f'Please find the document "{document.title}" attached.',
                settings.EMAIL_HOST_USER,
                [recipient_email],
                fail_silently=False,
            )
            document.emails_sent += 1
            document.save()
        else:
            # Handle document upload
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                document = form.save(commit=False)
                document.uploaded_by = request.user
                document.save()
                return redirect('document_list')
    else:
        form = DocumentForm()
    
    return render(request, 'documents/document_manage.html', {
        'documents': documents,
        'form': form
    })

@login_required
def download_document(request, document_id):
    document = Document.objects.get(id=document_id)
    document.downloads += 1
    document.save()
    return FileResponse(request, document.file)
