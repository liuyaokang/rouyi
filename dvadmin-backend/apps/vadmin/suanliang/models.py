from django.db import models

# Create your models here.
class Material_information(models.Model):
    material_num = models.CharField(max_length=32, verbose_name='材料类别编号')
    material_name = models.CharField(max_length=32, verbose_name='材料类别名称')
    is_node_or_not = models.BooleanField(verbose_name='是否叶子节点')
    father_num = models.CharField(max_length=32, verbose_name='所属父类编号')
    material_class =models.CharField(max_length=32, verbose_name='所属材料库类型')
    level = models.CharField(max_length=32, verbose_name='层级')
    create_time = models.DateTimeField(verbose_name="创建时间")
    create_name = models.CharField(max_length=32, verbose_name='创建人')
    update_time = models.DateTimeField(verbose_name="更新时间")
    update_name = models.CharField(max_length=32, verbose_name='创建人')
    status = models.CharField(max_length=32, verbose_name='状态')


    class Meta:
        verbose_name = "材料库信息"
        verbose_name_plural = "材料库信息"
        db_table = "material_information"

class Job_information(models.Model):
    job_num = models.CharField(max_length=32, verbose_name='工种类别编号')
    job_name = models.CharField(max_length=32, verbose_name='工种类别名称')
    is_node_or_not = models.BooleanField(verbose_name='是否叶子节点')
    father_num = models.CharField(max_length=32, verbose_name='所属父类编号')
    job_class =models.CharField(max_length=32, verbose_name='所属工种库编号')
    level = models.CharField(max_length=32, verbose_name='层级')
    create_time = models.DateTimeField(verbose_name="创建时间")
    create_name = models.CharField(max_length=32, verbose_name='创建人')
    update_time = models.DateTimeField(verbose_name="更新时间")
    update_name = models.CharField(max_length=32, verbose_name='创建人')
    status = models.CharField(max_length=32, verbose_name='状态')


    class Meta:
        verbose_name = "工种库信息"
        verbose_name_plural = "工种库信息"
        db_table = "job_information"

class Enterprise_quota_tree(models.Model):
    quota_num = models.CharField(max_length=32, verbose_name='定额类别编号')
    quota_name = models.CharField(max_length=32, verbose_name='定额类别名称')
    is_node_or_not = models.BooleanField(verbose_name='是否叶子节点')
    father_num = models.CharField(max_length=32, verbose_name='所属父类编号')
    quota_class =models.CharField(max_length=32, verbose_name='所属定额库编号')
    level = models.CharField(max_length=32, verbose_name='层级')
    engineering_class = models.CharField(max_length=32, verbose_name='所属施工工程类别')
    create_time = models.DateTimeField(verbose_name="创建时间")
    create_name = models.CharField(max_length=32, verbose_name='创建人')
    update_time = models.DateTimeField(verbose_name="更新时间")
    update_name = models.CharField(max_length=32, verbose_name='创建人')
    status = models.CharField(max_length=32, verbose_name='状态')


    class Meta:
        verbose_name = "企业定额树信息"
        verbose_name_plural = "企业定额树信息"
        db_table = "enterprise_quota_tree"


class Material_detail_information(models.Model):
    material_detail_num = models.CharField(max_length=32, verbose_name='材料编号')
    material_detail_name = models.CharField(max_length=32, verbose_name='材料名称')
    material_specification = models.CharField(max_length=32, verbose_name='材料规格')
    material_unit = models.CharField(max_length=32, verbose_name='材料单位')
    material_price = models.FloatField(verbose_name="材料单价")
    material_class_num = models.CharField(max_length=32, verbose_name='所属材料库类别编号')
    material_class =models.CharField(max_length=32, verbose_name='所属材料库类型')
    create_time = models.DateTimeField(verbose_name="创建时间")
    create_name = models.CharField(max_length=32, verbose_name='创建人')
    update_time = models.DateTimeField(verbose_name="更新时间")
    update_name = models.CharField(max_length=32, verbose_name='创建人')
    status = models.CharField(max_length=32, verbose_name='状态')


    class Meta:
        verbose_name = "材料明细信息"
        verbose_name_plural = "材料明细信息"
        db_table = "material_detail_information"


