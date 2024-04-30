from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from colorfield.fields import ColorField
from django.utils.timezone import now


class Domain(models.Model):
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=64, unique=True)
    CreateAt = models.DateTimeField (default=now)
    class Meta:
        verbose_name = "دامنه"
        verbose_name_plural = "دامنه ها"
    def __str__(self):
        return self.name+ '(' + self.domain+')'


# برای اندازه حجم ویدیو اضافه شده است
def validate_file_size(value):
    filesize = value.size
    if filesize > 400 * 1024 * 1024:
        raise ValidationError(_('مگه جنگه؟!!! فایل بیششتر از 400 مگابایت نمیشه اپلود کرد')) 
    
#Informations
class Information (models.Model) :
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)
    CreateAt = models.DateTimeField (default=now)
    Logo1 = models.ImageField (upload_to='static/images/' , blank=True, null=True)
    Logo2 = models.ImageField (upload_to='static/images/' , blank=True, null=True)
    Logotext = models.ImageField (upload_to='static/images/' , blank=True, null=True)
    Name = models.CharField (max_length=255)
    Telephone1 = models.CharField (max_length=255)
    Telephone2 = models.CharField (max_length=255)
    Fax = models.CharField (max_length=255)
    Address = models.CharField (max_length=255)
    NationalID = models.CharField (max_length=12)
    AboutUs = models.TextField ()
    Theme = models.IntegerField (blank=True, null=True)
    MapLink = models.CharField (max_length=255)
    Email = models.EmailField (max_length=255,blank=True, null=True)
    instagram = models.CharField (max_length=255,blank=True, null=True)
    telegram =models.CharField (max_length=255,blank=True, null=True)
    tweeter = models.CharField (max_length=255,blank=True, null=True)
    Cataloge = models.CharField (max_length=255,blank=True, null=True)
    Description = models.CharField (max_length=500 , blank=True, null=True)
    Keywords = models.CharField (max_length=500 ,blank=True, null=True)
    Admin = models.CharField (max_length=255)
    Date = models.CharField (max_length=255)
    FieldOfActivity = models.CharField (max_length=255)
    TypeOfCompany = models.CharField (max_length=255)
    class Meta:
        verbose_name = "Informations"
        verbose_name_plural = "Informations"
    def __str__(self):
        return str(self.Domain)

#Branchs
class BranchsOfCompany (models.Model) :
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)
    CreateAt = models.DateTimeField (default=now)
    Province = models.CharField (max_length=100)
    City = models.CharField (max_length=100)
    Address = models.CharField (max_length=255)
    MapLink = models.CharField (max_length=255)
    Telephone = models.CharField (max_length=20)
    Code = models.CharField (max_length=5)
    Types = models.CharField (max_length=100)
    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branchs"
    def __str__(self):
        return str(self.Domain) + ' [' +self.Address+']'

#Business Partners
class BusinessPartners (models.Model) :
    Domain =  models.ForeignKey(Domain, on_delete=models.CASCADE)
    CreateAt = models.DateTimeField (default=now)
    Name =  models.CharField (max_length=255)
    Logo =  models.ImageField (upload_to='static/images/')
    Link =  models.CharField (max_length=255)
    class Meta:
        verbose_name = "BusinessPartner"
        verbose_name_plural = "BusinessPartners"
    def __str__(self):
        return str(self.Domain) + '[' +self.Name+']'


#Contact Us
class ContactUs (models.Model) :
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)
    CreateAt = models.DateTimeField (default=now)
    Name = models.CharField (max_length=255)
    Email = models.CharField (max_length=200,blank=True, null=True)
    Phonenumber = models.CharField (max_length=12,blank=True, null=True)
    Subject = models.CharField (max_length=200)
    Message = models.CharField (max_length=1000)
    route = models.CharField (max_length=255)
    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us Form"
    def __str__(self):
        return str(self.Domain) + '[' +self.Name+' - '+self.Subject +']'





#HistoryOfCompanies
class HistoryOfCompanies (models.Model) :
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)
    CreateAt = models.DateTimeField (default=now)
    Date = models.CharField (max_length=12)
    Title = models.CharField (max_length=255)
    Paragraph = models.TextField (blank=True, null=True)
    Picture = models.ImageField (upload_to='static/images/' , blank=True, null=True) 
    Video = models.FileField (upload_to='static/images/' , blank=True, null=True) 
    Icon = models.ImageField (upload_to='static/images/' , blank=True, null=True)
    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "History"
    def __str__(self):
        return str(self.Domain) + '[' +self.Date+' - ' +self.Title+'>'
    


