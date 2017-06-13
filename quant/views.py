import os
import re

from flask import current_app as app, render_template, request, redirect, abort, jsonify, url_for, session, Response, send_file, send_from_directory
from jinja2.exceptions import TemplateNotFound


@views.route('/', methods = ['GET', 'POST'])



@views.route('/loans')



@views.route('/homeloans', methods=['GET', 'POST'])
def homeloan_query():
    db = get_db()
    # cur =db.execute('select * from homeloan where usertenure> tenureLowerLimit and usertenure < tenureUpperLimit and userage >= ageLowerLimit and userage <= ageUpperLimit', [request.form['usertenure'], request.form['userage'], request.form['usercategory']]) 



@views.route('/propertyloans')

 
