import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
_PATH = os.path.abspath(os.path.dirname(__file__))

print('Template_DIR :', os.path.join(BASE_DIR, 'templates'))
print('Base_DIR :', BASE_DIR)
print('Project_DIR :', PROJECT_DIR)
print('_Path :', _PATH)
print('Static_ROOT :', os.path.join(_PATH, 'files', 'static'))