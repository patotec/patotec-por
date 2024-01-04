from django.db import models

from django.utils.text import slugify


class Contact(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()
	subject = models.CharField(max_length=2000)
	message = models.TextField()

	def __str__ (self):
		return self.name
class About(models.Model):
	name = models.CharField(max_length=200)
	date = models.CharField(max_length=46)
	image = models.ImageField(upload_to='images/media', null=True, blank=True)
	body = models.TextField(max_length=200000)

	def __str__ (self):
		return self.name
class Catagory(models.Model):
    name = models.CharField(max_length=200, null=True)
    slug = models.SlugField(null=True)

    class Meta:
        verbose_name_plural = 'Catagory'

    def __str__(self):
        return str(self.name) 

# tags model
class Tag(models.Model):

    name  = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name 

# Blog model 
class Blog(models.Model):
    status = (
        ('active','active'),
        ('pending','pending')
    )

    title  = models.CharField(max_length=200, null=True)
    detail = models.TextField(max_length=2000, null=True)
    image = models.ImageField(upload_to='images/media', null=True, blank=True)
    catagories = models.ForeignKey(Catagory,on_delete=models.DO_NOTHING, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    status = models.CharField(max_length=20, choices=status, default='pending')
    featured  = models.BooleanField(default=False)
    trending  = models.BooleanField(default=False)
    video  = models.BooleanField(default=False)
    link  = models.CharField(max_length=200, null=True)
    visit_count = models.IntegerField(default=0)
    visible = models.BooleanField(default=True)
    slug = models.SlugField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Blog'

    def overview(self):
        short = self.detail[:30]
        return short 

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    
    # @property
    # def image_url(self):
    #     if self.image and hasattr(self.image, 'url'):
    #         return self.image.url 

    def __str__(self):
        return f"{ self.title}"

# Comment Class
class Comment(models.Model):
    name = models.CharField(max_length=200)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post.title}"



# Create your models here.
class ads(models.Model):
    contact = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='images/ads', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    visible = models.BooleanField(default=True)


    def __str__(self):
        return f"{ self.name}"