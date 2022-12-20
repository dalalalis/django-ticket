from rest_framework.permissions import BasePermission

# class IsOwner(BasePermission):
#     message = 'You should be an admin to edit or create an event'
#     def has_object_permission(self, request, view, obj):
#         return request.user.is_superuser 