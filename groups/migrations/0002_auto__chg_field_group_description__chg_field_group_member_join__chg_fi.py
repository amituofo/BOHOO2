# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Group.description'
        db.alter_column('group', 'description', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Group.member_join'
        db.alter_column('group', 'member_join', self.gf('django.db.models.fields.CharField')(max_length=256))

        # Changing field 'Group.last_topic_add'
        db.alter_column('group', 'last_topic_add', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Group.group_type'
        db.alter_column('group', 'group_type', self.gf('django.db.models.fields.CharField')(max_length=256))

    def backwards(self, orm):

        # Changing field 'Group.description'
        db.alter_column('group', 'description', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Group.member_join'
        db.alter_column('group', 'member_join', self.gf('django.db.models.fields.SmallIntegerField')())

        # Changing field 'Group.last_topic_add'
        db.alter_column('group', 'last_topic_add', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Group.group_type'
        db.alter_column('group', 'group_type', self.gf('django.db.models.fields.SmallIntegerField')())

    models = {
        u'User.myuser': {
            'Meta': {'object_name': 'MyUser'},
            'activation_key': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'follower': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'follower_rel_+'", 'to': u"orm['User.MyUser']"}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'job': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'qq': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'sign': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'weibo': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'groups.category': {
            'Meta': {'object_name': 'Category', 'db_table': "'group_category'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['groups.Category']"})
        },
        u'groups.group': {
            'Meta': {'object_name': 'Group', 'db_table': "'group'"},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'category_group'", 'to': u"orm['groups.Category']"}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'creator_group'", 'to': u"orm['User.MyUser']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'flag': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gfriend': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['groups.Group']", 'symmetrical': 'False'}),
            'group_type': ('django.db.models.fields.CharField', [], {'default': "'open'", 'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_topic_add': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'member': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['User.MyUser']", 'symmetrical': 'False'}),
            'member_join': ('django.db.models.fields.CharField', [], {'default': "'everyone_can_join'", 'max_length': '256'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'topic_amount': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'groups.reply': {
            'Meta': {'object_name': 'Reply', 'db_table': "'reply'"},
            'content': ('django.db.models.fields.TextField', [], {}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'creator_reply'", 'to': u"orm['User.MyUser']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topic_replies'", 'to': u"orm['groups.Topic']"})
        },
        u'groups.report': {
            'Meta': {'object_name': 'Report', 'db_table': "'report'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_handle': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reason': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'report_type': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topic_report'", 'to': u"orm['groups.Topic']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_report'", 'to': u"orm['User.MyUser']"})
        },
        u'groups.topic': {
            'Meta': {'object_name': 'Topic', 'db_table': "'topic'"},
            'content': ('django.db.models.fields.TextField', [], {}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'creator_topic'", 'to': u"orm['User.MyUser']"}),
            'dislike': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'group_topic'", 'to': u"orm['groups.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ilike': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'is_closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_top': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_reply_add': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'reply_amount': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'topic_type': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['groups']