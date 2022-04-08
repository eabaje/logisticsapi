from django.db import models

# Create your models here.
class Assigndrivers(models.Model):
    assignid = models.UUIDField(db_column='AssignId', primary_key=True)  # Field name made lowercase.
    assigned = models.BooleanField(db_column='Assigned', blank=True, null=True)  # Field name made lowercase.
    assigneddate = models.DateTimeField(db_column='AssignedDate', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    driverid = models.ForeignKey('Drivers', models.DO_NOTHING, db_column='DriverId', blank=True, null=True)  # Field name made lowercase.
    vehicleid = models.ForeignKey('Vehicles', models.DO_NOTHING, db_column='VehicleId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AssignDrivers'
        unique_together = (('driverid', 'vehicleid'),)


class Assignshipments(models.Model):
    assignshipmentid = models.UUIDField(db_column='AssignShipmentId', primary_key=True)  # Field name made lowercase.
    isassigned = models.BooleanField(db_column='IsAssigned', blank=True, null=True)  # Field name made lowercase.
    assigneddate = models.DateTimeField(db_column='AssignedDate', blank=True, null=True)  # Field name made lowercase.
    assignedto = models.CharField(db_column='AssignedTo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AssignShipments'


class Carriers(models.Model):
    carrierid = models.UUIDField(db_column='CarrierId', primary_key=True)  # Field name made lowercase.
    carriertype = models.CharField(db_column='CarrierType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fleettype = models.CharField(db_column='FleetType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fleetnumber = models.CharField(db_column='FleetNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    aboutus = models.CharField(db_column='AboutUs', max_length=255, blank=True, null=True)  # Field name made lowercase.
    servicedescription = models.CharField(db_column='ServiceDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating', blank=True, null=True)  # Field name made lowercase.
    licensed = models.BooleanField(db_column='Licensed', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    companyid = models.ForeignKey('Companys', models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Carriers'


class Companys(models.Model):
    companyid = models.AutoField(db_column='CompanyId', primary_key=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contactemail = models.CharField(db_column='ContactEmail', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contactphone = models.CharField(db_column='ContactPhone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=255, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=255, blank=True, null=True)  # Field name made lowercase.
    companytype = models.CharField(db_column='CompanyType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    specilaization = models.CharField(db_column='Specilaization', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Companys'


class Drivers(models.Model):
    driverid = models.UUIDField(db_column='DriverId', primary_key=True)  # Field name made lowercase.
    drivername = models.CharField(db_column='DriverName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    secondaryphone = models.CharField(db_column='SecondaryPhone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=255, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=255, blank=True, null=True)  # Field name made lowercase.
    picurl = models.CharField(db_column='PicUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    licensed = models.BooleanField(db_column='Licensed', blank=True, null=True)  # Field name made lowercase.
    licenseurl = models.CharField(db_column='LicenseUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating', blank=True, null=True)  # Field name made lowercase.
    driverdocs = models.CharField(db_column='DriverDocs', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    companyid = models.ForeignKey('Companys', models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Drivers'


class Insurances(models.Model):
    insuranceid = models.AutoField(db_column='InsuranceId', primary_key=True)  # Field name made lowercase.
    shipmentid = models.CharField(db_column='ShipmentId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    companyid = models.IntegerField(db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    insurancename = models.CharField(db_column='InsuranceName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    insurancetype = models.CharField(db_column='InsuranceType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    insurer = models.CharField(db_column='Insurer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    insurerancedoc = models.CharField(db_column='InsureranceDoc', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Insurances'


class Medias(models.Model):
    mediaid = models.AutoField(db_column='MediaId', primary_key=True)  # Field name made lowercase.
    refid = models.CharField(db_column='RefId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(max_length=255, blank=True, null=True)
    uploaddate = models.DateField(db_column='UploadDate', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    filename = models.TextField(db_column='FileName', blank=True, null=True)  # Field name made lowercase.
    filetype = models.TextField(db_column='FileType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Medias'


class Orders(models.Model):
    orderid = models.CharField(db_column='OrderId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    totalprice = models.DecimalField(db_column='TotalPrice', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.      
    paymentsessionid = models.CharField(db_column='PaymentSessionId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ispaymentsuccessful = models.BooleanField(db_column='IsPaymentSuccessful', blank=True, null=True)  # Field name made lowercase.
    orderstatus = models.CharField(db_column='OrderStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    orderdate = models.DateTimeField(db_column='OrderDate', blank=True, null=True)  # Field name made lowercase.
    paymentmethod = models.CharField(db_column='PaymentMethod', max_length=255, blank=True, null=True)  # Field name made lowercase.
    currency = models.CharField(db_column='Currency', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Orders'


class Payments(models.Model):
    paymentid = models.AutoField(db_column='PaymentId', primary_key=True)  # Field name made lowercase.
    totalprice = models.DecimalField(db_column='TotalPrice', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.      
    paymentsessionid = models.CharField(db_column='PaymentSessionId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    referenceid = models.CharField(db_column='ReferenceId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    orderstatus = models.CharField(db_column='OrderStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    paymentmethod = models.CharField(db_column='PaymentMethod', max_length=255, blank=True, null=True)  # Field name made lowercase.
    paymentdate = models.DateField(db_column='PaymentDate', blank=True, null=True)  # Field name made lowercase.
    currency = models.CharField(db_column='Currency', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Payments'




class Shipments(models.Model):
    shipmentid = models.UUIDField(db_column='ShipmentId', primary_key=True)  # Field name made lowercase.
    loadcategory = models.CharField(db_column='LoadCategory', max_length=255, blank=True, null=True)  # Field name made lowercase.
    loadtype = models.CharField(db_column='LoadType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    loadweight = models.DecimalField(db_column='LoadWeight', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    loadunit = models.CharField(db_column='LoadUnit', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qty = models.IntegerField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pickupcountry = models.CharField(db_column='PickUpCountry', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pickupregion = models.CharField(db_column='PickUpRegion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pickuplocation = models.CharField(db_column='PickUpLocation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    deliverycountry = models.CharField(db_column='DeliveryCountry', max_length=255, blank=True, null=True)  # Field name made lowercase.
    deliveryregion = models.CharField(db_column='DeliveryRegion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    deliverylocation = models.CharField(db_column='DeliveryLocation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    expectedpickupdate = models.DateField(db_column='ExpectedPickUpDate', blank=True, null=True)  # Field name made lowercase.
    expecteddeliverydate = models.DateField(db_column='ExpectedDeliveryDate', blank=True, null=True)  # Field name made lowercase.
    requestforshipment = models.CharField(db_column='RequestForShipment', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shipmentrequestprice = models.DecimalField(db_column='ShipmentRequestPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    deliverycontactname = models.CharField(db_column='DeliveryContactName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    deliverycontactphone = models.CharField(db_column='DeliveryContactPhone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    deliveryemail = models.CharField(db_column='DeliveryEmail', max_length=255, blank=True, null=True)  # Field name made lowercase.
    assignedshipment = models.BooleanField(db_column='AssignedShipment', blank=True, null=True)  # Field name made lowercase.
    shipmentdate = models.DateField(db_column='ShipmentDate', blank=True, null=True)  # Field name made lowercase.
    shipmentdocs = models.CharField(db_column='ShipmentDocs', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shipmentstatus = models.CharField(db_column='ShipmentStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    companyid = models.ForeignKey('Companys', models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Shipments'


class Shipmentsinteresteds(models.Model):
    shipmentinterestid = models.UUIDField(db_column='ShipmentInterestId', primary_key=True)  # Field name made lowercase.
    carrierid = models.CharField(db_column='CarrierId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isinterested = models.BooleanField(db_column='IsInterested', blank=True, null=True)  # Field name made lowercase.
    interestdate = models.DateField(db_column='InterestDate', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    shipmentid = models.ForeignKey('Shipments', models.DO_NOTHING, db_column='ShipmentId', blank=True, null=True)  # Field name made lowercase.
    driverid = models.ForeignKey('Drivers', models.DO_NOTHING, db_column='DriverId', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ShipmentsInteresteds'


class Subscriptions(models.Model):
    subscribeid = models.AutoField(db_column='SubscribeId', primary_key=True)  # Field name made lowercase.
    subscriptiontype = models.CharField(db_column='SubscriptionType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    subscriptionname = models.CharField(db_column='SubscriptionName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    duration = models.IntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Subscriptions'


class Tracks(models.Model):
    trackid = models.AutoField(db_column='TrackId', primary_key=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tracknote = models.CharField(db_column='TrackNote', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    shipmentid = models.ForeignKey('Shipments', models.DO_NOTHING, db_column='ShipmentId', blank=True, null=True)  # Field name made lowercase.
    tripid = models.ForeignKey('Trips', models.DO_NOTHING, db_column='TripId', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tracks'


class Trips(models.Model):
    tripid = models.UUIDField(db_column='TripId', primary_key=True)  # Field name made lowercase.
    pickuplocation = models.CharField(db_column='PickUpLocation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    deliverylocation = models.CharField(db_column='DeliveryLocation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pickupdate = models.DateField(db_column='PickUpDate', blank=True, null=True)  # Field name made lowercase.
    duration = models.CharField(db_column='Duration', max_length=255, blank=True, null=True)  # Field name made lowercase.
    deliverydate = models.DateField(db_column='DeliveryDate', blank=True, null=True)  # Field name made lowercase.
    drivernote = models.CharField(db_column='DriverNote', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating', blank=True, null=True)  # Field name made lowercase.
    review = models.CharField(db_column='Review', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    vehicleid = models.ForeignKey('Vehicles', models.DO_NOTHING, db_column='VehicleId', blank=True, null=True)  # Field name made lowercase.
    driverid = models.ForeignKey('Drivers', models.DO_NOTHING, db_column='DriverId', blank=True, null=True)  # Field name made lowercase.
    shipmentid = models.ForeignKey('Shipments', models.DO_NOTHING, db_column='ShipmentId', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Trips'


class Roles(models.Model):
    roleid = models.UUIDField(db_column='RoleId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Roles'


class Userroles(models.Model):
    userroleid = models.UUIDField(db_column='UserRoleId', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    roleid = models.ForeignKey('Roles', models.DO_NOTHING, db_column='RoleId', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserRoles'
        unique_together = (('userid', 'roleid'),)


class Usersubscriptions(models.Model):
    usersubscriptionid = models.AutoField(db_column='UserSubscriptionId', primary_key=True)  # Field name made lowercase.
    subscriptionname = models.CharField(db_column='SubscriptionName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    subscribeid = models.ForeignKey('Subscriptions', models.DO_NOTHING, db_column='SubscribeId', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserSubscriptions'


class Users(models.Model):
    userid = models.UUIDField(db_column='UserId', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=255, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=255, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255, blank=True, null=True)  # Field name made lowercase.
    userpicurl = models.CharField(db_column='UserPicUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    token = models.CharField(db_column='Token', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isactivated = models.BooleanField(db_column='IsActivated', blank=True, null=True)  # Field name made lowercase.
    acceptterms = models.BooleanField(db_column='AcceptTerms', blank=True, null=True)  # Field name made lowercase.
    logincount = models.IntegerField(db_column='LoginCount', blank=True, null=True)  # Field name made lowercase.
    paymentmethod = models.CharField(db_column='PaymentMethod', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    companyid = models.ForeignKey('Companys', models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    currency = models.TextField(db_column='Currency', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Users'


class Vehicles(models.Model):
    vehicleid = models.UUIDField(db_column='VehicleId', primary_key=True)  # Field name made lowercase.
    vehicletype = models.CharField(db_column='VehicleType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vehiclenumber = models.CharField(db_column='VehicleNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vehiclemake = models.CharField(db_column='VehicleMake', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vehiclecolor = models.CharField(db_column='VehicleColor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vehiclemodel = models.CharField(db_column='VehicleModel', max_length=255, blank=True, null=True)  # Field name made lowercase.
    licenseplate = models.CharField(db_column='LicensePlate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vehiclemodelyear = models.DateField(db_column='VehicleModelYear', blank=True, null=True)  # Field name made lowercase.
    purchaseyear = models.DateField(db_column='PurchaseYear', blank=True, null=True)  # Field name made lowercase.
    insured = models.BooleanField(db_column='Insured', blank=True, null=True)  # Field name made lowercase.
    picurl = models.CharField(db_column='PicUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vehicledocs = models.CharField(db_column='VehicleDocs', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    carrierid = models.ForeignKey('Carriers', models.DO_NOTHING, db_column='CarrierId', blank=True, null=True)  # Field name made lowercase.
    companyid = models.ForeignKey('Companys', models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Vehicles'

