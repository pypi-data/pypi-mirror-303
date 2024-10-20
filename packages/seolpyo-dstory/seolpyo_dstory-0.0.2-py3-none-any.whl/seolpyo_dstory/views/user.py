from django.contrib.auth.views import LoginView as LiV, LogoutView


class LoginView(LiV):
    template_name = 'seolpyo_dstory/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': '로그인',
        })
        del context['site_name']

        return context


