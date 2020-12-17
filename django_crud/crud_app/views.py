from django.shortcuts import render, redirect, get_object_or_404
import uuid
from django.forms import ModelForm


def error_404(request, template_name='error_pages/404.html'):
    return render(request, template_name)


def error_400(request, template_name='error_pages/400.html'):
    return render(request, template_name)


def error_403(request, template_name='error_pages/403.html'):
    return render(request, template_name)


def error_500(request, template_name='error_pages/500.html'):
    return render(request, template_name)


def main_page(request, template_name='pages/main_page.html'):
    session_id = request.GET.get('sid', '')
    if session_id == '':
        session_id = uuid.uuid4().hex
        return redirect('/?sid=' + session_id)
    return render(request, template_name, {'session_id': session_id})


def new_project(request, template_name='pages/main_page.html'):
    return render(request, template_name)


def display_project(request, template_name='pages/main_page.html'):
    return render(request, template_name)


def delete_project(request, template_name='pages/main_page.html'):
    return render(request, template_name)


def update_project(request, template_name='pages/main_page.html'):
    return render(request, template_name)


def work(request, template_name='pages/work.html'):
    return render(request, template_name)


def mobile(request, template_name='pages/mobile.html'):
    return render(request, template_name)


def web(request, template_name='pages/web.html'):
    return render(request, template_name)


def awards(request, template_name='pages/awards.html'):
    return render(request, template_name)


def about(request, template_name='pages/about.html'):
    return render(request, template_name)


def contact(request, template_name='pages/contact.html'):
    return render(request, template_name)
