from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('document_parsing', '0004_auto_20180917_0645'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documentversionparseerror',
            old_name='document_version',
            new_name='document_file',
        ),
    ]