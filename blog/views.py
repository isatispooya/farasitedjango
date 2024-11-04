from rest_framework import viewsets
from website import models
from website import serializer
from rest_framework import serializers

# Create your views here.
class BlogViewSet(viewsets.ModelViewSet):
    queryset = models.News.objects.all()
    serializer_class = serializer.News
    
    def get_queryset(self):
        domain = self.request.query_params.get('domain')
        if not domain:
            raise serializers.ValidationError({'domain': 'این پارامتر الزامی است'})
        try:
            domain_obj = models.Domain.objects.get(domain=domain)
        except models.Domain.DoesNotExist:
            raise serializers.ValidationError({'domain': 'دامنه مورد نظر یافت نشد'})
            
        queryset = super().get_queryset().filter(Domain=domain_obj, show=True)
        if not queryset.exists():
            raise serializers.ValidationError({'error': 'هیچ داده‌ای با این فیلترها یافت نشد'})
            
        return queryset
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

