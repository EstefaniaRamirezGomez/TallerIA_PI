from django.core.management.base import BaseCommand
import numpy as np
from movie.models import Movie

class Command(BaseCommand):
    help = 'Display embeddings for a randomly selected movie'

    def handle(self, *args, **kwargs):
        # Select a random movie
        movie = Movie.objects.order_by('?').first()
        if not movie:
            self.stdout.write(self.style.ERROR("No movies found in the database"))
            return

        self.stdout.write(f"🎬 Random Movie: {movie.title}")
        self.stdout.write(f"📝 Description: {movie.description[:100]}...")
        self.stdout.write(f"🎭 Genre: {movie.genre}")
        self.stdout.write(f"📅 Year: {movie.year}")

        try:
            # Retrieve embedding
            embedding_vector = np.frombuffer(movie.emb, dtype=np.float32)
            self.stdout.write(f"\n🔢 Embedding (first 10 values): {embedding_vector[:10]}")
            self.stdout.write(f"📏 Vector length: {len(embedding_vector)}")

            # Optional: Show some statistics
            self.stdout.write(f"📊 Mean: {embedding_vector.mean():.4f}")
            self.stdout.write(f"📈 Std: {embedding_vector.std():.4f}")
            self.stdout.write(f"🔺 Max: {embedding_vector.max():.4f}")
            self.stdout.write(f"🔻 Min: {embedding_vector.min():.4f}")

        except Exception as e:
            self.stderr.write(f"❌ Error retrieving embedding: {e}")