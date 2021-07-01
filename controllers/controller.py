from flask import render_template, request, redirect
from app import app
from models.events_list import events, add_new_event
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/events', methods=['POST'])
def add_event():
    event_name = request.form['name_of_event']
    event_description = request.form['description']
    event_date = request.form['date']
    event_location = request.form['location']
    event_number_of_guests = request.form['number_of_guests']
    new_event = Event(event_name, event_date, event_location, event_number_of_guests, event_description)
    add_new_event(new_event)
    return redirect('/events')

     
