import random
from io import BytesIO

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from PIL import Image, ImageDraw, ImageFont

from blog_buster.models import Post


class Command(BaseCommand):
    help = "Generate dummy featured images for posts that do not have one."

    def add_arguments(self, parser):
        parser.add_argument(
            '--limit',
            type=int,
            default=None,
            help='Maximum number of posts to update',
        )

    def handle(self, *args, **options):
        limit = options.get('limit')
        posts = Post.objects.filter(featured_image='') | Post.objects.filter(featured_image__isnull=True)
        if limit:
            posts = posts[:limit]

        updated = 0
        for post in posts:
            image_file = self._generate_image(post.title)
            filename = f"{slugify(post.title)}.jpg" or f"post-{post.id}.jpg"
            post.featured_image.save(filename, image_file, save=True)
            updated += 1
            self.stdout.write(self.style.SUCCESS(f"Attached dummy image to '{post.title}'"))

        if updated == 0:
            self.stdout.write(self.style.WARNING("All posts already have featured images."))
        else:
            self.stdout.write(self.style.SUCCESS(f"Dummy images added to {updated} post(s)."))

    def _generate_image(self, title):
        width, height = 1200, 800
        base_colors = [
            (0, 102, 204),
            (15, 23, 42),
            (0, 168, 232),
            (34, 197, 94),
            (234, 179, 8),
        ]
        color = random.choice(base_colors)

        image = Image.new("RGB", (width, height), color)
        draw = ImageDraw.Draw(image)

        accent = tuple(min(255, c + 40) for c in color)
        draw.rectangle([0, height - 200, width, height], fill=accent)

        font_size = 72
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except IOError:
            font = ImageFont.load_default()

        text = title[:60]
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        text_x = (width - text_width) / 2
        text_y = (height - text_height) / 2

        draw.text((text_x, text_y), text, fill=(255, 255, 255), font=font)

        buffer = BytesIO()
        image.save(buffer, format="JPEG", quality=85)
        buffer.seek(0)
        return ContentFile(buffer.read())