#ProjectProgress
class ProjectProgress (models.Model) :
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)
    CreateAt = models.DateTimeField (default=now)
    Date = models.CharField (max_length=12)
    Title = models.CharField (max_length=255)
    Paragraph = models.TextField (blank=True, null=True)
    File = models.FileField (upload_to='static/pdf/' , blank=True, null=True)
    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Project Progress"
    def __str__(self):
        return str(self.Domain) + '[' +self.Title+' - ' +self.Date+'>'



#IntroductionOfCompanies
class IntroductionOfCompanies (models.Model) :
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)
    CreateAt = models.DateTimeField (default=now)
    Logo =models.ImageField (upload_to='static/images/')
    Name =models.CharField (max_length=255)
    Link =models.CharField (max_length=255)
    Telephone = models.CharField (max_length=12)
    Address = models.CharField (max_length=500)
    ShortAboutUs = models.TextField (max_length=80)
    LongAboutUs = models.TextField ( blank=True, null=True)
    Picture = models.ImageField (upload_to='static/images/', blank=True, null=True)
    SubName =models.CharField (max_length=255,blank=True, null=True)
    Size = models.IntegerField ()
    Background = ColorField (format="hexa" , default='#FFFFFF')
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
    def __str__(self):
        return str(self.Domain) + '['+self.Name+']'

#TypeOfContent
class TypeOfContent (models.Model) :
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)
    CreateAt = models.DateTimeField (default=now)
    Title = models.CharField (max_length=300)
    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Type Of Content"
    def __str__(self):
        return str(self.Domain) + '[' +self.Title+']'

#Content Tabs
class ContentTabs (models.Model) :
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)
    CreateAt = models.DateTimeField (default=now)
    Title = models.TextField ()
    Description = models.TextField (blank=True, null=True)
    class Meta:
        verbose_name = "Content"
        verbose_name_plural = "Content Tabs"
    def __str__(self):
        return str(self.Domain) + '[' +self.Title+']'


class QaOfContentTabs(models.Model):
    ContentTabs = models.ForeignKey(ContentTabs, on_delete=models.CASCADE)
    CreateAt = models.DateTimeField(default=now)
    TitleTab = models.CharField(max_length=80)
    Question = models.TextField()
    Answer = models.TextField(blank=True, null=True)
    Image = models.ImageField(upload_to='static/images/')
    Link = models.CharField(max_length=150)
    class Meta:
        verbose_name = "QA"
        verbose_name_plural = "QA Of Content Tabs"

    def __str__(self):
        return str(self.ContentTabs) + '[' + self.Question + ']'


#Content Tabs
class ContentComparison (models.Model) :
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)
    CreateAt = models.DateTimeField (default=now)
    Title = models.TextField ()
    Description = models.TextField (blank=True, null=True)
    class Meta:
        verbose_name = "محتوا مقایسه"
        verbose_name_plural = "محتوای های مقایسه"
    def __str__(self):
        return str(self.Domain) + '[' +self.Title+']'

class ContentComparisonBtn(models.Model):
    ContentTabs = models.ForeignKey(ContentComparison, on_delete=models.CASCADE)
    CreateAt = models.DateTimeField(default=now)
    Title = models.TextField()
    Description = models.TextField(blank=True, null=True)
    Image = models.ImageField(upload_to='static/images/')
    class Meta:
        verbose_name = "محتوای مقایسه بخش"
        verbose_name_plural = "محتوای مقایسه بخش ها"
    def __str__(self):
        return str(self.ContentTabs) + '[' + self.Title + ']'
    


#Content Tabs
class ContentList (models.Model) :
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)
    CreateAt = models.DateTimeField (default=now)
    Title = models.TextField ()
    Description = models.TextField (blank=True, null=True)
    Image = models.ImageField(upload_to='static/images/')
    class Meta:
        verbose_name = "محتوا لیست"
        verbose_name_plural = "محتوای های لیست"
    def __str__(self):
        return str(self.Domain) + '[' +self.Title+']'

