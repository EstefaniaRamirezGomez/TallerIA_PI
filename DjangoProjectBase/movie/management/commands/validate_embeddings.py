from django.core.management.base import BaseCommand
import numpy as np
from movie.models import Movie

class Command(BaseCommand):
    help = 'Validate that embeddings are stored correctly in the database'

    def handle(self, *args, **kwargs):
        movies = Movie.objects.all()
        self.stdout.write(f"Validating embeddings for {movies.count()} movies...\n")

        for movie in movies:
            try:
                embedding_vector = np.frombuffer(movie.emb, dtype=np.float32)
                self.stdout.write(f"{movie.title}: {embedding_vector[:5]}")
            except Exception as e:
                self.stderr.write(f"❌ Error retrieving embedding for {movie.title}: {e}")

        self.stdout.write(self.style.SUCCESS("\n✅ Validation completed"))