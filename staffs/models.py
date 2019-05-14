from django.db import models


class Issues(models.Model):
    tracker_id = models.IntegerField()
    project_id = models.IntegerField()
    subject = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    # category_id = models.IntegerField(blank=True, null=True)
    status_id = models.IntegerField()
    assigned_to_id = models.IntegerField(blank=True, null=True)
    priority_id = models.IntegerField()
    fixed_version_id = models.IntegerField(blank=True, null=True)
    author_id = models.IntegerField()
    lock_version = models.IntegerField()
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    done_ratio = models.IntegerField()
    estimated_hours = models.FloatField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    root_id = models.IntegerField(blank=True, null=True)
    lft = models.IntegerField(blank=True, null=True)
    rgt = models.IntegerField(blank=True, null=True)
    is_private = models.IntegerField()
    closed_on = models.DateTimeField(blank=True, null=True)

    poison = models.ForeignKey(
        'IssueStatuses',
        models.PROTECT,
        db_column='category_id',
        to_field='position',
        related_name='issue_statuses'
    )

    class Meta:
        managed = False
        db_table = 'issues'

class IssueStatuses(models.Model):
    name = models.CharField(max_length=30)
    is_closed = models.IntegerField()
    position = models.IntegerField(blank=True, null=True, unique=True)
    default_done_ratio = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issue_statuses'
