from rest_framework import serializers
from .models import Student, Address

# class AddressSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Address
#         fields = ["id", "city", "state"]
#
# class StudentSerializer(serializers.ModelSerializer):
#     addresslist = AddressSerializer(many=True, read_only=True)
#     # print(address)
#     class Meta:
#         model = Student
#         # fields = "__all__"
#         fields = ['id', 'name', 'addresslist']



def max_length(value):
    if len(value) > 10:
        raise serializers.ValidationError("Name should not be more than 10")
    return value
class AddressSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    # students = StudentSerializer(read_only=True)
    # student_data = serializers.SerializerMethodField()
    class Meta:
        model = Address
        fields = "__all__"
        # fields = ["id", "city", "state", "students"]

    def get_student_name(self, objects):
        return objects.student.name

class StudentSerializer(serializers.ModelSerializer):
    grade = serializers.SerializerMethodField('find_grade')
    # address = AddressSerializer(read_only=True)
    class Meta:
        model = Student
        fields = "__all__"

    def find_grade(self, obj):
        if obj.marks > 90:
            return 'A'
        elif obj.marks >70 and obj.marks <= 90:
            return 'B'
        else:
            return 'C'

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name should be more than 2")
        return value

    ### object level validation
    def validate(self, data):
        if data['marks'] > 100:
            raise serializers.ValidationError("Marks should not be more than 100")
        return data
# class AddressSerializer(serializers.ModelSerializer):
#     # students = StudentSerializer(read_only=True)
#     # student_data = serializers.SerializerMethodField()
#     class Meta:
#         model = Address
#         fields = "__all__"
#         # fields = ["id", "city", "state", "students"]

    # def get_student_data(self, object):


# class StudentSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[max_length])
#     email = serializers.EmailField()
#     marks = serializers.IntegerField()
#
#     ### field level validation
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Name should be more than 2")
#         return value
#
#     ### object level validation
#     def validate(self, data):
#         if data['marks'] > 100:
#             raise serializers.ValidationError("Marks should not be more than 100")
#         return data
#
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)       ### if no value then instance.name will take previous value
#         instance.email = validated_data.get('email', instance.email)
#         instance.marks = validated_data.get('marks', instance.marks)
#         instance.save()     ## used for saving db changes
#         return instance