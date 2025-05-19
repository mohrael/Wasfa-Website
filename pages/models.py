from django.db import models
from django.db import models
from django.utils.text import slugify


class user(models.Model):
    username = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, unique=True, null=True)
    password = models.CharField(max_length=50, null=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username or 'No Username'


class Recipe(models.Model):
    COURSE_TYPE_CHOICES = [
        ('maincourse', 'Main Course'),
        ('dessert', 'Dessert'),
        ('appetizer', 'Appetizer'),
    ]

    name = models.CharField(max_length=255, null=True)
    course_type = models.CharField(max_length=20, choices=COURSE_TYPE_CHOICES)
    notes = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Recipe.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    
class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=100)  # You can use a CharField to store quantities like '2 cups', '1 tbsp', etc.

    def __str__(self):
        return f"{self.quantity} of {self.name}"


class Step(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='steps', on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    description = models.TextField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Step {self.order} for {self.recipe.name}"
