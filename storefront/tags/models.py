from django.db import models
#from store.models import Product jika menggunakan seperti itu, maka akan bergantung pada store, dan  akan sulit kedepannya jika akan men-tag artikel atau videos dll.
from django.contrib.contenttypes.models import ContentType
#ContentType allowing to generic relationship
from django.contrib.contenttypes.fields import GenericForeignKey

class TaggedItemManager(models.Manager):
    def get_tags_for(self, obj_type, obj_id):
        content_type = ContentType.objects.get_for_model(obj_type)
    
        return TaggedItem.objects.select_related('tag').filter(
                content_type=content_type,
                object_id=obj_id
                )

class Tag(models.Model):
    label = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.label
    
class TaggedItem(models.Model):
    objects = TaggedItemManager()
    #what Tag applied to what Object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    #requirement to identify an object: information about Type(product, video, articel, etc.) and ID

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    #primary key is assumed as positive integer
    content_object = GenericForeignKey()
    