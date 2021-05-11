from django.contrib import admin

from leads.models import Agent, Lead, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    pass


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    pass