class ContentListChild(models.Model):
    ContentTabs = models.ForeignKey(ContentList, on_delete=models.CASCADE)
    CreateAt = models.DateTimeField(default=now)
    Title = models.TextField()
    Description = models.TextField(blank=True, null=True)
    Icon = models.ImageField(upload_to='static/images/')
    class Meta:
        verbose_name = "محتوای های لیست فرزند"
        verbose_name_plural = "محتوای های لیست فرزند ها"
    def __str__(self):
        return str(self.ContentTabs) + '[' + self.Title + ']'
    


#Grouping 
class Grouping (models.Model) :
    CreateAt = models.DateTimeField (default=now)
    Domain =  models.ForeignKey(Domain, on_delete=models.CASCADE)
    Title = models.CharField (max_length=255)
    Icone = models.ImageField (upload_to='static/images/')
    Url = models.CharField (max_length=255)
    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Grouping"
    def __str__(self):
        return str(self.Domain) + '[' +self.Title+']'

# News
class News (models.Model) :
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)
    CreateAt = models.DateTimeField (default=now)
    Content = models.TextField ()
    KeyWord = models.CharField (max_length=500)
    Grouping = models.ForeignKey(Grouping, on_delete=models.CASCADE)
    Title = models.CharField (max_length=500)
    ShortDescription = models.CharField (max_length=700)
    route = models.CharField (max_length=255)
    Picture = models.ImageField (upload_to='static/images/', blank=True, null=True)
    class Meta:
        verbose_name = "New"
        verbose_name_plural = "News"
    def __str__(self):
        return str(self.Domain) + '[' +self.Title+']'


#Products
class Products (models.Model) :
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)
    CreateAt = models.DateTimeField (default=now)
    Picture =models.ImageField (upload_to='static/images/')
    Paragraph = models.TextField ()
    Title = models.CharField (max_length=255)
    route = models.CharField (max_length=255)
    AdditionalImages = models.ImageField (upload_to='static/images/',blank=True, null=True)
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
    def __str__(self):
        return str(self.Domain) + '[' +self.Title+']'


#Questions
class Questions (models.Model) :
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)
    CreateAt = models.DateTimeField (default=now)
    Question = models.CharField (max_length=500)
    Answer = models.TextField ()
    class Meta:
        verbose_name = "Questions & Answer"
        verbose_name_plural = "Questions"
    def __str__(self):
        return str(self.Domain) + '[' +self.Question+']'


#QuickAccess 
class QuickAccess (models.Model) :
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)
    CreateAt = models.DateTimeField (default=now)
    Url = models.CharField (max_length=255)
    Picture = models.ImageField (upload_to='static/images/')
    Title = models.CharField (max_length=500)
    class Meta:
        verbose_name = "Links"
        verbose_name_plural = "QuickAccess"
    def __str__(self):
        return str(self.Domain) + '[' +self.Title+']'






#Menu 
class Menu (models.Model) :
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)
    CreateAt = models.DateTimeField (default=now)
    MegaMenu = models.CharField (max_length=255)
    Title = models.CharField (max_length=500)
    Link = models.CharField (max_length=255)
    Icon = models.ImageField (upload_to='static/images/' , blank=True , null=True)
    class Meta:
        verbose_name = "Links"
        verbose_name_plural = "Menu"
    def __str__(self):
        return str(self.Domain) + '[' +self.Title+']'




#RelatedLinks
class RelatedLinks (models.Model) :
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)
    CreateAt = models.DateTimeField (default=now)
    Title = models.CharField (max_length=300)
    Link = models.CharField (max_length=255)
    class Meta:
        verbose_name = "Links"
        verbose_name_plural = "Related Links"
    def __str__(self):
        return str(self.Domain) + '[' +self.Title+']'





#Slider
class Slider (models.Model) :
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)
    CreateAt = models.DateTimeField (default=now)
    Picture = models.ImageField (upload_to='static/images/')
    Title = models.CharField (max_length=300)
    Alt = models.CharField (max_length=300)
    class Meta:
        verbose_name = "Slide"
        verbose_name_plural = "Slider"
    def __str__(self):
        return str(self.Domain) + '[' +self.Title+']'


