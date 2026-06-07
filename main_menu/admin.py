from django.contrib import admin
from django.db.models import Count
from .models import Mem, Comment

@admin.register(Mem)
class AdminMem(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo', 'author_name')
    search_fields = ('title',)
    readonly_fields = ('author_name',)
    list_per_page = 20
    def changelist_view(self, request, extra_context=None):
        stats = Mem.objects.aggregate(all_mems = Count('id'))
        msg = (
            f"📊 СТАТИСТИКА: "
            f"Всего мемов: {stats['all_mems']}")
        self.message_user(request, msg, level ="INFO")
        return super().changelist_view(request,extra_context = extra_context)


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ('id','author_name', 'mem', 'comment')
    search_fields = ('author_name',)
    readonly_fields = ('author_name',)
    paginator = 20

