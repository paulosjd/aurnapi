from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import field_for, ModelConverter
from app.models import Site

ma = Marshmallow()


class DataSchema(ma.Schema):
    # By default Schemas will unmarshal an input dict to an output dict whose keys are identical to field names.
    #owner = field_for(Site, 'site_code')
    #owner= ModelConverter
    o3 = ma.String(dump_to='ozone')
    time = ma.Method(serialize='standardize_time')


    def standardize_time(self, obj):
        std_time = '{}-{}-{} {}'.format(*obj.time.split(' ')[0].split('/')[::-1], obj.time.split(' ')[1])
        return std_time

    class Meta:
        additional = ('no2', 'so2', 'pm25', 'pm10')


data_schema = DataSchema()
many_data_schema = DataSchema(many=True)


class SiteSchema(ma.ModelSchema):
    data = ma.Nested(DataSchema)
    lat = ma.String(dump_to='latitude')
    long = ma.String(dump_to='longitude')
    environ = ma.String(dump_to='type')
    url = ma.URLFor('Site.site_detail', id='<id>')

    class Meta:
        model = Site
        exclude = ['id', 'hourly']

site_schema = SiteSchema()
sites_schema = SiteSchema(exclude=['defra_url', 'map_url'], many=True)

