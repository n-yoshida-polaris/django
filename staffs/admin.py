from django.contrib import admin

# Register your models here.
from staffs.models import Issues
from staffs.models import IssueStatuses

# 削除ボタンの非活性化
def has_delete_permission(self, request, obj=None):
    return False

# 追加ボタンの非活性化
def has_add_permission(self, request):
    return False

# 更新ボタンの非活性化
def has_change_permission(self, request, obj=None):
    return False

# admin.site.register(IssueStatuses)


admin.ModelAdmin.has_add_permission = has_add_permission
admin.ModelAdmin.has_change_permission = has_change_permission
admin.ModelAdmin.has_delete_permission = has_delete_permission

# 一覧画面 操作
admin.site.disable_action('delete_selected')

@admin.register(IssueStatuses)
class IssueStatusesAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Issues)
class IssuesAdmin(admin.ModelAdmin):
    list_display = ('subject', 'peipei', 'poipoioi')

    def peipei(self, obj):
        return obj.poison.id

    def poipoioi(self, obj):
        return obj.poison.name
