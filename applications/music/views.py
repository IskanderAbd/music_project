from rest_framework import generics



class MusicListView(generics.ListAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
