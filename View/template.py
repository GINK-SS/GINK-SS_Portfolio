from flask import Blueprint, render_template
from templates import *

BP = Blueprint('template', __name__)

# 메인 페이지
@BP.route('/')
def main_page():
    return render_template('main.html')