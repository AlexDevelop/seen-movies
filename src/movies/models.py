from django.db import models


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Movie(BaseModel):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    imdb_id = models.CharField(max_length=30)
    year = models.CharField(max_length=30)  # Use Date field and format with Year only

    def __str__(self):
        return "{} {} {} {} {}".format(self.created_date, self.name, self.last_name, self.imdb_id, self.year)