class Job_detail_information(models.Model):
    job_detail_num = models.CharField(max_length=32, verbose_name='工种编号')
    job_detail_name = models.CharField(max_length=32, verbose_name='工种名称')
    job_specification = models.CharField(max_length=32, verbose_name='工种规格')
    job_unit = models.CharField(max_length=32, verbose_name='计量单位')
    job_price = models.FloatField(verbose_name="工种单价")
    job_class_num = models.CharField(max_length=32, verbose_name='所属工种库类别编号')
    job_class = models.CharField(max_length=32, verbose_name='所属工种库类型')
    create_time = models.DateTimeField(verbose_name="创建时间")
    create_name = models.CharField(max_length=32, verbose_name='创建人')
    update_time = models.DateTimeField(verbose_name="更新时间")
    update_name = models.CharField(max_length=32, verbose_name='创建人')
    status = models.CharField(max_length=32, verbose_name='状态')


    class Meta:
        verbose_name = "工种明细信息"
        verbose_name_plural = "工种明细信息"
        db_table = "job_detail_information"


class Quota_detail_information(models.Model):
    quota_detail_num = models.CharField(max_length=32, verbose_name='定额编号')
    quota_detail_name = models.CharField(max_length=32, verbose_name='定额名称')
    quota_unit = models.CharField(max_length=32, verbose_name='计量单位')
    quota_price = models.IntegerField(verbose_name="定额单价")
    quota_class_num = models.CharField(max_length=32, verbose_name='所属定额类别编号')
    quota_class =models.CharField(max_length=32, verbose_name='所属定额类别')
    engineering_class = models.CharField(max_length=32, verbose_name='所属施工工程类别')
    quota_engineering = models.CharField(max_length=32, verbose_name='定额项目特征')
    job_content = models.TextField(max_length=32, verbose_name='工作内容描述')
    create_time = models.DateTimeField(verbose_name="创建时间")
    create_name = models.CharField(max_length=32, verbose_name='创建人')
    update_time = models.DateTimeField(verbose_name="更新时间")
    update_name = models.CharField(max_length=32, verbose_name='创建人')
    status = models.CharField(max_length=32, verbose_name='状态')


    class Meta:
        verbose_name = "定额明细信息"
        verbose_name_plural = "定额明细信息"
        db_table = "quota_detail_information"

class Measure_rate(models.Model):
    measure_num = models.CharField(max_length=32, verbose_name='措施费率编号')
    measure_name = models.CharField(max_length=32, verbose_name='措施费率名称')
    measure_class =models.CharField(max_length=32, verbose_name='所属材料库类型')
    measure_level = models.CharField(max_length=32, verbose_name='费率档次')
    measure_subject = models.CharField(max_length=32, verbose_name='所属取费专业')
    measure_rate = models.FloatField(verbose_name="对应费率")
    create_time = models.DateTimeField(verbose_name="创建时间")
    create_name = models.CharField(max_length=32, verbose_name='创建人')
    update_time = models.DateTimeField(verbose_name="更新时间")
    update_name = models.CharField(max_length=32, verbose_name='创建人')
    status = models.CharField(max_length=32, verbose_name='状态')


    class Meta:
        verbose_name = "措施费率信息"
        verbose_name_plural = "措施费率信息"
        db_table = "measure_rate_information"

class Quota_business_detail_information(models.Model):
    quota_detail_num = models.CharField(max_length=32, verbose_name='定额编号')
    quota_detail_name = models.CharField(max_length=32, verbose_name='定额名称')
    relate_business_class = models.CharField(max_length=32, verbose_name='关联业务类别')
    relate_business_num = models.CharField(max_length=32, verbose_name='关联业务编码')
    relate_business_unit = models.CharField(max_length=32, verbose_name='关联业务单位')
    relate_business_consume = models.FloatField(max_length=32, verbose_name='关联业务单位')
    relate_business_fix_price = models.FloatField(max_length=32, verbose_name='关联业务定额价格')
    relate_business_tax_price = models.FloatField(max_length=32, verbose_name='关联业务含税价')
    coefficient = models.FloatField(max_length=32, verbose_name='系数',default=1)
    original_consumption =models.FloatField(max_length=32, verbose_name='原始消耗量')
    marks = models.FloatField(max_length=256, verbose_name='备注')
    create_time = models.DateTimeField(verbose_name="创建时间")
    create_name = models.CharField(max_length=32, verbose_name='创建人')
    update_time = models.DateTimeField(verbose_name="更新时间")
    update_name = models.CharField(max_length=32, verbose_name='创建人')
    status = models.CharField(max_length=32, verbose_name='状态')


    class Meta:
        verbose_name = "企业定额业务明细"
        verbose_name_plural = "企业定额业务明细"
        db_table = "quota_business_detail_information"