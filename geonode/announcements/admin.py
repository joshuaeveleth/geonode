from django.contrib import admin
from geonode.announcements.models import Announcement, AnnouncementType, AnnouncementUserTarget, AnnouncementGroupTarget, AnnouncementResourceTarget, AnnouncementDismissalOption, Dismissal, DismissalType

class AnnouncementAdmin(admin.ModelAdmin):
    model = Announcement
    list_display = ('id', 'title', 'dateCreated', 'type', 'message','owner')
    list_display_links = ('id',)
    list_filter  = ('dateCreated',)
    search_fields = ('title',)
    date_hierarchy = 'dateCreated'

class AnnouncementTypeAdmin(admin.ModelAdmin):
    model = AnnouncementType
    list_display_links = ('identifier',)
    list_display = ('identifier', 'description')
    
    def has_add_permission(self, request):
            return False
        
    def has_delete_permission(self, request, obj=None):
            return False

class AnnouncementUserTargetAdmin(admin.ModelAdmin):
    model = AnnouncementUserTarget
    list_display_links = ('id',)
    list_display = ('id', 'announcement','target',)

class AnnouncementGroupTargetAdmin(admin.ModelAdmin):
    model = AnnouncementGroupTarget
    list_display_links = ('id',)
    list_display = ('id', 'announcement','target',)

class AnnouncementResourceTargetAdmin(admin.ModelAdmin):
    model = AnnouncementResourceTarget
    list_display_links = ('id',)
    list_display = ('id', 'announcement','target',)

class AnnouncementDismissalOptionAdmin(admin.ModelAdmin):
    model = AnnouncementDismissalOption
    list_display_links = ('id',)
    list_display = ('id', )

class DismissalAdmin(admin.ModelAdmin):
    model = Dismissal
    list_display_links = ('id',)
    list_display = ('id',)

class DismissalTypeAdmin(admin.ModelAdmin):
    model = DismissalType
    list_display_links = ('identifier',)
    list_display = ('identifier', 'description')
    
    def has_add_permission(self, request):
            return False
        
    def has_delete_permission(self, request, obj=None):
            return False

admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(AnnouncementType, AnnouncementTypeAdmin)
admin.site.register(AnnouncementUserTarget, AnnouncementUserTargetAdmin)
admin.site.register(AnnouncementGroupTarget, AnnouncementGroupTargetAdmin)
admin.site.register(AnnouncementResourceTarget, AnnouncementResourceTargetAdmin)
admin.site.register(AnnouncementDismissalOption, AnnouncementDismissalOptionAdmin)
admin.site.register(Dismissal, DismissalAdmin)
admin.site.register(DismissalType, DismissalTypeAdmin)
