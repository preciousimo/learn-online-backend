from rest_framework import serializers
from .models import *
        
from django.contrib.auth.hashers import make_password, check_password

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name', 'email', 'qualification', 'mobile_no', 'skills', 'profile_img',  'password', 'teacher_courses', 'skill_list']
        depth=1
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(TeacherSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super(TeacherSerializer, self).update(instance, validated_data)
    
    def __init__(self, *args, **kwargs):
        super(TeacherSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth=1

class TeacherDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = [ 'total_teacher_courses', 'total_teacher_students', 'total_teacher_chapters']
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = [ 'id', 'title', 'description']
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [ 'id', 'category', 'teacher', 'title', 'description', 'featured_img', 'techs', 'course_chapters', 'related_videos', 'tech_list', 'total_enrolled_students', 'course_rating']
    def __init__(self, *args, **kwargs):
        super(CourseSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth=2
        

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = [ 'id', 'course', 'title', 'description', 'video', 'remarks']
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'username', 'password', 'profile_img', 'interested_categories']
        extra_kwargs = {'password': {'write_only': True}}
        
class StudentDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [ 'enrolled_courses', 'favourite_courses', 'complete_assignments', 'pending_assignments']
        
class StudentCourseEnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCourseEnrollment
        fields = [ 'id', 'course', 'student', 'enrolled_time']
    def __init__(self, *args, **kwargs):
        super(StudentCourseEnrollSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth=2
            
class StudentFavouriteCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentFavouriteCourse
        fields = [ 'id', 'course', 'student', 'status']
    def __init__(self, *args, **kwargs):
        super(StudentFavouriteCourseSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth=2
        
class CourseRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseRating
        fields = [ 'id', 'course', 'student', 'rating', 'reviews', 'review_time']
    def __init__(self, *args, **kwargs):
        super(CourseRatingSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth=1
            
class StudentAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAssignment
        fields = [ 'id', 'teacher', 'student', 'title', 'detail', 'student_status', 'add_time']
    def __init__(self, *args, **kwargs):
        super(StudentAssignmentSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth=2