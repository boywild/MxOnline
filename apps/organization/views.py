from django.shortcuts import render
from django.views.generic import View
from apps.organization.models import CourseOrg, City
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

class OrgView(View):
    def get(self, request, *args, **kwargs):
        all_orgs = CourseOrg.objects.all()
        all_citys = City.objects.all()
        org_nums = all_orgs.count()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs, per_page=10, request=request)
        orgs = p.page(page)


        return render(request, 'org-list.html', {
            'all_orgs': orgs,
            'all_citys': all_citys,
            'org_nums': org_nums
        })
