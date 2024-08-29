
class Cart():
    def __init__(self, request):
        self.session = request.session

        # get the current session key if it exist
        cart = self.session.get('session_key')

        #If the user is new, no session key! then create one!
        cart = self.session['session_key']={}