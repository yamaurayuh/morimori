from django.contrib import admin
from .models import NutritionFacts
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats

# Register your models here.
# admin.site.unregister(NutritionFacts)
# admin.site.register(NutritionFacts)


class NutritionFactsResource(resources.ModelResource):
    class Meta:
        model = NutritionFacts
        fields = ('id', 'number', 'classification', 'name', 'disposalRate', 'energyJ', 
                  'energyCal', 'moisture', 'proteinByAminoAcidComposition', 'protein', 
                  'fattyAcidTriAcylGlycerolEquivalent', 'cholesterol', 'lipid', 
                  'availableCarbohydrateMonosaccharideEquivalent',
                  'availableCarbohydrateMassTotal', 'deductionLawByAvailableCarbohydrate', 
                  'foodFiberTotal', 'sugarAlcohol', 'carbohydrate', 'organicAcid', 'ash', 
                  'natrium', 'potassium', 'calcium', 'magnesium', 'phosphorus', 'iron', 
                  'zinc', 'copper', 'manganese', 'iodine', 'selenium', 'chrome', 'molybdenum', 
                  'retinol', 'alphaCarotene', 'betaCarotene', 'betaCryptoxanthin', 
                  'betaCaroteneEquivalent', 'vitaminA', 'vitaminD', 'vitaminE', 
                  'betaTocopherol', 'gammaTocopherol', 'deltaTocopherol', 'vitaminK', 
                  'vitaminB1', 'vitaminB2', 'niacin', 'niacinEquivalent', 'vitaminB6', 
                  'vitaminB12', 'folicAcid', 'pantothenicAcid', 'biotin', 'vitaminC', 
                  'alcohol', 'salt', 'note')
        import_id_fields = ['id']

# @admin.register(NutritionFacts)
class NutritionFactsAdmin(ImportExportModelAdmin):
    list_display = ('number', 'classification', 'name', 'disposalRate', 'energyJ', 
                  'energyCal', 'moisture', 'proteinByAminoAcidComposition', 'protein', 
                  'fattyAcidTriAcylGlycerolEquivalent', 'cholesterol', 'lipid', 
                  'availableCarbohydrateMonosaccharideEquivalent',
                  'availableCarbohydrateMassTotal', 'deductionLawByAvailableCarbohydrate', 
                  'foodFiberTotal', 'sugarAlcohol', 'carbohydrate', 'organicAcid', 'ash', 
                  'natrium', 'potassium', 'calcium', 'magnesium', 'phosphorus', 'iron', 
                  'zinc', 'copper', 'manganese', 'iodine', 'selenium', 'chrome', 'molybdenum', 
                  'retinol', 'alphaCarotene', 'betaCarotene', 'betaCryptoxanthin', 
                  'betaCaroteneEquivalent', 'vitaminA', 'vitaminD', 'vitaminE', 
                  'betaTocopherol', 'gammaTocopherol', 'deltaTocopherol', 'vitaminK', 
                  'vitaminB1', 'vitaminB2', 'niacin', 'niacinEquivalent', 'vitaminB6', 
                  'vitaminB12', 'folicAcid', 'pantothenicAcid', 'biotin', 'vitaminC', 
                  'alcohol', 'salt', 'note')

    # django-import-exportsの設定
    resource_class = NutritionFactsResource
    formats = [base_formats.CSV]

admin.site.register(NutritionFacts, NutritionFactsAdmin)