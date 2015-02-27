from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # url(r'^image/(\d*)/(\d*)/(\d*).jpg', 'map.views.map_image'),
    url(r'^cosmos-grz/(\d+)/(\d+)/(\d+)/(\d+).jpg', 'map.views.map_cosmos_grz'),
    # url(r'^cosmos-urz/(\d*)/(\d*)/(\d*).jpg', 'map.views.map_cosmos_urz'),

    # Tiles
    url(r'^decals/(\d+)/(\d+)/(\d+)/(\d+).jpg', 'map.views.map_decals'),
    url(r'^decals-pr/(\d+)/(\d+)/(\d+)/(\d+).jpg', 'map.views.map_decals_pr'),
    url(r'^decals-model/(\d+)/(\d+)/(\d+)/(\d+).jpg', 'map.views.map_decals_model'),
    url(r'^decals-model-pr/(\d+)/(\d+)/(\d+)/(\d+).jpg', 'map.views.map_decals_model_pr'),
    url(r'^des-stripe82/(\d+)/(\d+)/(\d+)/(\d+).jpg', 'map.views.map_des_stripe82'),
    url(r'^des-pr/(\d+)/(\d+)/(\d+)/(\d+).jpg', 'map.views.map_des_pr'),

    # "EDR2"
    url(r'^decals-edr2/(\d+)/(\d+)/(\d+)/(\d+).jpg', 'map.views.map_decals_edr2'),
    url(r'^decals-model-edr2/(\d+)/(\d+)/(\d+)/(\d+).jpg', 'map.views.map_decals_model_edr2'),

    # EDR2 residuals
    url(r'^decals-resid-edr2/(\d+)/(\d+)/(\d+)/(\d+).jpg', 'map.views.map_decals_resid_edr2'),

    # EDR3
    url(r'^decals-edr3/(\d+)/(\d+)/(\d+)/(\d+).jpg', 'map.views.map_decals_edr3'),
    url(r'^decals-model-edr3/(\d+)/(\d+)/(\d+)/(\d+).jpg', 'map.views.map_decals_model_edr3'),

    # EDR3 residuals
    url(r'^decals-resid-edr3/(\d+)/(\d+)/(\d+)/(\d+).jpg', 'map.views.map_decals_resid_edr3'),


    # SFD dust map
    url(r'^sfd-tiles/(\d+)/(\d+)/(\d+)/(\d+).jpg', 'map.views.map_sfd'),

    ## Cutouts
    url(r'^cutouts/', 'map.views.cutouts', name='cutouts'),

    url(r'^cutout_panels/(?P<expnum>\d+)/(?P<extname>[NS]\d{1,2})/', 'map.views.cutout_panels', name='cutout_panels'),


    url(r'^cat_plot/', 'map.views.cat_plot', name='cat_plot'),

    # Catalogs
    url(r'^decals/(\d+)/(\d+)/(\d+)/(\d+).cat.json', 'map.views.cat_decals'),

    url(r'^decals-edr2/(\d+)/(\d+)/(\d+)/(\d+).cat.json', 'map.views.cat_decals_edr2'),
    url(r'^decals-edr3/(\d+)/(\d+)/(\d+)/(\d+).cat.json', 'map.views.cat_decals_edr3'),

    # brick list of polygons
    url(r'^bricks/', 'map.views.brick_list'),
    # CCD list of polygons
    url(r'^ccds/', 'map.views.ccd_list'),

    # Brick details
    url(r'^brick/(\d{4}[pm]\d{3})', 'map.views.brick_detail', name='brick_detail'),
    # this one is here to provide a name for the javascript to refer to.
    url(r'^brick/', 'map.views.nil', name='brick_detail_blank'),
    # CCD details
    url(r'^ccd/([\w-]+)', 'map.views.ccd_detail', name='ccd_detail'),
    # this one is here to provide a name for the javascript to refer to.
    url(r'^ccd/', 'map.views.nil', name='ccd_detail_blank'),

    # fall-through
    url(r'', 'map.views.index'),
    )
