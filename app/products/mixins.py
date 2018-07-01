from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, reverse


class AuthRedirectMixin(object):
    """
        *: Desempaquetar Listas
        **: Desempaquetar Diccionarios
    """
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(reverse('users:index'))
        else:
            return super(AuthRedirectMixin, self.get(self, request, *args, **kwargs))


class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
