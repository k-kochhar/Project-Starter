import os

folderName = input('What is the name of the folder?: ')
fileName = input('What is the name of the file?: ') + '.py'

# In this example, I used a folder on my desktop. Feel free to use whatever you want
specifiedFolder = '\Python\Learning'

# Get the path to the desktop directory
desktopPath = os.path.join(os.path.expanduser('~'), 'Desktop') + specifiedFolder

# Create the folder
if not os.path.exists(os.path.join(desktopPath, folderName)):
    os.makedirs(os.path.join(desktopPath, folderName))

# Create the file if it does not already exist
if not os.path.exists(os.path.join(desktopPath, folderName, fileName)):
    with open(os.path.join(desktopPath, folderName, fileName), 'w') as f:
        f.write('# Hello World.')

# Open the file in VS Code
os.system(f'code {os.path.join(desktopPath, folderName, fileName)}')