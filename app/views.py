# coding: utf-8
__author__ = 'Paul Cunningham'
__copyright = 'Copyright 2017, Paul Cunningham'


from datetime import datetime
from flask_mail import Message
from flask import render_template, flash, redirect, url_for, request, jsonify
from flask.views import MethodView


class HomeView(MethodView):

    def get(self):
        return render_template('home.html')


class Example1View(MethodView):

    def get(self):
        return render_template('example1.html', email='test@example.com')

    # Taken from https://blog.miguelgrinberg.com/post/using-celery-with-flask
    def post(self):
        from app.tasks import send_async_email,dummy_task

        email = request.form['email']

        msg = Message('Hello from Flask', recipients=[request.form['email']])
        msg.body = 'This is a test email sent from a background Huey task.'

        if request.form['submit'] == 'Send':
            # send right away
            send_async_email(msg)
            flash('Sending email to {0}'.format(email))
        elif request.form['submit'] == 'dummy':
            dummy_task()
        else:
            # send in one minute
            send_async_email.schedule(args=[msg], delay=60)
            flash('An email will be sent to {0} in one minute'.format(email))

        return redirect(url_for('home'))


    def post2(self):
        from app.tasks import dummy_task
        dummy_task()

        return redirect(url_for('home'))

