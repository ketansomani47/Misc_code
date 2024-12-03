from rest_framework.throttling import UserRateThrottle

class StudentListThrotttle(UserRateThrottle):
    scope = 'student-list'