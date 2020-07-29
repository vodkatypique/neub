# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


def upload_to_faces(instance, filename):
    return "faces/" + filename


class HmcPlayers(models.Model):
    idu = models.PositiveIntegerField(db_column='IDU', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(max_length=255)
    poste = models.CharField(max_length=255)
    poste2 = models.CharField(max_length=255)
    club = models.CharField(max_length=255, blank=True, null=True)
    nat = models.CharField(max_length=6)
    ca = models.PositiveSmallIntegerField(db_column='CA')  # Field name made lowercase.
    pa = models.PositiveSmallIntegerField(db_column='PA')  # Field name made lowercase.
    niveausaison = models.PositiveSmallIntegerField(blank=True, null=True)
    age = models.PositiveSmallIntegerField()
    taille = models.CharField(max_length=50)
    poids = models.CharField(max_length=50)
    pied = models.CharField(max_length=255)
    personnalite = models.CharField(max_length=255)
    valeur = models.PositiveSmallIntegerField()
    valeursaison = models.PositiveSmallIntegerField(blank=True, null=True)
    contrat = models.PositiveSmallIntegerField(null=True)
    fincontrat = models.BooleanField(null=True)
    blessure = models.CharField(max_length=255, blank=True, null=True)
    dblessure = models.CharField(max_length=255, blank=True, null=True)
    newgen = models.IntegerField()
    face = models.ImageField(null=True, upload_to=upload_to_faces)
    box = models.PositiveSmallIntegerField()
    com = models.PositiveSmallIntegerField()
    deg = models.PositiveSmallIntegerField()
    detg = models.PositiveSmallIntegerField()
    pbl = models.PositiveSmallIntegerField()
    ref = models.PositiveSmallIntegerField()
    ucu = models.PositiveSmallIntegerField()
    tsp = models.PositiveSmallIntegerField()
    srf = models.PositiveSmallIntegerField()
    rel = models.PositiveSmallIntegerField()
    exc = models.PositiveSmallIntegerField()
    ant = models.PositiveSmallIntegerField()
    pas = models.PositiveSmallIntegerField()
    tet = models.PositiveSmallIntegerField()
    pen = models.PositiveSmallIntegerField()
    tir = models.PositiveSmallIntegerField()
    tec = models.PositiveSmallIntegerField()
    tlg = models.PositiveSmallIntegerField()
    mar = models.PositiveSmallIntegerField()
    tcl = models.PositiveSmallIntegerField()
    cen = models.PositiveSmallIntegerField()
    cor = models.PositiveSmallIntegerField()
    cf = models.PositiveSmallIntegerField()
    drb = models.PositiveSmallIntegerField()
    fin = models.PositiveSmallIntegerField()
    ctr = models.PositiveSmallIntegerField()
    apl = models.PositiveSmallIntegerField()
    agr = models.PositiveSmallIntegerField()
    col = models.PositiveSmallIntegerField()
    ctn = models.PositiveSmallIntegerField()
    crg = models.PositiveSmallIntegerField()
    dec = models.PositiveSmallIntegerField()
    dtm = models.PositiveSmallIntegerField()
    ins = models.PositiveSmallIntegerField()
    ldr = models.PositiveSmallIntegerField()
    pla = models.PositiveSmallIntegerField()
    sgf = models.PositiveSmallIntegerField()
    vis = models.PositiveSmallIntegerField()
    vol = models.PositiveSmallIntegerField()
    acc = models.PositiveSmallIntegerField()
    phy = models.PositiveSmallIntegerField()
    vit = models.PositiveSmallIntegerField()
    agi = models.PositiveSmallIntegerField()
    equ = models.PositiveSmallIntegerField()
    pui = models.PositiveSmallIntegerField()
    end = models.PositiveSmallIntegerField()
    det = models.PositiveSmallIntegerField()
    ble = models.PositiveSmallIntegerField()
    reg = models.PositiveSmallIntegerField()
    mat = models.PositiveSmallIntegerField()
    sapp = models.CharField(max_length=50, null=True)
    sbut = models.PositiveSmallIntegerField(null=True)
    spd = models.PositiveSmallIntegerField(null=True)
    shdm = models.PositiveSmallIntegerField(null=True)
    smoy = models.FloatField(null=True)
    moral = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.nom

    class Meta:
        db_table = 'hmc_players'


class HmcClassedraft(models.Model):
    idu = models.IntegerField(db_column='IDU', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=500)
    poste = models.CharField(max_length=500)
    ca = models.IntegerField(db_column='CA')  # Field name made lowercase.
    pa = models.IntegerField(db_column='PA')  # Field name made lowercase.
    nat = models.CharField(max_length=500)
    age = models.IntegerField()
    taille = models.CharField(max_length=50)
    poids = models.CharField(max_length=50)
    pfort = models.CharField(max_length=500)
    club = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'hmc_classedraft'


def upload_to(instance, filename):
    return "screens/"+str(instance.club)+"/"+filename


class HmcClubs(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    pseudo = models.CharField(max_length=500)
    club = models.CharField(max_length=500)
    conference = models.CharField(max_length=500, null=True)
    logo = models.CharField(max_length=500)
    classement = models.IntegerField(null=True)
    massebudget = models.IntegerField()
    massebudgetactuelle = models.IntegerField()
    cap = models.IntegerField()
    pointaction = models.IntegerField()
    formation = models.ForeignKey('HmcFormations', on_delete=models.DO_NOTHING, db_column='formation')
    mentality = models.CharField(max_length=50)
    consign = models.ForeignKey('HmcTactics', on_delete=models.DO_NOTHING, db_column='consign')
    compo = models.CharField(max_length=1000)
    edited_at = models.DateTimeField(blank=True, null=True)
    screenclub = models.ImageField(max_length=500, upload_to=upload_to)
    screeneffectif = models.ImageField(max_length=500, upload_to=upload_to)
    screencalendrier = models.ImageField(max_length=500, upload_to=upload_to)
    screencompet = models.ImageField(max_length=500, upload_to=upload_to)

    def __str__(self):
        return self.club

    class Meta:
        db_table = 'hmc_clubs'


class HmcFormations(models.Model):
    idu = models.AutoField(db_column='IDU', primary_key=True)  # Field name made lowercase.
    formation = models.CharField(max_length=255)
    postes = models.CharField(max_length=1000, blank=True, null=True)
    type = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.formation

    class Meta:
        db_table = 'hmc_formations'


class HmcRoles(models.Model):
    idu = models.AutoField(db_column='IDU', primary_key=True)  # Field name made lowercase.
    poste = models.CharField(max_length=255)
    roles = models.CharField(max_length=1000)

    def __str__(self):
        return self.poste

    class Meta:
        db_table = 'hmc_roles'


class HmcTactics(models.Model):
    idu = models.AutoField(db_column='IDU', primary_key=True)  # Field name made lowercase.
    tactique = models.CharField(max_length=255)
    cons1 = models.CharField(max_length=1000)
    cons2 = models.CharField(max_length=1000)
    cons3 = models.CharField(max_length=1000)

    def __str__(self):
        return self.tactique

    class Meta:
        db_table = 'hmc_tactics'
