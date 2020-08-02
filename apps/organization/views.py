from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from apps.organization.models import CourseOrg, City
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from apps.organization.forms import AddAskForm


# Create your views here.

class OrgView(View):
    def get(self, request, *args, **kwargs):
        all_orgs = CourseOrg.objects.all()
        all_citys = City.objects.all()
        hot_orgs = all_orgs.order_by('-click_nums')[:3]

        # 按类别筛选机构
        ct_name = request.GET.get('ct', '')
        if ct_name:
            all_orgs = all_orgs.filter(category=ct_name)

        # 按城市筛选机构
        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        # 对机构排序
        sort = request.GET.get('sort', '')
        if sort == 'students':
            all_orgs = all_orgs.order_by('-students')
        elif sort == 'courses':
            all_orgs = all_orgs.order_by('-courses_nums')

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
            'org_nums': org_nums,
            'ct_name': ct_name,
            'city_id': city_id,
            'sort': sort,
            'hot_orgs': hot_orgs
        })


class AddAskView(View):
    def post(self, request, *args, **kwargs):
        userask_form = AddAskForm(request.POST)
        if userask_form.is_valid():
            userask_form.save(commit=True)

            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'fail', 'msg': '添加出错'})
