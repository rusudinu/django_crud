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
    session_id = request.GET.get('sid', '')
    if session_id == '':
        session_id = uuid.uuid4().hex
        return redirect('/new?sid=' + session_id)
    return render(request, template_name, {'session_id': session_id})


def display_project(request, template_name='pages/main_page.html'):
    session_id = request.GET.get('sid', '')
    if session_id == '':
        session_id = uuid.uuid4().hex
        return redirect('/project?sid=' + session_id)
    return render(request, template_name, {'session_id': session_id})


def delete_project(request, template_name='pages/main_page.html'):
    session_id = request.GET.get('sid', '')
    if session_id == '':
        session_id = uuid.uuid4().hex
        return redirect('/delete?sid=' + session_id)
    return render(request, template_name, {'session_id': session_id})


def update_project(request, template_name='pages/main_page.html'):
    session_id = request.GET.get('sid', '')
    if session_id == '':
        session_id = uuid.uuid4().hex
        return redirect('/update?sid=' + session_id)
    return render(request, template_name, {'session_id': session_id})


def work(request, template_name='pages/work.html'):
    session_id = request.GET.get('sid', '')
    if session_id == '':
        session_id = uuid.uuid4().hex
        return redirect('/work?sid=' + session_id)
    return render(request, template_name, {'session_id': session_id})


def mobile(request, template_name='pages/mobile.html'):
    session_id = request.GET.get('sid', '')
    if session_id == '':
        session_id = uuid.uuid4().hex
        return redirect('/mobile?sid=' + session_id)
    return render(request, template_name, {'session_id': session_id})


def web(request, template_name='pages/web.html'):
    session_id = request.GET.get('sid', '')
    if session_id == '':
        session_id = uuid.uuid4().hex
        return redirect('/web?sid=' + session_id)
    return render(request, template_name, {'session_id': session_id})


def awards(request, template_name='pages/awards.html'):
    session_id = request.GET.get('sid', '')
    if session_id == '':
        session_id = uuid.uuid4().hex
        return redirect('/awards?sid=' + session_id)
    return render(request, template_name, {'session_id': session_id})


def about(request, template_name='pages/about.html'):
    session_id = request.GET.get('sid', '')
    if session_id == '':
        session_id = uuid.uuid4().hex
        return redirect('/about?sid=' + session_id)
    return render(request, template_name, {'session_id': session_id})


def contact(request, template_name='pages/contact.html'):
    session_id = request.GET.get('sid', '')
    if session_id == '':
        session_id = uuid.uuid4().hex
        return redirect('/contact?sid=' + session_id)
    return render(request, template_name, {'session_id': session_id})
