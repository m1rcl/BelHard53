from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Students(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="Студент",
        null=False,
        blank=False,
        # unique = True
        # db_column #Имя столбца базы
        # db_comment
        # db_index
        # editable
        # error_messages # переопределить сообщения об ошибках - null, blank, invalid, unique_for_date
        # help_text #Дополнительный текст «помощи», который будет отображаться с виджетом формы.
        # unique_for_date
    )

    surname = models.CharField(
        max_length=30,
        verbose_name="Фамилия",
    )
    sex = models.CharField(
        max_length=1,
        choices=[("m", "Мужчина"), ("w", "Женщина")],
        verbose_name="Пол",
    )
    active = models.BooleanField(
        verbose_name="Активный",
    )

    age = models.SmallIntegerField(
        null=True,
        validators=[MinValueValidator(18), MaxValueValidator(120)],
    )

    course = models.ManyToManyField(
        to="Course",
        blank=True,
        verbose_name="Посещаемые курсы",
    )

    photo = models.ImageField(
        upload_to=r"photos/%Y/%m/%d",
        blank=True,
        verbose_name="Фoто",
    )

    def __str__(self):
        return f"{self.name} {self.surname}"

    def get_absolute_url(self):
        return reverse("student", kwargs={"id": self.pk})

    class Meta:
        indexes = [models.Index(fields=["surname"])]
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
        unique_together = [["name", "surname"]]
        db_table = "students"
        ordering = ["surname"]
        # absrtract = True


class Course(models.Model):
    langs = [
        ("py", "Python"),
        ("js", "JavaScript"),
        ("c", "C++"),
        ("an", "Android"),
    ]
    name = models.CharField(
        max_length=20,
        choices=langs,
    )
    course_num = models.SmallIntegerField(
        default=1,
        verbose_name="Номер курса",
        validators=[MinValueValidator(1), MaxValueValidator(100)],
    )
    start_date = models.DateField(
        verbose_name="Начало курса",
        null=True,
    )
    end_date = models.DateField(
        verbose_name="Окончание курса",
        null=True,
    )
    description = models.TextField(
        blank=True,
        verbose_name="Описание",
    )

    def __str__(self):
        return f"{self.get_name_display()} - {self.course_num}"

    class Meta:
        unique_together = [["name", "course_num"]]
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["name", "course_num"]


class Rating(models.Model):

    student = models.ForeignKey(Students, on_delete=models.CASCADE)

    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    mark = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name="Оценка",
    )

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"

    def __str__(self):
        return f"{self.student} - {self.course} - оценка {self.mark}"


"""
CRUD

CREATE        
s1 = Students(name="Николай", surname="Николаев", active=True)         
s1.save()

Students.objects.create(name="Николай2", surname="Николаев2", active=True) 
или 
s2 = Students.objects.create(name="Николай3", surname="Николаев3", active=True) 

c1 = Course(name='py', course_num=3)
c2 = Course(name='js', course_num=4)
c1.save()
c2.save()

s1.course.add(c1) 
s1.course.add(c2) 
s1.course.remove(c2) 


--------------------------
READ
all_students = Students.objects.all()
for student in all_students:
    print(student)


student = Students.objects.get(id=1)
for c in student.course:
    print(c)
    
male_students = Students.objects.filter(sex='m')

c3 = Course.objects.get(id=1)
c3.students_set.all() # все студенты на курсе с3


----------------------
UPDATE
student = Students.objects.get(id=1)
student.age = 21  
student.save()  

Students.objects.filter(age__gt=30).update(active=True)



---------------------
DELETE
student = Students.objects.get(id=1)
student.delete()

Students.objects.filter(active=False).delete()

"""
