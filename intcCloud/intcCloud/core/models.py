from django.db import models


class Document(models.Model):
    documentName = models.CharField("<b>Наименование модуля </b>", max_length=255)
    documentName2 = models.CharField("<b>Наименование дисциплины </b>", max_length=255, default="")
    cycleType = models.CharField("<b>Наименование ПЦК </b>", max_length=255, default="")
    studyGroup = models.CharField("<b>Группа </b>", max_length=255, default="")
    teacherName = models.CharField("<b>ФИО преподавателя </b>",max_length=255)
    documentType = models.CharField("<b>Тип документа </b>",max_length=100)
    document = models.FileField("<b>Файл </b>",upload_to='documents/files')

    def __str__(self):
        return self.documentName

    def delete(self, *args, **kwargs):
        self.document.delete()
        super().delete(*args, **kwargs)

class DiplomaDocument(models.Model):
    speciality = models.CharField("<b>Специальность </b>", max_length=255)
    qualification = models.CharField("<b>Квалификация </b>", max_length=255, default="")
    group = models.CharField("<b>Группа </b>", max_length=255, default="")
    theme = models.CharField("<b>Тема дипломного проекта </b>", max_length=255, default="")
    student = models.CharField("<b>ФИО студента </b>", max_length=255, default="")
    document = models.FileField("<b>Файл </b>",upload_to='documents/files')

    def __str__(self):
        return self.document

    def delete(self, *args, **kwargs):
        self.document.delete()
        super().delete(*args, **kwargs)