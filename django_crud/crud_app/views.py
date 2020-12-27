from django.shortcuts import render, redirect, get_object_or_404
import uuid
from django.forms import ModelForm

from .models import Project

# error code
ERRC = {"ERRC_0": "ERRC_0",
        "ERRC_1": "ERRC_1"
        }

# error name
ERRN = {
    "ERRC_0": "ERRC_0",
    "ERRC_1": "ERRC_1"
}

# error description
ERRCD = {"ERRC_0": "description of err_p_0",
         "ERRC_1": "description of err_p_1"
         }


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'storeUrl', 'description']


def error_404(request, template_name='error_pages/404.html'):
    session_id = request.GET.get('sid', '')
    if session_id == '':
        session_id = uuid.uuid4().hex
        return redirect('/?sid=' + session_id)
    return render(request, template_name, {'session_id': session_id})


def error_400(request, template_name='error_pages/400.html'):
    session_id = request.GET.get('sid', '')
    if session_id == '':
        session_id = uuid.uuid4().hex
        return redirect('/?sid=' + session_id)
    return render(request, template_name, {'session_id': session_id})


def error_403(request, template_name='error_pages/403.html'):
    session_id = request.GET.get('sid', '')
    if session_id == '':
        session_id = uuid.uuid4().hex
        return redirect('/?sid=' + session_id)
    return render(request, template_name, {'session_id': session_id})


def error_500(request, template_name='error_pages/500.html'):
    session_id = request.GET.get('sid', '')
    if session_id == '':
        session_id = uuid.uuid4().hex
        return redirect('/?sid=' + session_id)
    return render(request, template_name, {'session_id': session_id})


def main_page(request, template_name='pages/main.html'):
    session_id = request.GET.get('sid', '')
    if session_id == '':
        session_id = uuid.uuid4().hex
        return redirect('/?sid=' + session_id)
    return render(request, template_name, {'session_id': session_id})


def new_project(request, template_name='pages/main.html'):
    session_id = request.GET.get('sid', '')
    if session_id == '':
        session_id = uuid.uuid4().hex
        return redirect('/new?sid=' + session_id)
    return render(request, template_name, {'session_id': session_id})


def display_project(request, template_name='pages/main.html'):
    session_id = request.GET.get('sid', '')
    if session_id == '':
        session_id = uuid.uuid4().hex
        return redirect('/project?sid=' + session_id)
    return render(request, template_name, {'session_id': session_id})


def create(request, template_name='pages/create.html'):
    session_id = request.GET.get('sid', '')
    if session_id == '':
        session_id = uuid.uuid4().hex
        return redirect('/create?sid=' + session_id)
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        project_id = uuid.uuid4().hex
        project = form.save(commit=False)
        # project.user = request.user
        project.sid = session_id
        project.pid = project_id
        project.spid = session_id + '_' + project_id
        # project.name = request.name
        # project.description = request.description
        project.save()
        return redirect('/create?sid=' + session_id)
    # return render(request, template_name, {'form': form})
    return render(request, template_name, {'session_id': session_id, 'form': form})


def read(request, template_name='pages/read.html'):
    session_id = request.GET.get('sid', '')
    project_id = request.GET.get('pid', '')
    session_project_id = request.GET.get('spid', '')

    if session_id != '':
        # project = get_object_or_404(Project, spid=session_project_id)
        project = Project.objects.filter(sid=session_id)
    else:
        return redirect('/?sid=' + session_id)
    data = {}
    data['object_list'] = project
    data['session_id'] = session_id
    return render(request, template_name, data)


def update(request, template_name='pages/update.html'):
    session_id = request.GET.get('sid', '')
    project_id = request.GET.get('pid', '')
    session_project_id = request.GET.get('spid', '')

    if session_project_id != '':
        # project = get_object_or_404(Project, spid=session_project_id)
        project = Project.objects.get(spid=session_project_id)  # get_object_or_404(Project, spid=session_project_id)
    elif session_id != '' and project_id != '':
        spid = session_id + '_' + project_id
        project = get_object_or_404(Project, spid=session_project_id)
    else:
        return redirect('/err/?sid=' + session_id + '&errc=' + ERRC['ERRC_0'])
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect('/read?sid=' + session_id)
    return render(request, template_name, {'session_id': session_id, 'form': form})


def delete(request, template_name='pages/delete.html'):
    session_id = request.GET.get('sid', '')
    project_id = request.GET.get('pid', '')
    session_project_id = request.GET.get('spid', '')

    if session_project_id != '':
        # project = get_object_or_404(Project, spid=session_project_id)
        project = Project.objects.get(spid=session_project_id)  # get_object_or_404(Project, spid=session_project_id)
    elif session_id != '' and project_id != '':
        spid = session_id + '_' + project_id
        project = get_object_or_404(Project, spid=session_project_id)
    else:
        return redirect('/err/?sid=' + session_id + '&errc=' + ERRC['ERRC_1'])

    if request.method == 'POST':
        project.delete()
        return redirect('/?sid=' + session_id)  # redirect to a page that says deleted successfully

    return render(request, template_name, {'session_id': session_id, 'object': project})


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


def err(request, template_name='pages/custom_error.html'):
    session_id = request.GET.get('sid', '')
    error_code = request.GET.get('errc', '')
    if session_id == '':
        session_id = uuid.uuid4().hex
        return redirect('/err?sid=' + session_id)
    error_text = ERRCD.get(error_code, "Unknown error")
    error_code = ERRN.get(error_code, "Unknown error code")
    return render(request, template_name, {'session_id': session_id, 'error_text': error_text, 'error_code': error_code})
