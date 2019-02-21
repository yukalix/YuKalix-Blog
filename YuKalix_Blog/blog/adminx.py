from  xadmin import views
import xadmin

from .models import Banner, AboutMeInfo
from .models import AboutMeArticle
from .models import Article,ArticleTag
from .models import MessageUserPhoto, Message, Blogroll
# 管理平台主题更改
class BaseSetting(object):
    # 使用主题管理器
    enable_themes = True
    # 使用主题
    use_bootswatch = True

class GlobalSetting(object):
    # 设置base_site.html的Title
    site_title = 'YuKalix博客后台管理'
    # 设置base_site.html的Footer
    site_footer = 'YuKalix小小窝'
    # 设置导航折叠,以每一个app为一个折叠框
    # menu_style = 'accordion'
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)


# 主页
class BannerAdmin(object):
    list_display = ('baner_describe', 'add_time')

# 关于我信息
class AboutMeInfoAdmin(object):
    # 图标
    # model_icon = 'fa fa-user-plus'
    list_display = ('nick_name','name','work','place','email','record_tip','add_time')
    style_fields = {'goods_desc': 'ueditor'}
    # search_fields  = ('add_time')

xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(AboutMeInfo, AboutMeInfoAdmin)


class AboutMeArticleAdmin(object):
    list_display = ('title', 'article')

xadmin.site.register(AboutMeArticle, AboutMeArticleAdmin)

class ArticleTagAdmin(object):
    list_display = search_fields = list_filter = ['id', 'tag_name']
    list_editable = ['tag_name']
    ordering = ['-id']
    relfield_style = 'fk-ajax'
    refresh_tiems = [3, 5]
    readonly_fields = ['id']

class ArticleAdmin(object):
    pass

xadmin.site.register(ArticleTag,ArticleTagAdmin)
xadmin.site.register(Article)

# 留言
class MessageUserPhotoAdmin(object):
    pass
class MessageAdmin(object):
    list_display = ('user_name', 'message')

xadmin.site.register(Message, MessageAdmin)
xadmin.site.register(MessageUserPhoto)

# 友情链接
class BlogrollAdmin(object):
    list_display = ('name',)

xadmin.site.register(Blogroll, BlogrollAdmin)