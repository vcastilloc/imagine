from __future__ import unicode_literals

from django.db import models

class Router(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'cat':
            return 'cosmo'
        return None
    db_for_write = db_for_read

#########################################
# Below here generated by:
# python manage.py inspectdb --database cosmo > schema.py
#########################################

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class Bricks(models.Model):
    id = models.BigIntegerField(primary_key=True)
    brickname = models.CharField(max_length=-1, blank=True, null=True)
    brickid = models.IntegerField(blank=True, null=True)
    brickq = models.SmallIntegerField(blank=True, null=True)
    brickrow = models.IntegerField(blank=True, null=True)
    brickcol = models.IntegerField(blank=True, null=True)
    ra = models.FloatField(blank=True, null=True)
    dec = models.FloatField(blank=True, null=True)
    ra1 = models.FloatField(blank=True, null=True)
    ra2 = models.FloatField(blank=True, null=True)
    dec1 = models.FloatField(blank=True, null=True)
    dec2 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bricks'

class Tractor(models.Model):
    id = models.IntegerField(blank=True, null=True)
    brickid = models.IntegerField(blank=True, null=True)
    brickname = models.TextField(blank=True, null=True)
    objid = models.IntegerField(blank=True, null=True)
    brick_primary = models.SmallIntegerField(blank=True, null=True)
    blob = models.IntegerField(blank=True, null=True)
    ninblob = models.SmallIntegerField(blank=True, null=True)
    tycho2inblob = models.SmallIntegerField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    ra = models.FloatField(blank=True, null=True)
    ra_ivar = models.FloatField(blank=True, null=True)
    dec = models.FloatField(blank=True, null=True)
    dec_ivar = models.FloatField(blank=True, null=True)
    bx = models.FloatField(blank=True, null=True)
    by = models.FloatField(blank=True, null=True)
    bx0 = models.FloatField(blank=True, null=True)
    by0 = models.FloatField(blank=True, null=True)
    left_blob = models.SmallIntegerField(blank=True, null=True)
    out_of_bounds = models.SmallIntegerField(blank=True, null=True)
    dchisq_1 = models.FloatField(blank=True, null=True)
    dchisq_2 = models.FloatField(blank=True, null=True)
    dchisq_3 = models.FloatField(blank=True, null=True)
    dchisq_4 = models.FloatField(blank=True, null=True)
    dchisq_5 = models.FloatField(blank=True, null=True)
    ebv = models.FloatField(blank=True, null=True)
    cpu_source = models.FloatField(blank=True, null=True)
    cpu_blob = models.FloatField(blank=True, null=True)
    blob_width = models.SmallIntegerField(blank=True, null=True)
    blob_height = models.SmallIntegerField(blank=True, null=True)
    blob_npix = models.IntegerField(blank=True, null=True)
    blob_nimages = models.SmallIntegerField(blank=True, null=True)
    blob_totalpix = models.IntegerField(blank=True, null=True)
    decam_flux_1 = models.FloatField(blank=True, null=True)
    decam_flux_2 = models.FloatField(blank=True, null=True)
    decam_flux_3 = models.FloatField(blank=True, null=True)
    decam_flux_4 = models.FloatField(blank=True, null=True)
    decam_flux_5 = models.FloatField(blank=True, null=True)
    decam_flux_6 = models.FloatField(blank=True, null=True)
    decam_flux_ivar_1 = models.FloatField(blank=True, null=True)
    decam_flux_ivar_2 = models.FloatField(blank=True, null=True)
    decam_flux_ivar_3 = models.FloatField(blank=True, null=True)
    decam_flux_ivar_4 = models.FloatField(blank=True, null=True)
    decam_flux_ivar_5 = models.FloatField(blank=True, null=True)
    decam_flux_ivar_6 = models.FloatField(blank=True, null=True)
    decam_mw_transmission_1 = models.FloatField(blank=True, null=True)
    decam_mw_transmission_2 = models.FloatField(blank=True, null=True)
    decam_mw_transmission_3 = models.FloatField(blank=True, null=True)
    decam_mw_transmission_4 = models.FloatField(blank=True, null=True)
    decam_mw_transmission_5 = models.FloatField(blank=True, null=True)
    decam_mw_transmission_6 = models.FloatField(blank=True, null=True)
    decam_nobs_1 = models.SmallIntegerField(blank=True, null=True)
    decam_nobs_2 = models.SmallIntegerField(blank=True, null=True)
    decam_nobs_3 = models.SmallIntegerField(blank=True, null=True)
    decam_nobs_4 = models.SmallIntegerField(blank=True, null=True)
    decam_nobs_5 = models.SmallIntegerField(blank=True, null=True)
    decam_nobs_6 = models.SmallIntegerField(blank=True, null=True)
    decam_rchi2_1 = models.FloatField(blank=True, null=True)
    decam_rchi2_2 = models.FloatField(blank=True, null=True)
    decam_rchi2_3 = models.FloatField(blank=True, null=True)
    decam_rchi2_4 = models.FloatField(blank=True, null=True)
    decam_rchi2_5 = models.FloatField(blank=True, null=True)
    decam_rchi2_6 = models.FloatField(blank=True, null=True)
    decam_fracflux_1 = models.FloatField(blank=True, null=True)
    decam_fracflux_2 = models.FloatField(blank=True, null=True)
    decam_fracflux_3 = models.FloatField(blank=True, null=True)
    decam_fracflux_4 = models.FloatField(blank=True, null=True)
    decam_fracflux_5 = models.FloatField(blank=True, null=True)
    decam_fracflux_6 = models.FloatField(blank=True, null=True)
    decam_fracmasked_1 = models.FloatField(blank=True, null=True)
    decam_fracmasked_2 = models.FloatField(blank=True, null=True)
    decam_fracmasked_3 = models.FloatField(blank=True, null=True)
    decam_fracmasked_4 = models.FloatField(blank=True, null=True)
    decam_fracmasked_5 = models.FloatField(blank=True, null=True)
    decam_fracmasked_6 = models.FloatField(blank=True, null=True)
    decam_fracin_1 = models.FloatField(blank=True, null=True)
    decam_fracin_2 = models.FloatField(blank=True, null=True)
    decam_fracin_3 = models.FloatField(blank=True, null=True)
    decam_fracin_4 = models.FloatField(blank=True, null=True)
    decam_fracin_5 = models.FloatField(blank=True, null=True)
    decam_fracin_6 = models.FloatField(blank=True, null=True)
    decam_anymask_1 = models.SmallIntegerField(blank=True, null=True)
    decam_anymask_2 = models.SmallIntegerField(blank=True, null=True)
    decam_anymask_3 = models.SmallIntegerField(blank=True, null=True)
    decam_anymask_4 = models.SmallIntegerField(blank=True, null=True)
    decam_anymask_5 = models.SmallIntegerField(blank=True, null=True)
    decam_anymask_6 = models.SmallIntegerField(blank=True, null=True)
    decam_allmask_1 = models.SmallIntegerField(blank=True, null=True)
    decam_allmask_2 = models.SmallIntegerField(blank=True, null=True)
    decam_allmask_3 = models.SmallIntegerField(blank=True, null=True)
    decam_allmask_4 = models.SmallIntegerField(blank=True, null=True)
    decam_allmask_5 = models.SmallIntegerField(blank=True, null=True)
    decam_allmask_6 = models.SmallIntegerField(blank=True, null=True)
    decam_psfsize_1 = models.FloatField(blank=True, null=True)
    decam_psfsize_2 = models.FloatField(blank=True, null=True)
    decam_psfsize_3 = models.FloatField(blank=True, null=True)
    decam_psfsize_4 = models.FloatField(blank=True, null=True)
    decam_psfsize_5 = models.FloatField(blank=True, null=True)
    decam_psfsize_6 = models.FloatField(blank=True, null=True)
    fracdev = models.FloatField(blank=True, null=True)
    fracdev_ivar = models.FloatField(blank=True, null=True)
    shapeexp_r = models.FloatField(blank=True, null=True)
    shapeexp_r_ivar = models.FloatField(blank=True, null=True)
    shapeexp_e1 = models.FloatField(blank=True, null=True)
    shapeexp_e1_ivar = models.FloatField(blank=True, null=True)
    shapeexp_e2 = models.FloatField(blank=True, null=True)
    shapeexp_e2_ivar = models.FloatField(blank=True, null=True)
    shapedev_r = models.FloatField(blank=True, null=True)
    shapedev_r_ivar = models.FloatField(blank=True, null=True)
    shapedev_e1 = models.FloatField(blank=True, null=True)
    shapedev_e1_ivar = models.FloatField(blank=True, null=True)
    shapedev_e2 = models.FloatField(blank=True, null=True)
    shapedev_e2_ivar = models.FloatField(blank=True, null=True)
    decam_depth_1 = models.FloatField(blank=True, null=True)
    decam_depth_2 = models.FloatField(blank=True, null=True)
    decam_depth_3 = models.FloatField(blank=True, null=True)
    decam_depth_4 = models.FloatField(blank=True, null=True)
    decam_depth_5 = models.FloatField(blank=True, null=True)
    decam_depth_6 = models.FloatField(blank=True, null=True)
    decam_galdepth_1 = models.FloatField(blank=True, null=True)
    decam_galdepth_2 = models.FloatField(blank=True, null=True)
    decam_galdepth_3 = models.FloatField(blank=True, null=True)
    decam_galdepth_4 = models.FloatField(blank=True, null=True)
    decam_galdepth_5 = models.FloatField(blank=True, null=True)
    decam_galdepth_6 = models.FloatField(blank=True, null=True)
    htm_index = models.BigIntegerField(blank=True, null=True)
    u = models.FloatField(blank=True, null=True)
    g = models.FloatField(blank=True, null=True)
    r = models.FloatField(blank=True, null=True)
    i = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    u_g = models.FloatField(blank=True, null=True)
    g_r = models.FloatField(blank=True, null=True)
    r_i = models.FloatField(blank=True, null=True)
    i_z = models.FloatField(blank=True, null=True)
    z_y = models.FloatField(blank=True, null=True)
    w1 = models.FloatField(blank=True, null=True)
    w2 = models.FloatField(blank=True, null=True)
    w3 = models.FloatField(blank=True, null=True)
    w4 = models.FloatField(blank=True, null=True)
    preview = models.TextField(blank=True, null=True)
    camera = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tractor'


class Wise(models.Model):
    id = models.IntegerField(primary_key=True, blank=True, null=True)
    brickid = models.IntegerField(blank=True, null=True)
    objid = models.IntegerField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    w1 = models.FloatField(blank=True, null=True)
    w2 = models.FloatField(blank=True, null=True)
    w3 = models.FloatField(blank=True, null=True)
    w4 = models.FloatField(blank=True, null=True)
    wise_flux_1 = models.FloatField(blank=True, null=True)
    wise_flux_2 = models.FloatField(blank=True, null=True)
    wise_flux_3 = models.FloatField(blank=True, null=True)
    wise_flux_4 = models.FloatField(blank=True, null=True)
    wise_flux_ivar_1 = models.FloatField(blank=True, null=True)
    wise_flux_ivar_2 = models.FloatField(blank=True, null=True)
    wise_flux_ivar_3 = models.FloatField(blank=True, null=True)
    wise_flux_ivar_4 = models.FloatField(blank=True, null=True)
    wise_mw_transmission_1 = models.FloatField(blank=True, null=True)
    wise_mw_transmission_2 = models.FloatField(blank=True, null=True)
    wise_mw_transmission_3 = models.FloatField(blank=True, null=True)
    wise_mw_transmission_4 = models.FloatField(blank=True, null=True)
    wise_nobs_1 = models.SmallIntegerField(blank=True, null=True)
    wise_nobs_2 = models.SmallIntegerField(blank=True, null=True)
    wise_nobs_3 = models.SmallIntegerField(blank=True, null=True)
    wise_nobs_4 = models.SmallIntegerField(blank=True, null=True)
    wise_fracflux_1 = models.FloatField(blank=True, null=True)
    wise_fracflux_2 = models.FloatField(blank=True, null=True)
    wise_fracflux_3 = models.FloatField(blank=True, null=True)
    wise_fracflux_4 = models.FloatField(blank=True, null=True)
    wise_rchi2_1 = models.FloatField(blank=True, null=True)
    wise_rchi2_2 = models.FloatField(blank=True, null=True)
    wise_rchi2_3 = models.FloatField(blank=True, null=True)
    wise_rchi2_4 = models.FloatField(blank=True, null=True)
    wise_lc_flux_1_1 = models.FloatField(blank=True, null=True)
    wise_lc_flux_2_1 = models.FloatField(blank=True, null=True)
    wise_lc_flux_3_1 = models.FloatField(blank=True, null=True)
    wise_lc_flux_4_1 = models.FloatField(blank=True, null=True)
    wise_lc_flux_5_1 = models.FloatField(blank=True, null=True)
    wise_lc_flux_1_2 = models.FloatField(blank=True, null=True)
    wise_lc_flux_2_2 = models.FloatField(blank=True, null=True)
    wise_lc_flux_3_2 = models.FloatField(blank=True, null=True)
    wise_lc_flux_4_2 = models.FloatField(blank=True, null=True)
    wise_lc_flux_5_2 = models.FloatField(blank=True, null=True)
    wise_lc_flux_ivar_1_1 = models.FloatField(blank=True, null=True)
    wise_lc_flux_ivar_2_1 = models.FloatField(blank=True, null=True)
    wise_lc_flux_ivar_3_1 = models.FloatField(blank=True, null=True)
    wise_lc_flux_ivar_4_1 = models.FloatField(blank=True, null=True)
    wise_lc_flux_ivar_5_1 = models.FloatField(blank=True, null=True)
    wise_lc_flux_ivar_1_2 = models.FloatField(blank=True, null=True)
    wise_lc_flux_ivar_2_2 = models.FloatField(blank=True, null=True)
    wise_lc_flux_ivar_3_2 = models.FloatField(blank=True, null=True)
    wise_lc_flux_ivar_4_2 = models.FloatField(blank=True, null=True)
    wise_lc_flux_ivar_5_2 = models.FloatField(blank=True, null=True)
    wise_lc_nobs_1_1 = models.SmallIntegerField(blank=True, null=True)
    wise_lc_nobs_2_1 = models.SmallIntegerField(blank=True, null=True)
    wise_lc_nobs_3_1 = models.SmallIntegerField(blank=True, null=True)
    wise_lc_nobs_4_1 = models.SmallIntegerField(blank=True, null=True)
    wise_lc_nobs_5_1 = models.SmallIntegerField(blank=True, null=True)
    wise_lc_nobs_1_2 = models.SmallIntegerField(blank=True, null=True)
    wise_lc_nobs_2_2 = models.SmallIntegerField(blank=True, null=True)
    wise_lc_nobs_3_2 = models.SmallIntegerField(blank=True, null=True)
    wise_lc_nobs_4_2 = models.SmallIntegerField(blank=True, null=True)
    wise_lc_nobs_5_2 = models.SmallIntegerField(blank=True, null=True)
    wise_lc_fracflux_1_1 = models.FloatField(blank=True, null=True)
    wise_lc_fracflux_2_1 = models.FloatField(blank=True, null=True)
    wise_lc_fracflux_3_1 = models.FloatField(blank=True, null=True)
    wise_lc_fracflux_4_1 = models.FloatField(blank=True, null=True)
    wise_lc_fracflux_5_1 = models.FloatField(blank=True, null=True)
    wise_lc_fracflux_1_2 = models.FloatField(blank=True, null=True)
    wise_lc_fracflux_2_2 = models.FloatField(blank=True, null=True)
    wise_lc_fracflux_3_2 = models.FloatField(blank=True, null=True)
    wise_lc_fracflux_4_2 = models.FloatField(blank=True, null=True)
    wise_lc_fracflux_5_2 = models.FloatField(blank=True, null=True)
    wise_lc_rchi2_1_1 = models.FloatField(blank=True, null=True)
    wise_lc_rchi2_2_1 = models.FloatField(blank=True, null=True)
    wise_lc_rchi2_3_1 = models.FloatField(blank=True, null=True)
    wise_lc_rchi2_4_1 = models.FloatField(blank=True, null=True)
    wise_lc_rchi2_5_1 = models.FloatField(blank=True, null=True)
    wise_lc_rchi2_1_2 = models.FloatField(blank=True, null=True)
    wise_lc_rchi2_2_2 = models.FloatField(blank=True, null=True)
    wise_lc_rchi2_3_2 = models.FloatField(blank=True, null=True)
    wise_lc_rchi2_4_2 = models.FloatField(blank=True, null=True)
    wise_lc_rchi2_5_2 = models.FloatField(blank=True, null=True)
    wise_lc_mjd_1_1 = models.FloatField(blank=True, null=True)
    wise_lc_mjd_2_1 = models.FloatField(blank=True, null=True)
    wise_lc_mjd_3_1 = models.FloatField(blank=True, null=True)
    wise_lc_mjd_4_1 = models.FloatField(blank=True, null=True)
    wise_lc_mjd_5_1 = models.FloatField(blank=True, null=True)
    wise_lc_mjd_1_2 = models.FloatField(blank=True, null=True)
    wise_lc_mjd_2_2 = models.FloatField(blank=True, null=True)
    wise_lc_mjd_3_2 = models.FloatField(blank=True, null=True)
    wise_lc_mjd_4_2 = models.FloatField(blank=True, null=True)
    wise_lc_mjd_5_2 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wise'
