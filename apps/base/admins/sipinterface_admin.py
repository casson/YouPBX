# coding=utf-8

from xadmin import site
from xadmin.utils import fa_icon

from apps.base import models
from apps.common import ReXmlAdmin


class SipInterfaceAdmin(ReXmlAdmin):
    
    menu_group = 'network_group'
    order = 1
    model_icon = fa_icon('plug')
    
    def get_nav_btns(self):
        return [
            '''<a href="/xadmin/page/sipinterfaceautoconf/" class="btn btn-primary"><i class="fa fa-inbox"></i> 自动检测</a> '''
        ]

site.register(models.SipInterface, SipInterfaceAdmin)