#Statistics
class Statistics (models.Model) :
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)
    CreateAt = models.DateTimeField (default=now)
    Title = models.CharField (max_length=300)
    Number = models.CharField (max_length=300)
    Icon = models.ImageField (upload_to='static/images/' , blank=True, null=True)
    class Meta:
        verbose_name = "Statistics"
        verbose_name_plural = "Statistics"
    def __str__(self):
        return str(self.Domain) + '[' +self.Title+']'






#SubjectSubscription
class SubjectSubscription (models.Model) :
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)
    CreateAt = models.DateTimeField (default=now)
    Title = models.CharField (max_length=300)
    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subject Subscription"
    def __str__(self):
        return str(self.Domain) + '[' +self.Title+']'









#Subscription
class Subscription (models.Model) :
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)
    CreateAt = models.DateTimeField (default=now)
    Subject = models.CharField (max_length=300)
    Telephone = models.CharField (max_length=12)
    class Meta:
        verbose_name = "Sub"
        verbose_name_plural = "Subscription"
    def __str__(self):
        return str(self.Domain) + '[' + self.Subject + ' - ' + self.Telephone + ']'



#GalleryPhoto
class GalleryPhoto (models.Model) :
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)
    CreateAt = models.DateTimeField (default=now)
    Picture =models.ImageField (upload_to='static/images/')
    Alt = models.CharField (max_length=255)
    route = models.CharField (max_length=255)

    class Meta:
        ordering = ['-CreateAt']
        verbose_name = "Photo"
        verbose_name_plural = "Gallery Photo"
    def __str__(self):
        return str(self.Domain) + '[' +self.Alt+']'


#GalleryVideo
class GalleryVideo (models.Model) :
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)
    CreateAt = models.DateTimeField (default=now)
    Video = models.FileField(upload_to='static/images/', validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi']), validate_file_size])
    ShortVideo = models.FileField(upload_to='static/images/', validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi']), validate_file_size])
    Alt = models.CharField (max_length=255)
    route = models.CharField (max_length=255)
    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Gallery Video"
    def __str__(self):
        return str(self.Domain) + '[' +self.Alt+']'





#PositionOfManagers
class positionofmanagers (models.Model) :
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)
    Title = models.CharField (max_length=300)
    Senior = models.CharField (max_length=300, blank=True , null= True)
    Level = models.IntegerField ()
    class Meta:
        verbose_name = "Position"
        verbose_name_plural = "Position Of Managers"
    def __str__(self):
        return str(self.Domain) + '[' +self.Title+']'






#ManagersPeople
class ManagersPeople (models.Model) :
    Position = models.ForeignKey(positionofmanagers, on_delete=models.CASCADE)
    Title = models.CharField (max_length=300)
    Name = models.CharField (max_length=300)
    Telephone = models.CharField (max_length=300)
    Email = models.CharField (max_length=300)
    Picture =models.ImageField (upload_to='static/images/')
    class Meta:
        verbose_name = "Manager"
        verbose_name_plural = "Managers"
    def __str__(self):
        return str(self.Position) + '[' +self.Title+ ' - ' + self.Name +']'





class Email(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    recipients = models.TextField()  # یک رشته جداشده با کاما که ایمیل‌های گیرندگان را در خود دارد
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)  # ضمیمه فایل
    SENDER_CHOICES = (
        ('info@isatispooya.com', 'info'),
        ('admin@isatispooya.com', 'admin'),
        ('fidip@isatispooya.com', 'fidip'),
        # ادامه‌ی فهرست آدرس‌های ایمیل و نام‌های فرستنده‌ها به ترتیب
    )
    sender = models.CharField(max_length=100, choices=SENDER_CHOICES)

    def __str__(self):
        return self.subject


#SendEmail
class SendEmail(models.Model):
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)
    CreateAt = models.DateTimeField (default=now)
    Recipient = models.CharField (max_length=300)
    Subject = models.CharField (max_length=300)
    Body = models.CharField (max_length=10000)
    SenderEmail = models.CharField (max_length=300)

 
 
#ReceiveEmail
class ReceiveEmail (models.Model) :
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)
    Receiver = models.CharField (max_length=255)
    Sender = models.CharField (max_length=255)
    Body = models.CharField (max_length=10000)
    Subject = models.CharField (max_length=300)
    CreateAt = models.DateTimeField (default=now)