from shapely.geometry import Polygon as ShapelyPoly
from django.core.management.base import BaseCommand
from .models import Place, Polygon, GEOTYPE_CHOICES


def generate_perimeter(geo_choice):
    if geo_choice:
        for place in Place.objects.filter(geotype=geo_choice).order_by('name'):

            polygons = []
            for child in place.getChild():
                for polygon in child.getPolygons():
                    polygons.append(ShapelyPoly(polygon.getPoints()))

            pol = ''
            if polygons:
                pol = polygons[0]
                if len(polygons) > 1:
                    for polygon in polygons[1:]:
                        try:
                            pol = pol.union(polygon)
                        except:
                            pass
                for polygon in place.getPolygons():
                    polygon.delete()
            try:
                coords = ' '.join(['%s,%s' % (a[0], a[1]) for a in pol.exterior.coords])
                poly = Polygon()
                poly.place = place
                poly.limits = coords
                poly.save()
            except:
                try:
                    for pol2 in pol.geoms:
                        coords = ' '.join(['%s,%s' % (a[0], a[1]) for a in pol2.exterior.coords])
                        poly = Polygon()
                        poly.place = place
                        poly.limits = coords
                        poly.save()
                except:
                    print 'Oh no!!'

            print place.name

        return 'Ok'
    return 'Select geo type. Choices are: ' + ', '.join(['%d.- %s' % (a[0], a[1]) for a in GEOTYPE_CHOICES])


class Command(BaseCommand):
    help = "Redefine place perimeters"

    def add_arguments(self, parser):
        parser.add_argument('-gtype', '--geotype', type=int, help='Calculate this geo type places')

    def handle(self, *args, **options):
        generate_perimeter(geo_choice=options.get('geotype', None))
