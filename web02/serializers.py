from rest_framework import serializers
from .models import StudentInfo,ClassInfo


# class ClassInfoSerializer(serializers.Modelserializer):
#     class Meta:
#         model = ClassInfo
#         fields = ('major_name')

# class StudentInfoSerializer(serializers.Modelserializer):
#     major_name = serializers.ReadOnlyField()
#     major_id = serializers.ReadOnlyField()
#     class Meta:
#         model = StudentInfo
#         fields = (
#             'name',
#             'student_num',
#             'major_name',
#             'major_id',
#             'the_1st_judge',
#             'the_2nd_judge',
#             'the_3rd_judge',
#             'the_4th_judge',
#             'the_5th_judge',
#             'the_6th_judge',
#             'the_7th_judge',
#             'the_8th_judge',
#         )
        