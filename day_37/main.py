import requests
from datetime import datetime
import os

# variables definitions of the pixela API endpoint and the parameters requested
USER_NAME = os.environ["USER_NAME"]
GRAPH_ID = "graph1fran"
pixela_endpoint = "https://pixe.la/v1/users"
pixela_token = os.environ["TOKEN"]
user_params = {
    "token": pixela_token,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# Authentication with token, any post after creating the user requires authentication
graph_headers = {
    "X-USER-TOKEN": pixela_token
}
# variables to create the graph
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "reading_graph",
    "unit": "pages",
    "type": "int",
    "color": "shibafu"
}
# vars to post a pixel
today = datetime.today()
pixel_post_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many pages did you read today? ")
}
# vars to update a pixel
pixel_update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/20211114"
pixel_update_data = {
    "quantity": "21",  # said 32 in the first post
}
# vars to delete a pixel
pixel_delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/20211114"


# run() function sets the main functionality of the program
def run():
    # Create the user, only in the first execution works, once the user is created.
    # pixela_response = requests.post(url=pixela_endpoint, json=user_params)
    # print(pixela_response.text)
    # Create the graph, only run once, do not work after graph is created
    # respose = requests.post(url=graph_endpoint, json=graph_config, headers=graph_headers)
    # print(respose.text)
    # Post a pixel
    response = requests.post(url=pixel_post_endpoint, json=pixel_data, headers=graph_headers)
    print(response.text)
    # update a pixel
    # response = requests.put(url=pixel_update_endpoint, json=pixel_update_data, headers=graph_headers)
    # print(response.text)
    # response = requests.delete(url=pixel_delete_endpoint, headers=graph_headers)
    # print(response.text)


# Entry point, to give the interpreter a place to start executing the code
if __name__ == '__main__':
    run()
