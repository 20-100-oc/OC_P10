# Execute this if running the bot locally.
# Generate a command to paste in powershell to set environment variables



def env_variables_command():
    '''
    # old
    secrets = {
        "PORT": "8000", 
        "MicrosoftAppId": "", 
        "MicrosoftAppPassword": "", 
        "LuisAppId": "448b542a-1140-48af-a909-207052d7fc5a", 
        "LuisAPIKey": "ec52dd6d1e7449b1b0e33adead613bb4", 
        "LuisAPIHostName": "westeurope.api.cognitive.microsoft.com", 
        "AppInsightsInstrumentationKey": "5d20c1e7-4c90-44aa-89e6-ed28c9d458eb"
    }
    '''

    # new
    secrets = {
        "PORT": "8000", 
        "MicrosoftAppId": "", 
        "MicrosoftAppPassword": "", 
        "LuisAppId": "c78c19a0-1730-441c-9d70-b93e292192b1", 
        "LuisAPIKey": "03773c8be49140af87a85494568f93fc", 
        "LuisAPIHostName": "westeurope.api.cognitive.microsoft.com", 
        "AppInsightsInstrumentationKey": "5d20c1e7-4c90-44aa-89e6-ed28c9d458eb", 
        "LuisAppEndpoint": "https://oc-10-luis-pred-2.cognitiveservices.azure.com/"
    }


    command = ''
    for i, key_name in enumerate(secrets):
        semicolon = ';' if i >= 1 else ''

        key = secrets[key_name]
        if len(key) > 0:
            command += semicolon + f'$Env:{key_name}="{key}"'

    return command



if __name__ == '__main__':
    command = env_variables_command()
    print(command)
