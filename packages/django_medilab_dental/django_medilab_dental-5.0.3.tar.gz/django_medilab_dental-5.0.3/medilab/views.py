from django.shortcuts import render
from shared_lib import utils
from _data import medilab


c = medilab.context


def medilab_home(request):
    return utils.home(request,'medilab/index.html', c)

# 이후의 함수 및 클래스에 컨택스트를 전달하는 이유는 color 변수 때문으로 다른 템플릿에서는 전달할 필요 없다.

def medilab_terms(request):
    return utils.terms(request, 'medilab/pages/terms.html', c)

def medilab_privacy(request):
    return utils.privacy(request, 'medilab/pages/privacy.html', c)


class MedilabBlogDetailView(utils.BlogDetailView):
    template_name = "medilab/pages/blog_details.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(c)
        return context


def fee(request):
    c.update(
        {
            "breadcrumb": {
                "title": "비급여 진료수가 안내",
            },
        }
    )
    return render(request, 'medilab/pages/fee.html', c)


