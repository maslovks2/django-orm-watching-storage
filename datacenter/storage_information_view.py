from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from pytz import timezone


def storage_information_view(request):
    non_closed_visits = []
    for visit in Visit.objects.filter(leaved_at__isnull=True):
        duration_in_seconds = visit.get_duration().total_seconds()
        non_closed_visits.append(
            {
                "who_entered": visit.passcard.owner_name,
                "entered_at": localtime(visit.entered_at, timezone=timezone('Europe/Moscow')),
                "duration": Visit.format_duration(duration_in_seconds)
            }
        )

    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
