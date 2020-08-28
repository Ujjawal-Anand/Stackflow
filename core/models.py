from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class ApiData(models.Model):
    page =  models.PositiveIntegerField(_("Page number"), null=True, blank=True)
    pagesize = models.PositiveIntegerField(_("Page Size"), null=True, blank=True)
    fromdate = models.DateField(_("From Date"), null=True, blank=True)
    todate = models.DateField(_("To Date"), null=True, blank=True)
    
    DESCENDING = 'desc'
    Ascending = 'asc'
    ORDER_OPTIONS = (
        (DESCENDING, 'Descending'),
        (Ascending, 'Ascending')
    )
    order = models.CharField(_("Order"), max_length=20, default=DESCENDING, choices=ORDER_OPTIONS)
    min_date = models.DateField(_("min"), null=True, blank=True)
    max_date = models.DateField(_("max"), null=True, blank=True)
    SORT_OPTIONS = (
        ('activity', 'Activity'),
        ('votes', 'Votes'),
        ('creation', 'Creation'),
        ('relevance', 'Relevance')
    )
    sort = models.CharField(_("Sort"), max_length=20, 
                            default='activity', choices=SORT_OPTIONS)
    
    # a free form text parameter, will match all question properties 
    # based on an undocumented algorithm
    q = models.CharField(_("q"), max_length=1023, blank=True)
    
    # true to return only questions with accepted answers, 
    # false to return only those without. Omit to elide constraint.
    accepted = models.BooleanField(_("accepted"), blank=True, null=True)
    
    # the minimum number of answers returned questions must have.
    answers = models.PositiveIntegerField(_("Number of answers"), blank=True, null=True)
    
    # text which must appear in returned questions' bodies
    body = models.CharField(blank=True, max_length=1023,
                            help_text=_("text which must appear in returned questions' bodies."))
    
    # true to return only closed questions, false to return only open ones. Omit to elide constraint.
    closed = models.BooleanField(_("closed?"), blank=True, null=True)
    
    # true to return only questions migrated away from a site, 
    # false to return only those not. Omit to elide constraint.
    migated = models.BooleanField(_("migrated?"), blank=True, null=True)

    # true to return only questions with post notices, 
    # false to return only those without. Omit to elide constraint.
    notice = models.BooleanField(_("Notice"), blank=True, null=True)

    # a semicolon delimited list of tags, none of which 
    # will be present on returned questions.
    notagged = models.CharField(_("Not tagged"), max_length=253, blank=True)

    # a semicolon delimited list of tags, of which at least 
    # one will be present on all returned questions
    tagged = models.CharField(_("Tagged"), max_length=255, blank=True)

    # text which must appear in returned questions' titles
    title = models.CharField(_("Title"), max_length=255, blank=True)

    # the id of the user who must own the questions returned.
    user = models.PositiveIntegerField(_("Id of user"), null=True, blank=True)

    # a url which must be contained in a post, may include a wildcard.
    url = models.CharField(_("url"), max_length=255, blank=True)

    # the minimum number of views returned questions must have.
    views = models.PositiveIntegerField(_("Minimum number of views"), blank=True, null=True)

    # true to return only community wiki questions, false to return 
    # only non-community wiki ones. Omit to elide constraint.
    wiki = models.BooleanField(_("wiki"), blank=True, null=True)

    class Meta:
        verbose_name = _("ApiData")
        verbose_name_plural = _("ApiDatas")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ApiData_detail", kwargs={"pk": self.pk})

