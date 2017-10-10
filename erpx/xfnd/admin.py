from django.contrib import admin

# Register your models here.
from .models import XfndUser
from .models import XfndProgram
from .models import XfndFunction
from .models import XfndMenu
from .models import XfndMenuItem
from .models import XfndReportGroup
from .models import XfndReportGroupItem
from .models import XfndResp
from .models import XfndUserResp
from .models import XfndLoginLog
from .models import XfndFunctionExecLog


admin.site.register(XfndUser);
admin.site.register(XfndProgram);
admin.site.register(XfndFunction);
admin.site.register(XfndMenu);
admin.site.register(XfndMenuItem);
admin.site.register(XfndReportGroup);
admin.site.register(XfndReportGroupItem);
admin.site.register(XfndResp);
admin.site.register(XfndUserResp);
admin.site.register(XfndLoginLog);
admin.site.register(XfndFunctionExecLog);

