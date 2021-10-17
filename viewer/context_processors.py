from viewer.models import DocumentDiskUsage
from django.db.models import Sum
from hurry.filesize import size, alternative

# Maximum allotted storage to store documents.
MAX_ALLOWED = 20 * (2 ** 30)  # 20 GB in bytes


def total_disk_usage(request):
    usage = DocumentDiskUsage.objects.aggregate(Sum('size'))['size__sum']
    usage = usage if usage else 0
    percent_used = (usage/MAX_ALLOWED) * 100
    context = {
        'usage': size(usage, alternative),
        'percent_used': round(percent_used, 2),
        'num_usage': usage
    }
    return context
