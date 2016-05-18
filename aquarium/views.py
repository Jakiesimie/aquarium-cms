from django.shortcuts import render, get_object_or_404, redirect

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.core.urlresolvers import reverse

from models import Map, Tank, Habitat, Species, Trivia
from quiz.models import Quiz, Grade, Image

from forms import MapForm, TankForm, HabitatForm, TriviaForm, SpeciesForm
from quiz.forms import QuizForm, QuizTextForm, QuizImageForm, QuizTableForm, ImageForm


get_abs_url = lambda name, key, value: reverse(name, kwargs={key: value})

########################################
#### Map
########################################

@login_required
def map_list(request):
    queryset = Map.objects.all().order_by('id')
    context = {
        'title': 'Maps',
        'queryset': queryset,
    }
    return render(request, 'aquarium/map_list.html', context)

@login_required
def map_create(request):
    form = MapForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created")
        return redirect('mlist')

    context = {
        'form': form,
    }
    return render(request, 'aquarium/generic_form.html', context)

@login_required
def map_update(request, id=None):
    instance = get_object_or_404(Map, id=id)

    form = MapForm(request.POST or None, request.FILES or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Updated")
        return redirect('mlist')

    context = {
        'form': form,
    }
    return render(request, 'aquarium/generic_form.html', context)

@login_required
def map_delete(request, id=None):
    instance = get_object_or_404(Map, id=id)
    instance.delete()
    messages.success(request, 'Successfully Deleted')
    return redirect('mlist')

########################################
#### Tank
########################################

@login_required
def tank_list(request):
    queryset = Tank.objects.all().order_by('tank_id')
    context = {
        'title': 'Tanks',
        'queryset': queryset,
    }
    return render(request, 'aquarium/tank_list.html', context)

@login_required
def tank_quiz_detail(request, tank_id=None):
    instance = get_object_or_404(Tank, tank_id=tank_id)
    quizes = Quiz.objects.filter(tank=tank_id).order_by('position')
    grades = Grade.objects.all()
    context = {
        'title': instance.name_eng,
        'instance': instance,
        'quizes': quizes,
        'grades': grades,
    }
    return render(request, 'aquarium/tank_detail_quiz.html', context)

@login_required
def tank_species_detail(request, tank_id=None):
    instance = get_object_or_404(Tank, tank_id=tank_id)
    species_all = Species.objects.filter(tank=tank_id).order_by('id')
    context = {
        'title': instance.name_eng,
        'instance': instance,
        'species_all': species_all,
    }
    return render(request, 'aquarium/tank_detail_species.html', context)

@login_required
def tank_create(request):
    form = TankForm(request.POST or None) #, request.FILES or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created")
        return redirect(get_abs_url('tdetail', 'tank_id', instance.tank_id))

    context = {
        'form': form,
    }
    return render(request, 'aquarium/generic_form.html', context)

@login_required
def tank_update(request, tank_id=None):
    instance = get_object_or_404(Tank, tank_id=tank_id)

    form = TankForm(request.POST or None, instance=instance)

    # If Tank's tank_id was changed, every item connected to that tank
    # must also have updated value ot the 'tank' field.
    quizes = Quiz.objects.filter(tank__tank_id=tank_id)
    species_all = Species.objects.filter(tank__tank_id=tank_id)
    tank_items = [quizes, species_all]

    if form.is_valid():
        instance = form.save(commit=False)

        # Because of the ForeignKey constraints, in case of edited tank_id,
        # to which quizitems and species are connected, I have to first create
        # a new tank intance (with tank_id value taken from instance object),
        # and finaly I can transfer all items connected to the original tank object.
        if int(tank_id) != instance.tank_id:
            Tank.objects.create(
                tank_id=instance.tank_id,
                name_eng=instance.name_eng,
                name_arabic=instance.name_arabic,
                habitat=instance.habitat,
                direction_label_eng=instance.direction_label_eng,
                direction_label_arabic=instance.direction_label_arabic,
                direction=instance.direction,
            )

            # Iterate through every type of item connected to original tank by ForeignKey,
            # then through every record in items, changing 'tank_id' value (pointing to specific tank),
            # and finaly saves changes to the database.
            for item in tank_items:
                for index in xrange(len(item)):
                    item[index].tank_id = instance.tank_id
                    item[index].save()

            # Finally, when every item was transferred to the copied tank object
            # original one must be deleted (or killed - just like in the thought experiment
            # on teleportation also called 'Teleportation Paradox').
            Tank.objects.get(tank_id=tank_id).delete()
        else:
            instance.save()

        messages.success(request, "Successfully Updated")
        return redirect(get_abs_url('tdetail', 'tank_id', instance.tank_id))

    context = {
        'form': form,
    }
    return render(request, 'aquarium/generic_form.html', context)

@login_required
def tank_delete_safe(request, tank_id=None):
    instance = get_object_or_404(Tank, tank_id=tank_id)
    quizes = Quiz.objects.filter(tank_id=tank_id)
    context = {
        'instance': instance,
        'quizes': quizes,
    }
    return render(request, 'aquarium/tank_delete.html', context)

@login_required
def tank_delete(request, tank_id=None):
    quizes = Quiz.objects.filter(tank_id=tank_id)
    species_all = Species.objects.filter(tank_id=tank_id)
    quizes.delete()
    species_all.delete()
    instance = get_object_or_404(Tank, tank_id=tank_id)
    instance.delete()
    messages.success(request, 'Successfully Deleted')
    return redirect('tlist')

@login_required
def tank_custom_quiz_create(request, tank_id=None, arg=None):
    form = {
        'text': QuizTextForm,
        'image': QuizImageForm,
        'image_table': QuizTableForm,
    }[arg](request.POST or None, request.FILES or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.tank_id = tank_id
        instance.type = arg
        instance.save()
        messages.success(request, "Successfully Created")
        return redirect(get_abs_url('tdetail', 'tank_id', tank_id))

    context = {
        'form': form,
        # 'name': arg
    }
    return render(request, 'aquarium/generic_form.html', context)

@login_required
def tank_custom_quiz_update(request, tank_id=None, id=None, arg=None):
    instance = get_object_or_404(Quiz, id=id)

    form = {
        'text': QuizTextForm,
        'image': QuizImageForm,
        'image_table': QuizTableForm,
    }[arg](request.POST or None, request.FILES or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.tank_id = tank_id
        instance.type = arg
        instance.save()
        messages.success(request, "Successfully Created")
        return redirect(get_abs_url('tdetail', 'tank_id', tank_id))

    context = {
        'form': form,
        # 'name': arg
    }
    return render(request, 'aquarium/generic_form.html', context)

@login_required
def tank_quiz_delete(request, tank_id=None, id=None):
    instance = get_object_or_404(Quiz, id=id)
    Image.objects.filter(quiz__id=id).delete()
    instance.delete()
    messages.success(request, 'Successfully Deleted')
    return redirect(get_abs_url('tdetail', 'tank_id', tank_id))

@login_required
def tank_quizimage_create(request, tank_id=None, id=None):
    form = ImageForm(request.POST or None, request.FILES or None)
    quiz = Quiz.objects.get(id=id)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        quiz.images.add(instance)
        messages.success(request, 'Successfully Created')
        return redirect(get_abs_url('tdetail', 'tank_id', tank_id))

    context = {
        'form': form,
    }
    return render(request, 'aquarium/generic_form.html', context)

@login_required
def tank_quizimage_update(request, tank_id=None, id=None):
    instance = get_object_or_404(Image, id=id)

    form = ImageForm(request.POST or None, request.FILES or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Successfully Updated')
        return redirect(get_abs_url('tdetail', 'tank_id', tank_id))

    context = {
        'form': form,
    }
    return render(request, 'aquarium/generic_form.html', context)

@login_required
def tank_quizimage_delete(request, tank_id=None, id=None):
    instance = get_object_or_404(Image, id=id)
    instance.delete()
    messages.success(request, 'Successfully Deleted')
    return redirect(get_abs_url('tdetail', 'tank_id', tank_id))

@login_required
def tank_species_create(request, tank_id=None):
    form = SpeciesForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.tank_id = tank_id
        instance.save()
        messages.success(request, 'Successfully Created')
        return redirect(get_abs_url('tdetail_s', 'tank_id', tank_id))

    context = {
        'form': form,
    }
    return render(request, 'aquarium/generic_form.html', context)

@login_required
def tank_species_update(request, tank_id=None, id=None):
    instance = get_object_or_404(Species, id=id)

    form = SpeciesForm(request.POST or None, request.FILES or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Successfully Updated')
        return redirect(get_abs_url('tdetail_s', 'tank_id', tank_id))

    context = {
        'form': form,
    }
    return render(request, 'aquarium/generic_form.html', context)

@login_required
def tank_species_delete(request, tank_id=None, id=None):
    instance = get_object_or_404(Species, id=id)
    instance.delete()
    messages.success(request, 'Successfully Deleted')
    return redirect(get_abs_url('tdetail_s', 'tank_id', tank_id))

########################################
#### Habitat
########################################

@login_required
def habitat_list(request):
    queryset = Habitat.objects.all().order_by('id')
    context = {
        'title': 'Habitats',
        'queryset': queryset,
    }
    return render(request, 'aquarium/habitat_list.html', context)

@login_required
def habitat_detail(request, id=None):
    instance = get_object_or_404(Habitat, id=id)
    tanks = Tank.objects.filter(habitat=id)
    context = {
        'title': instance.name_eng,
        'instance': instance,
        'tanks': tanks,
    }
    return render(request, 'aquarium/habitat_detail.html', context)

@login_required
def habitat_create(request):
    form = HabitatForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created")
        # return redirect('hlist')
        return redirect(get_abs_url('hdetail', 'id', instance.id))

    context = {
        'form': form,
    }
    return render(request, 'aquarium/generic_form.html', context)

@login_required
def habitat_update(request, id=None):
    instance = get_object_or_404(Habitat, id=id)

    form = HabitatForm(request.POST or None, request.FILES or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Updated")
        return redirect(get_abs_url('hdetail', 'id', id))

    context = {
        'form': form,
    }
    return render(request, 'aquarium/generic_form.html', context)

@login_required
def habitat_delete_safe(request, id=None):
    instance = get_object_or_404(Habitat, id=id)
    context = {
        'instance': instance,
    }
    return render(request, 'aquarium/habitat_delete.html', context)

@login_required
def habitat_delete(request, id=None):
    instance = get_object_or_404(Habitat, id=id)

    tanks = Tank.objects.filter(habitat__id=id)
    trivias = Trivia.objects.filter(habitat__id=id)

    for tank in tanks:
        print tank.tank_id
        print Species.objects.filter(tank__tank_id=tank.tank_id)
        # print Quiz.objects.filter(tank__tank_id=tank.tank_id)
        print 'Quizes', len(Quiz.objects.filter(tank__tank_id=tank.tank_id))
        print 'Species', len(Species.objects.filter(tank__tank_id=tank.tank_id))

    print tanks
    messages.success(request, 'Successfully Deleted')
    return redirect('hlist')

########################################
#### Trivia
########################################

@login_required
def trivia_create(request, id=None):
    form = TriviaForm(request.POST or None)
    habitat = Habitat.objects.get(id=id)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        habitat.trivia.add(instance)
        messages.success(request, "Successfully Created")
        return redirect(get_abs_url('hdetail', 'id', id))

    context = {
        'form': form,
    }
    return render(request, 'aquarium/generic_form.html', context)

@login_required
def trivia_update(request, id=None, trid=None):
    instance = get_object_or_404(Trivia, id=trid)

    form = TriviaForm(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save()
        messages.success(request, 'Successfully Updated')
        return redirect(get_abs_url('hdetail', 'id', id))

    context = {
        'form': form,
    }
    return render(request, 'aquarium/generic_form.html', context)

@login_required
def trivia_delete(request, hid=None, id=None):
    instance = get_object_or_404(Trivia, id=id)
    instance.delete()
    messages.success(request, 'Successfully Deleted')
    return redirect(get_abs_url('hdetail', 'id', hid))

