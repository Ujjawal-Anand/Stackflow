from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class ApiData(models.Model):
    page =  models.PositiveIntegerField(_("Page number"), null=True, blank=True,
                                help_text=_("Returns specified Page of result"))
    pagesize = models.PositiveIntegerField(_("Page Size"), null=True, blank=True,
                            help_text=_("Number of pages to be returned"))
    fromdate = models.DateField(_("From Date"), null=True, blank=True,
                        help_text=_('Return questions from date'))
    todate = models.DateField(_("To Date"), null=True, blank=True,
                            help_text=_("Returns question up to date"))
    
    DESCENDING = 'desc'
    Ascending = 'asc'
    ORDER_OPTIONS = (
        (DESCENDING, 'Descending'),
        (Ascending, 'Ascending')
    )
    order = models.CharField(_("Order"), max_length=20, default=DESCENDING, choices=ORDER_OPTIONS,
                                help_text=_("order of data returned"))
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
    
    
    q = models.CharField(_("q"), max_length=1023, blank=True,
                            help_text=_('A free form text parameter, will match all question properties '))
    
    # true to return only questions with accepted answers, 
    # false to return only those without. Omit to elide constraint.
    accepted = models.BooleanField(_("accepted"), blank=True, null=True,
                                    help_text=_("True to return only questions with accepted answers"))
    
    answers = models.PositiveIntegerField(_("Number of answers"), 
                                          blank=True, null=True,
                                          help_text=_("The minimum number of answers returned questions must have"))
    
    body = models.CharField(blank=True, max_length=1023,
                            help_text=_("Text which must appear in returned questions' bodies."))
    
    closed = models.BooleanField(_("closed"), blank=True, null=True,
                                help_text=_("True to return only closed questions, false to return only open ones"))
    
    # true to return only questions migrated away from a site, 
    # false to return only those not. Omit to elide constraint.
    migrated = models.BooleanField(_("migrated"), blank=True, null=True,
                                help_text=_("True to return only questions migrated away from a site"))

    # true to return only questions with post notices, 
    # false to return only those without. Omit to elide constraint.
    notice = models.BooleanField(_("Notice"), blank=True, null=True,
                                help_text=_("True to return only questions with post notices"))

    
    notagged = models.CharField(_("Not tagged"), max_length=253, blank=True,
                                help_text=_("A semicolon delimited list of tags, none of which will be present on returned questions."))

    tagged = models.CharField(_("Tagged"), max_length=255, blank=True,
                                help_text=_("A semicolon delimited list of tags, to be present (at least one)"))

    title = models.CharField(_("Title"), max_length=255, blank=True,
                            help_text=_("Text which must appear in returned questions' titles"))

    user = models.PositiveIntegerField(_("Id of user"), null=True, blank=True,
                            help_text=_("The id of the user who must own the questions returned."))

    
    url = models.CharField(_("url"), max_length=255, blank=True,
                            help_text=_("A url which must be contained in a post, may include a wildcard."))

    views = models.PositiveIntegerField(_("views"), blank=True, null=True,
                                help_text=_("The minimum number of views returned questions must have."))

    wiki = models.BooleanField(_("wiki"), blank=True, null=True,
                            help_text=_("True to return only community wiki questions"))

    class Meta:
        verbose_name = _("ApiData")
        verbose_name_plural = _("ApiDatas")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ApiData_detail", kwargs={"pk": self.pk})

