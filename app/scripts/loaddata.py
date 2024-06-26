

import os, sys
from django.conf import settings
from module.models import DiagnosticTest,Tag
import csv
sys.path.append('/DjangoWebAppWithoutModelsTemplate/app')
os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'
#django.setup()


print("here")
print(settings.CONFIG_VALUES["nonsmokervalue"])
def run():
    with open('module/data.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header
        DiagnosticTest.objects.all().delete()
        Tag.objects.all().delete()

        # Create all the Tag Objects:
        for tagname in settings.CONFIG_VALUES.values():
            print(tagname)
            tag = Tag(tagname=tagname)
            tag.save()

        for row in reader:
            print(row)



            test = DiagnosticTest(name=row[0],type = row[1], description=row[2],validity_days=row[3],displayicon=row[4])
            test.save()
            tags = [str(name) for name in row[5].split(',')]
            for tag in tags:
                t1 = Tag.objects.get(tagname=tag)
                test.tags.add(t1)


            #genre, _ = Genre.objects.get_or_create(name=row[-1])

            #film = Film(title=row[0],year=row[2],genre=genre)
            #film.save()