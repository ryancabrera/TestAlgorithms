__Author__ = 'Ryan Cabrera'

import requests
import json


def main():
    # Gives info about space station
    response = requests.get(" http://api.open-notify.org/astros.json")
    api_response = response.status_code

    # Not gonna try/except because unwarranted in this situation, thanks for that mentality Golang
    if api_response != 200:
        print("Failed API Request, exiting program")
        exit(1)

    json_response = response.json()
    print(json_response)
    figure_out_this_object = json_print(json_response)
    #print(figure_out_this_object)
    print(figure_out_this_object.index("people"))


def json_print(json_object):
    output = json.dumps(json_object, sort_keys=True, indent=4)
    return output


if __Author__:
    main()