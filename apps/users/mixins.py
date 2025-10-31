from django.shortcuts import redirect 
from django.urls import reverse_lazy 

class RedirectAuthenticatedUserMixin:
    redirect_url=reverse_lazy('dashboard')

    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect(self.redirect_url)
        return super().dispatch(request, *args, **kwargs)
    