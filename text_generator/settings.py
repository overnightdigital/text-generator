import os
# 5. Explain how we have all the env in one place 
# and want to load them here so we don't need to change them everywhere

ADMIN_USERNAME=os.environ.get('ADMIN_USERNAME')
ADMIN_PASSWORD=os.environ.get('ADMIN_PASSWORD')