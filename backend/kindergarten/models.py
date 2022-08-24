from django.db import models

class Class(models.Model):
    # クラスID
    class_id = models.AutoField(primary_key=True)
    # クラス名
    class_name = models.CharField(max_length=200)


class Child(models.Model):
    # 園児ID
    child_id = models.CharField(max_length=200, primary_key=True)
    # 保護者姓
    parent_last_name = models.CharField(max_length=200)
    # 保護者名
    parent_first_name = models.CharField(max_length=200)
    # 保護者カナ姓
    parent_last_name_kana = models.CharField(max_length=200)
    # 保護者カナ名
    parent_first_name_kana = models.CharField(max_length=200)
    # 園児姓
    child_last_name = models.CharField(max_length=200)
    # 園児名
    child_first_name = models.CharField(max_length=200)
    # 園児カナ姓
    child_last_name_kana = models.CharField(max_length=200)
    # 園児カナ名
    child_first_name_kana = models.CharField(max_length=200)
    # 所属クラスID
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)


class Teacher(models.Model):
    # 保育士ID
    teacher_id = models.CharField(max_length=200, primary_key=True)
    # 姓
    last_name = models.CharField(max_length=200)
    # 名
    first_name = models.CharField(max_length=200)
    # クラスID
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)


class AttendanceData(models.Model):
    # 出欠ID
    attendance_id = models.AutoField(primary_key=True)
    # # 子供ID
    child_id = models.ForeignKey(Child, on_delete=models.CASCADE)
    # 日付
    date = models.DateField(max_length=200)
    # 出欠状態
    status = models.IntegerField()
    # 欠席理由 nullを許す
    reason = models.TextField(max_length=1000, blank=True, null=True)
    # 返信 nullを許す
    reply = models.TextField(max_length=1000, blank=True, null=True)
    # 返信した保育士ID nullを許す
    reply_teacher_id = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, blank=True, null=True)
