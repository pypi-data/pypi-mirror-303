from datetime import datetime

def greet():
    
    '''
    Greets user based on time of the day.
    
    Returns: 
        greetings (str)
    ''' 
    
    time = datetime.now().hour
    if time < 12:
        return 'Good Morning!'
    elif time < 15:
        return 'Good Afternoon!'
    elif time < 18:
        return 'Good Evening!'
    else:
        return 'Good Night!'