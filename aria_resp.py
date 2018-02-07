#!/usr/bin/python3

import subprocess
import random
import docker
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
client = docker.from_env() # connect to local docker engine

@app.route("/incoming_sms/<uri>", methods=['POST'])
def incoming_sms(uri):
    "responseds to sms via webhooks"

    body = request.values.get('Body', None) # get sent text
    resp = MessagingResponse() # start response

    # for testing purposes
    #if request.method == 'POST':
    #    body = uri + " web dynamic"

    reply = action(body)
    print(reply)
    resp.message(reply) # convert to twiml
    return str(resp)

# =========LOGIC=========

def action(body):
    """ If action stated then preform respective service else have convo """
    #capture and get rid of prefix
    cmd = body.split()[0]
    package = body.replace(cmd, '')

    if cmd == 'start':
        return start_service(package)
    elif cmd == 'stop':
        return stop_service(package)
    elif cmd == 'status':
        return status_service(package)
    else:
        return convo(body)

def start_service(package):
    """ Set up infrastructure """
    output = subprocess.check_output(["docker-compose", "up", "-d"])
    return "Starting" + package + '!'

def stop_service(package):
    """ Tear down infrastructure """
    output = subprocess.check_output(["docker-compose", "down"])
    return "Stopping" + package + '!'

def status_service(package):
    """ get status of infrastructure """
    status = []
    active_containers = client.containers.list(all)
    for container in active_containers:
        status.append(str(container.name +'...'+ container.status))

    return '\n'.join(status) if len(status) else "No Services Running..."

def convo(sentence):
        """If any of the words in the user's input was a greeting, return a
        greeting response"""

        # Sentences we'll respond with if the user greeted us
        GREETING_KEYWORDS = ["hello", "hi", "greetings", "sup", "what's up",
                             "aria", "hola"]
        GREETING_RESPONSES = ["Hi Anoop!", "hey!", "*nods*", "hey Anoop, you get my snap?"]

        for word in sentence.split():
            if word.lower() in GREETING_KEYWORDS:
                return random.choice(GREETING_RESPONSES)

if __name__ == "__main__":
    app.run(debug=True)
