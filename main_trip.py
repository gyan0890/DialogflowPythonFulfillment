# -*- coding:utf8 -*-
# !/usr/bin/env python
# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This is a sample for a weather fulfillment webhook for an Dialogflow agent
This is meant to be used with the sample weather agent for Dialogflow, located at
https://console.dialogflow.com/api-client/#/agent//prebuiltAgents/Weather

This sample uses the WWO Weather Forecast API and requires an WWO API key
Get a WWO API key here: https://developer.worldweatheronline.com/api/
"""

import json

from flask import Flask, request, make_response, jsonify


app = Flask(__name__)
log = app.logger

@app.route('/webhooksample', methods=['POST'])
def webhooksample():
    """This method handles the http requests for the Dialogflow webhook

    This is meant to be used in conjunction with the weather Dialogflow agent
    """
    req = request.get_json(silent=True, force=True)
    try:
        action = req.get('queryResult').get('action')
        parameters = req.get('queryResult').get('parameters')
        print(parameters)
    except AttributeError:
        return 'json error'
    if action == 'input.flightBooking':
        res = "Hey there! This is a response from the webhook!Your flight is booked successfully for!"

    print('Action: ' + action)
    print('Response: ' + res)

    return make_response(jsonify({'fulfillmentText': res}))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')