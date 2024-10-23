from django.db import models
from django.db.models.signals import pre_save
from .signals import encode_limits
from django.utils.translation import ugettext as _

GEOTYPE_CHOICES = ((0, _('Consortium')), (1, _('District / Neighborhood')), (2, _('Town / City')), (3, _('Valley / Region')), (4, _('Province')), (5, _('State')), (6, _('Country')))


class Place(models.Model):
    code = models.CharField(verbose_name=_("Code"), max_length=255)
    local_lang_name = models.CharField(verbose_name=_("Local language name"), max_length=255)
    country_lang_name = models.CharField(verbose_name=_("Country language name"), max_length=255, null=True, blank=True)
    official_name = models.CharField(verbose_name=_("Official name"), max_length=255, null=True, blank=True)
    lang_academ_name = models.CharField(verbose_name=_("Language Academy name"), max_length=255, null=True, blank=True)

    slug = models.SlugField(unique=True, db_index=True)
    geotype = models.IntegerField(verbose_name=_("Type"), default=0, db_index=True, choices=GEOTYPE_CHOICES)
    notes = models.TextField(verbose_name=_("Notes"), null=True, blank=True)
    lat = models.FloatField(verbose_name=_("Latitude"), default=0, null=True, blank=True)
    lon = models.FloatField(verbose_name=_("Longitude"), default=0, null=True, blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child_set', on_delete=models.SET_NULL, verbose_name=_("Parent"))

    added = models.DateField(_('Added'), auto_now_add=True)
    modified = models.DateField(_('Modified'), auto_now=True)

    def countChild(self):
        return self.child_set.all().count()

    def getChild(self):
        return self.child_set.all().order_by('local_lang_name')

    def getPolygons(self):
        return self.polygon_set.all()

    def countPolygons(self):
        return self.polygon_set.all().count()
    countPolygons.short_description = _('Polygons')

    def countPolygonsEx(self):
        return self.polygon_set.filter(is_exterior=True).count()
    countPolygonsEx.short_description = _('Exterior Polygons')

    def countPolygonsIn(self):
        return self.polygon_set.filter(is_exterior=False).count()
    countPolygonsIn.short_description = _('Interior Polygons')

    def countPoints(self):
        total = 0
        for polygon in self.getPolygons():
            total = total + polygon.countPoints()
        return total
    countPoints.short_description = _('Points')

    class Meta:
        verbose_name = _('Place')
        verbose_name_plural = _('Places')
        ordering = ('local_lang_name',)

    def __unicode__(self):
        return u'%s' % (self.local_lang_name)


class Polygon(models.Model):
    place = models.ForeignKey(Place, verbose_name=_("Place"))

    limits = models.TextField(verbose_name=_("Limits"), null=True, blank=True)
    is_visible = models.BooleanField(verbose_name=_("Is visible"), default=1)
    is_exterior = models.BooleanField(verbose_name=_("Is exterior"), default=1)

    encode_points = models.TextField(verbose_name=_("Encode points"), null=True, blank=True)
    encode_levels = models.TextField(verbose_name=_("Encode levels"), null=True, blank=True)
    encode_zoomfactor = models.CharField(verbose_name=_("Encode zoom factor"), max_length=20, blank=True, null=True)
    encode_numlevels = models.CharField(verbose_name=_("Encode number levels"), max_length=20, blank=True, null=True)

    added = models.DateField(_('Added'), auto_now_add=True)
    modified = models.DateField(_('Modified'), auto_now=True)

    def getPoints(self):
        return tuple([tuple([float(b) for b in a.split(',')]) for a in self.limits.split(' ')])

    def countPoints(self):
        return len(self.limits.split(' '))

    class Meta:
        verbose_name = _('Polygon')
        verbose_name_plural = _('Polygons')

    def __unicode__(self):
        return u'%d' % self.pk

pre_save.connect(encode_limits, sender=Polygon)
