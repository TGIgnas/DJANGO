from django.contrib import admin
from .models import AutomobilioModelis, Automobilis, Paslauga, Užsakymas, UžsakymoEilutė


class UžsakymoEilutėInline(admin.TabularInline):
    model = UžsakymoEilutė


class UžsakymasAdmin(admin.ModelAdmin):
    list_display = ('automobilis', 'data')
    inlines = [UžsakymoEilutėInline]


class AutomobilisAdmin(admin.ModelAdmin):
    list_display = ('klientas', 'automobilio_modelis', 'valstybinis_nr', 'vin_kodas')
    list_filter = ('klientas', 'automobilio_modelis')
    search_fields = ('valstybinis_nr', 'vin_kodas')


class PaslaugaAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', 'kaina')


admin.site.register(AutomobilioModelis)
admin.site.register(Automobilis, AutomobilisAdmin)
admin.site.register(Paslauga, PaslaugaAdmin)
admin.site.register(Užsakymas, UžsakymasAdmin)
admin.site.register(UžsakymoEilutė)


def app_resort(func):
    def inner(*args, **kwargs):
        app_list = func(*args, **kwargs)
        # Useful to discover your app and module list:
        # import pprint
        # pprint.pprint(app_list)

        app_sort_key = 'name'
        app_ordering = {
            "APP_NAME1": 1,
            "APP_NAME2": 2,
            "APP_NAME3": 3,
        }

        resorted_app_list = sorted(app_list, key=lambda x: app_ordering[x[app_sort_key]] if x[app_sort_key] in app_ordering else 1000)

        model_sort_key = 'object_name'
        model_ordering = {
            "AutomobilioModelis": 1,
            "Automobilis": 2,
            "Paslauga": 3,
            "Užsakymas": 4,
            "UžsakymoEilutė": 5,
        }
        for app in resorted_app_list:
            app['models'].sort(
                key=lambda x: model_ordering[x[model_sort_key]] if x[model_sort_key] in model_ordering else 1000)
        return resorted_app_list

    return inner


admin.site.get_app_list = app_resort(admin.site.get_app_list)
