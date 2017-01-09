from django.shortcuts import render
from django.views import generic
from .forms import RecignitionImageForm
from .models import RecognitionImage
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, get_list_or_404

from recognition.what_leaf_is import label_image

class IndexView(generic.FormView):
    template_name = 'recognition/index.html'
    form_class = RecignitionImageForm

    def form_valid(self, form):
        recognition_image = RecognitionImage(
            image = self.get_form_kwargs().get('files')['image'])
        recognition_image.save()
        self.id = recognition_image.id
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        #return reverse('recognition:recognition_image_upload', kwargs={'image_pk': self.id})
        return reverse('recognition:recognition_image_upload', kwargs={'id': self.id})

class ImageDetailView(generic.DetailView):
    model = RecognitionImage
    template_name = 'recognition/recognition_image.html'
    context_object_name = 'some_image'
    s = RecognitionImage.objects.all()
    #instance = get_list_or_404(RecognitionImage)
    something = "asfdf"
    #pk_url_kwarg = RecognitionImage.pk
    #query_pk_and_slug = RecognitionImage.pk
    #def get_queryset(self):
     #   return RecognitionImage.objects.all()
    #def get_object(self, queryset=None):
     #   return RecognitionImage.objects.filter(pk=self.kwargs.get("image_pk"))
    def get_object(self, queryset=None):
        return RecognitionImage.objects.all()

def img_detail(request, id=None):
    instance = get_object_or_404(RecognitionImage, id = id)
    result =  label_image.recognition(instance.image.path)#label_image.test(instance.image.url)#label_image.recognition(instance.image.url)
    context = {
        'image': instance.image,
        'instance' : instance,
        'result' : result,
        'first_label': result[0],
        'first_score': result[1],
        'second_label': result[2],
        'second_score': result[3],
    }
    return render(request, "recognition/recognition_image.html", context)
