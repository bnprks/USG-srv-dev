import django_tables2 as tables
from wintersession.models import Course, Student, Registration

class CourseTable(tables.Table):
    get_instructors = tables.Column(verbose_name="Instructors", orderable=False)
    current_enroll = tables.Column(orderable=False)
    max_enroll = tables.Column(orderable=False)
    class Meta:
        model = Course
        attrs = {"class": "paleblue"}
        fields = ('courseID', 'title', 'schedule', 'current_enroll', 'max_enroll', 'get_instructors', 'room',)
        order_by = ('courseID')
        
class LtdCourseTable(tables.Table):
    get_instructors = tables.Column(verbose_name="Instructors", orderable=False)
    current_enroll = tables.Column(orderable=False)
    max_enroll = tables.Column(orderable=False)
    class Meta:
        model = Course
        attrs = {"class": "paleblue"}
        fields = ('courseID', 'title', 'schedule', 'current_enroll', 'max_enroll', 'get_instructors',)
        order_by = ('courseID')

        
class StudentTable(tables.Table):
    class Meta:
        model = Student
        attrs = {"class": "paleblue"}
        fields = ('netID', 'first_name', 'last_name', )
        ordering = ('last_name',)        
        
class AttendanceTable(tables.Table):
    netID = tables.Column(accessor='student.netID')
    first = tables.Column(accessor='student.first_name')
    last = tables.Column(accessor='student.last_name')
    class Meta:
        model = Registration
        attrs = {"class": "paleblue"}
        fields = ('attendance_M', 'attendance_Tu', 'attendance_W',
                     'attendance_Th', 'attendance_F',)
        sequence = ('netID', 'first', 'last', 'attendance_M', 'attendance_Tu', 'attendance_W',
                     'attendance_Th', 'attendance_F',)
        order_by = 'last'
