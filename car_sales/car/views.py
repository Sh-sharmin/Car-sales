from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from .models import Car,Comment
from .forms import CommentForm

# Create your views here

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_details.html'
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = self.object
            if request.user.is_authenticated:
                comment.user = request.user
            comment.save()
            return redirect('car_details', pk=self.object.pk)
        return self.render_to_response(self.get_context_data(form=form))