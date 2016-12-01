# coding:utf-8
from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import HttpResponse,HttpResponseRedirect
from .models import TestUser


class SsoLoginView(View):

    def __init__(self):
        super(SsoLoginView, self).__init__()
        self.username = None
        self.password = None

    def makeTicket(self, request):
        def _md5(str):
            import hashlib
            m = hashlib.md5()
            m.update(str)
            return m.hexdigest()
        return _md5(unicode(request.user))

    def get(self, request, *args, ** kwargs):

        referer = request.GET.get('referer', None)
        context = {}
        context['referer'] = referer
        if referer is not None:
            referer = referer.strip()
        if 'login_id' in request.session:
            if referer is not None:
                return HttpResponseRedirect(referer + '?ticket=' + self.makeTicket(request))
        return render(request, 'login.html', context=context)

    def post(self, request, *args, ** kwargs):

        self.username = request.POST.get('username', None)
        self.password = request.POST.get('password', None)
        referer = request.POST.get('referer', None)

        try:
            user = TestUser.objects.get(username=self.username)

            if self.password == user.password:
                request.session['login_id'] = user.id
                if referer:
                    return HttpResponseRedirect(referer + '?ticket=' + self.makeTicket(request))
                return HttpResponse(content=u'系统已登陆，请访问你前往的系统')
        except:
            return HttpResponse(content=u'无法登陆请检查用户名密码')
        return HttpResponse(content=u'系统已登陆，请访问你前往的系统')


class SsoLogoutView(View):

    def get(self, request, *args, **kwargs):
        try:
            del request.session['login_id']
        except KeyError:
            pass
        return HttpResponse('You are logged out')
