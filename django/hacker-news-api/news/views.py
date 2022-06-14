from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.db.models import Q

from .forms import NewsSearchForm

from .models import News, Comment


class Index(TemplateView):
    model = News
    template_name = 'list_item.html'

    def get_context_data(self, **kwargs):
        # print(News.objects.all())
        context = super().get_context_data(**kwargs)
        page_size = 100
        paginator = Paginator(News.objects.order_by('-time'), page_size)
        page = self.request.GET.get('page', 1)
        page_obj = paginator.page(page)

        context['news'] = page_obj
        context['form'] = NewsSearchForm(self.request.POST or None)
        return context

    def get_queryset(self):
        return self.model.objects.all()

    def post(self, request, *args, **kwargs):
        form = NewsSearchForm(request.POST)
        if form.is_valid():
            print("Valid form")
            data = form.cleaned_data
            print(data)

            queryset = News.objects.filter(Q(author__icontains=data['name']) | Q(story_type__icontains=data['name']) | Q(title__icontains=data['name']))
            print(queryset)

            context = {
                "form": form,
                "news": queryset,
            }
            return render(request, "list_item.html", context)
        return redirect("news:index")


def story_detail(request, id, slug):
    story = get_object_or_404(News, id=id, slug=slug)
    comments_by_parent_id = News.objects.filter(unique_api_story_id=story.parent_id)
    comments_normally = Comment.objects.select_related("story").filter(story=story)
    from itertools import chain

    story_comments = list(chain(comments_by_parent_id, comments_normally))
    context = {
        "page_title": f"{story.title}",
        "story": story,
        "story_comments": story_comments,
    }
    return render(request, "news_detail.html", context)
