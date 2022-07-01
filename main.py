import PySimpleGUI as sg
import ASc_Smart_Human_Interface as sensing

a = sensing.sensing_remote()

#import os
#from pprint import pprint
#from google.cloud import storage

#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceKey_GoogleCloud.json'

#storage_client = storage.Client()

#bucket_name = '<bucket name>'

#bucket.name
#bucket._properties['selfLink']
#bucket._properties['id']
#bucket._properties['location']
#bucket._properties['timeCreated']
#bucket._properties['storageClass']
#bucket._properties['timeCreated']
#bucket._properties['updated']

"""
Get Bucket
"""
#my_bucket = storage_client.get_bucket(bucket_name)
#pprint(vars(my_bucket))

"""
Upload File
"""
#def upload_to_bucket(blob_name, file_path, bucket_name):
#    '''
#    Upload file to a bucket
#    : blob_name  (str) - object name
#    : file_path (str)
#    : bucket_name (str)
#    '''
#    bucket = storage_client.get_bucket(bucket_name)
#    blob = bucket.blob(blob_name)
#    blob.upload_from_filename(file_path)
#    return blob


sg.theme('DarkAmber')   # Add a little color to your windows
# All the stuff inside your window. This is the PSG magic code compactor...
layout = [  [sg.Text('I hate this type of Interface but it what it is')],
            [sg.Text('Age'), sg.InputText(key='TextAge')],
            [sg.Text('Gender'), sg.InputText()],
            [sg.SimpleButton(key='btnRUN', button_text= 'Run'), sg.Cancel()]]

# Create the Window
window = sg.Window('Smart Human Interface', layout)
# Event Loop to process "events"

while True:
    event, values = window.read()
    if event == 'btnRUN':
        print(values)
        #upload_to_bucket(blob_name, file_path, bucket_name)
        a.run()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break

window.close()