from django.shortcuts import render, redirect
from .forms import ParticipantForm
from .models import People


# Create your views here.
def landing(request):
    form = ParticipantForm()
    return render(request, "landing.html")


def Create(request):
    form = ParticipantForm()
    if request.POST:
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Succesfully Added"
            ppl = People.objects.all()
            return redirect("/allitems/")
    return render(request, "create.html", {"form": form})


def AllItems(request):
    ppl = People.objects.all().order_by("age")
    pending = People.objects.filter(status="Pending")
    completed_count = len(People.objects.filter(status="Finished"))
    total_count = len(ppl)
    count_of_pending = len(pending)
    datas = {
        "ppl": ppl,
        "pending": count_of_pending,
        "total_count": total_count,
        "completed_count": completed_count,
    }

    return render(request, "allitems.html", datas)


def Details(request, id):
    ppl = People.objects.get(id=id)
    return render(request, "details.html", {"ppl": ppl})


def Edit(request, id):
    ppl = People.objects.get(id=id)
    form = ParticipantForm(instance=ppl)
    if request.POST:
        form = ParticipantForm(request.POST, instance=ppl)
        if form.is_valid():
            form.save()
            return redirect(f"/allitems/{ppl.id}")
    return render(request, "edit.html", {"form": form})


def Delete(request, id):
    ppl = People.objects.get(id=id)
    ppl.delete()
    return redirect("/allitems/")


def SingleItems(request):
    ppl = People.objects.filter(category="Single")
    pending = People.objects.filter(status="Pending", category="Single")
    completed_count = len(People.objects.filter(status="Finished", category="Single"))
    total_count = len(ppl)
    count_of_pending = len(pending)
    datas = {
        "ppl": ppl,
        "pending": count_of_pending,
        "total_count": total_count,
        "completed_count": completed_count,
    }

    return render(request, "single_items.html", datas)


def GroupItems(request):
    ppl = People.objects.filter(category="Group")
    pending = People.objects.filter(status="Pending", category="Group")
    completed_count = len(People.objects.filter(status="Finished", category="Group"))
    total_count = len(ppl)
    count_of_pending = len(pending)
    datas = {
        "ppl": ppl,
        "pending": count_of_pending,
        "total_count": total_count,
        "completed_count": completed_count,
    }
    return render(request, "group_items.html", datas)


def Completed(request):
    ppl = People.objects.filter(status="Finished")
    return render(request, "completed.html", {"ppl": ppl})


def Remaining(request):
    ppl = People.objects.exclude(status="Finished")
    return render(request, "remaining.html", {"ppl": ppl})
