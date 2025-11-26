from django.db import models


class Role(models.Model):
    role_nom = models.CharField(max_length=255)
    description_role = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.role_nom

class Direction(models.Model):
    direction_nom = models.CharField(max_length=255)

    def __str__(self):
        return self.direction_nom

class Service(models.Model):
    service_nom = models.CharField(max_length=255)
    id_direction = models.ForeignKey(Direction, on_delete=models.PROTECT)

    def __str__(self):
        return self.service_nom

class Utilisateur(models.Model):
    matricule = models.BigIntegerField()
    nom_utilisateur = models.CharField(max_length=255)
    prenom_utilisateur = models.CharField(max_length=255)
    mot_de_pass = models.CharField(max_length=255)
    login = models.CharField(max_length=255, unique=True)
    mail = models.EmailField()
    id_role = models.ForeignKey(Role, on_delete=models.PROTECT)
    id_service = models.ForeignKey(Service, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nom_utilisateur} {self.prenom_utilisateur}"

class LogAction(models.Model):
    action = models.CharField(max_length=255)
    ip_adresse = models.CharField(max_length=255)
    navigateur = models.CharField(max_length=255)
    date_action = models.DateTimeField(auto_now_add=True)
    id_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

class ValeurExtrait(models.Model):
    date_extraction = models.DateField()
    serdau = models.CharField(max_length=255)
    datedau = models.DateField()
    liquide = models.CharField(max_length=255)
    dateliquide = models.DateField()
    importateur = models.CharField(max_length=255)
    exportateur = models.CharField(max_length=255)
    pays_destinataire = models.CharField(max_length=255)
    description_article = models.CharField(max_length=255)
    poid_brut = models.DecimalField(max_digits=19, decimal_places=2)
    poid_net = models.DecimalField(max_digits=19, decimal_places=2)
    quantite = models.DecimalField(max_digits=19, decimal_places=2)
    unite = models.CharField(max_length=255)
    prix_article = models.DecimalField(max_digits=19, decimal_places=2)
    incoterm = models.CharField(max_length=255)
    id_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.PROTECT)

class Valeur(models.Model):
    codesh = models.CharField(max_length=255)
    descrip = models.CharField(max_length=255)
    unite = models.CharField(max_length=255)
    quantite = models.DecimalField(max_digits=19, decimal_places=2)
    pu_fact = models.DecimalField(max_digits=19, decimal_places=2)
    pu_redr = models.DecimalField(max_digits=19, decimal_places=2)
    methode = models.CharField(max_length=255)
    incoterm = models.CharField(max_length=255)
    devise = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    ref_fact = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    details_marchandises = models.CharField(max_length=255)
    poid_brut = models.DecimalField(max_digits=19, decimal_places=2)
    poid_net = models.DecimalField(max_digits=19, decimal_places=2)
    exportateur = models.CharField(max_length=255)
    pays_destinataire = models.CharField(max_length=255)
    importateur = models.CharField(max_length=255)
    conditionnement = models.CharField(max_length=255)
    image = models.BinaryField(null=True, blank=True)  # BLOB Oracle
    date_effet = models.DateField()
    id_extraction = models.ForeignKey(ValeurExtrait, null=True, blank=True, on_delete=models.SET_NULL)
    id_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.PROTECT)

class HistoriqueValeur(models.Model):
    champ_modifies = models.CharField(max_length=255)
    ancienne_valeur = models.CharField(max_length=255)
    nouvelle_valeur = models.CharField(max_length=255)
    date_modif = models.DateTimeField(auto_now_add=True)
    id_valeur = models.ForeignKey(Valeur, on_delete=models.CASCADE)
    id_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.PROTECT)

class Validation(models.Model):
    decision = models.CharField(max_length=255)
    date_validation = models.DateField(null=True, blank=True)
    id_extraction = models.ForeignKey(ValeurExtrait, on_delete=models.CASCADE)
    id_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.PROTECT)

