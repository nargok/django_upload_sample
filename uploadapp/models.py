from django.db import models


class File(models.Model):
    """
    FileFieldはDBには登録されない特殊なフィールド
    ファイルアップロードの際は、フィールド名にfileを指定する
    """
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name
