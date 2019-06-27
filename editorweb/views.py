from django.shortcuts import render , redirect, get_object_or_404
from .models import Post, Person
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from tablib import Dataset


@login_required
# Create your views here.
#def home(request):
#    posts = Post.objects.all()
#    return render(request,'home.html',{'posts':posts})
def home(request):
  if request.POST:
      return render(request,'home.html')
  else:
    person = Person.objects.all()
    q = request.GET.get('q', '')
    if q:
        person = person.filter(subject__icontains=q)

    return render(request, 'home.html', {
        'person' : person,
        'q' : q
    })



def new(request):
    return render(request,'new.html')

def create(request):
    
    post = Post()
    post.title = request.POST['post_title']
    post.body = request.POST['post_body']
    post.pub_date = timezone.datetime.now()
    if request.FILES:
      post.image = request.FILES['post_image']
    post.save()

    return redirect('home')



def read(request, post_id):
    post = get_object_or_404(Person, pk=post_id)
    return render(request, 'read.html', {'post' : post})

def renew(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'renew.html',{'post' : post})

def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.title = request.POST["post_title"]
    post.body = request.POST["post_body"]
    post.pub_date = timezone.datetime.now()
    if request.FILES:
      post.image = request.FILES['post_image']
    post.save()
    return redirect('read', post_id=post_id)

def delete(request, post_id):
    if request.POST:
      post = get_object_or_404(Post, pk=post_id)
      post.delete()
      return redirect('home')
    else:
      return redirect('read', post_id=post_id)




def simple_upload(request):
    if request.method == 'GET':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'simple_upload.html')