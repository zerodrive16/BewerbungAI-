class Data(models.Model):
    id = models.IntegerField(primary_key=True)

    # Personal Information
                                                        # Frontend Bedingungen in Eingabefelder (Alle müssen Pflichtfelder sein)
    surname = models.CharField(max_length=20)           # frontend sollte max. 20 char haben
    lastname = models.CharField(max_length=20)          # frontend sollte max. 20 char haben
    birthday = models.DateField()                       # frontend sollte nur Zeitformat (DateTimeFormat) haben
    address = models.CharField(max_length=50)           # frontend sollte max. 50 char haben
    city = models.CharField(max_length=50)              # frontend sollte max. 50 char haben
    zipcode = models.CharField(max_length=10)           # frontend sollte max. 10 char haben
    phone = models.CharField(max_length=17)             # frontend sollte max. 17 char haben
    email = models.EmailField()                         # frontend sollte email format im textfeld haben
    date = models.DateField()                           # frontend sollte aktuelle Zeit als "Default" Format haben, ansonsten DateTimeFormat
    experience = models.TextField(max_length=200)       # frontend sollte max. 200 char haben
    education = models.TextField(max_length=200)        # frontend sollte max. 200 char haben
    skills = models.TextField(max_length=200)           # frontend sollte max. 200 char haben
    interests = models.TextField(max_length=200)        # frontend sollte max. 200 char haben

    # Job Description Information
    companyname = models.CharField(max_length=25)       # frontend sollte max. 25 char haben
    companyaddress = models.CharField(max_length=50)    # frontend sollte max. 50 char haben
    companycity = models.CharField(max_length=50)       # frontend sollte max. 50 char haben
    companyzipcode = models.CharField(max_length=10)    # frontend sollte max. 10 char haben
    commpanystate = models.CharField(max_length=50)     # frontend sollte max. 50 char haben
    jobFieldName = models.CharField(max_length=50)      # frontend sollte max. 50 char haben
    jobFieldContent = models.TextField(max_length=400)  # frontend sollte max. 400 char haben

    # Generated JobApplication letter
    jobApplicationId = models.IntegerField()
    jobApplicationContent = models.TextField()

    def __str__(self):
        return self.jobFieldName