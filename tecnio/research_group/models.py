from django.db import models


class Person(models.Model):
    PREFIXES = (
        ('PHD', 'PhD.'),
        ('MSC', 'MSc.'),
        ('ENG', 'Ing.'),
        ('MAL', 'Sr.'),
        ('FEM', 'Sra.')
    )
    name = models.CharField("Nombre",max_length=150)
    prefix = models.CharField("Prefijo", max_length=3, choices=PREFIXES,
                              default=None, blank=True, null=True,
                              )
    title = models.TextField("Títulos")
    photo_url = models.URLField("Fotografía", max_length=250, default=None, blank=True, null=True)

    def __str__(self):
        if self.prefix:
            return self.get_prefix_display() + ' ' + self.name
        else:
            return self.name


class Item(models.Model):
    name = models.CharField(max_length=250)
    abstract = models.TextField()
    date = models.DateField()
    information = models.TextField()
    image_url = models.CharField(max_length=250, default=None,
                                 blank=True, null=True)
    source = models.TextField()
    main_project = models.ForeignKey('self')


class Project(models.Model):
    object = models.OneToOneField(Item)


class Article(models.Model):
    object = models.OneToOneField(Item)


class Conference(models.Model):
    object=models.OneToOneField(Item)
    place=models.TextField()
    end_date=models.DateField()


class Ownership(models.Model):
    person=models.ForeignKey(Person, on_delete=models.CASCADE)
    object=models.ForeignKey(Item, on_delete=models.CASCADE)
    main=models.BooleanField()




