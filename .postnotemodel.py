class Postnote(models.Model):
    title = models.CharField(help_text='Enter a note title')
    author = models.CharField(max_length=100, help_text='Enter the author of the note')
    content = models.TextField(help_text='Enter the content of the note')

    def __str__(self):
        """String for representing the Model object."""
        return self.title
