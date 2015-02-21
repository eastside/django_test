class BadMiddleware(object):
    def process_view(self, request, *args, **kwargs):
        # Access a key on the POST dictionary...
        print request.POST.get("")
