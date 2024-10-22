from django.db import models
from django.urls import reverse
from django.db.models import Transform
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from timezone_field import TimeZoneField

from netbox.models import NetBoxModel, PrimaryModel
from netbox.models.features import ContactsMixin
from utilities.choices import ChoiceSet
from circuits.models import Provider
from dcim.models import Site

from .validators import PhoneValidator, PhoneMaintainerValidator
from .utils import format_number, format_number_error


__all__ = (
    'PhoneDID',
    'LogValue',
    'PhoneInfo',
    'FloorValue',
    'PhoneDelivery',
    'AbsoluteValue',
    'PhoneMaintainer',
    'PhoneBoolChoices',
    'PhoneMaintainerStatusChoice',
    'PhoneDeliveryStatusChoices',
)


class PhoneMaintainerStatusChoice(ChoiceSet):

    CHOICES = (
        ('active', _('Active'), 'green'),
        ('retired', _('Retired'), 'red'),
        ('unknown', _('Unknown'), 'gray'),
    )


class PhoneDeliveryStatusChoices(ChoiceSet):

    CHOICES = (
        ('active', _('Active'), 'green'),
        ('planned', _('Planned'), 'cyan'),
        ('staging', _('Staging'), 'blue'),
        ('retired', _('Retired'), 'red'),
        ('unknown', _('Unknown'), 'gray'),
    )


class PhoneBoolChoices(ChoiceSet):

    CHOICES = (
        ('unknown', _('Unknown'), 'gray'),
        ('true', _('True'), 'green'),
        ('false', _('False'), 'red'),
    )


class AbsoluteValue(Transform):
    lookup_name = "abs"
    function = "ABS"
    bilateral = True

class FloorValue(Transform):
    lookup_name = "floor"
    function = "FLOOR"
    bilateral = True

class LogValue(Transform):
    lookup_name = "log"
    function = "LOG"
    bilateral = True


models.IntegerField.register_lookup(AbsoluteValue)
models.IntegerField.register_lookup(FloorValue)
models.IntegerField.register_lookup(LogValue)


class BiAbsoluteValue(Transform):
    lookup_name = "biabs"
    function = "ABS"
    bilateral = True

class BiFloorValue(Transform):
    lookup_name = "bifloor"
    function = "FLOOR"
    bilateral = True

class BiLogValue(Transform):
    lookup_name = "bilog"
    function = "LOG"
    bilateral = True

models.IntegerField.register_lookup(BiAbsoluteValue)
models.IntegerField.register_lookup(BiFloorValue)
models.IntegerField.register_lookup(BiLogValue)

class PhoneMaintainer(PrimaryModel, ContactsMixin):
    name = models.CharField(
        verbose_name=_('Maintainer'),
        unique=True,
    )
    slug = models.SlugField(
        verbose_name=_('slug'),
        max_length=100,
        unique=True,
        blank=True,
    )
    status = models.CharField(
        max_length=30,
        choices=PhoneMaintainerStatusChoice,
        default="Unknown",
        verbose_name=_('Status')
    )
    physical_address = models.CharField(
        verbose_name=_('Physical address'),
        max_length=200,
        null=True,
        blank=True,
        help_text=_('Physical location of the maintainer')
    )
    shipping_address = models.CharField(
        verbose_name=_('Shipping address'),
        max_length=200,
        null=True,
        blank=True,
        help_text=_('If different from the physical address')
    )
    time_zone = TimeZoneField(
        null=True,
        blank=True
    )
    latitude = models.DecimalField(
        verbose_name=_('Latitude'),
        max_digits=8,
        decimal_places=6,
        blank=True,
        null=True,
        help_text=_('GPS coordinate in decimal format (xx.yyyyyy)')
    )
    longitude = models.DecimalField(
        verbose_name=_('Longitude'),
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True,
        help_text=_('GPS coordinate in decimal format (xx.yyyyyy)')
    )

    def __str__(self) -> str:
        return f'{self.name}'

    def get_absolute_url(self) -> str:
        return reverse('plugins:sop_phone:phonemaintainer_detail', args=[self.pk])

    def get_status_color(self) -> str:
        return PhoneDeliveryStatusChoices.colors.get(self.status)

    class Meta(NetBoxModel.Meta):
        verbose_name = _('Phone Maintainer')
        verbose_name_plural = _('Phone Maintainers')
        constraints = (
            models.UniqueConstraint(
                fields=('name',),
                name='%(app_label)s_%(class)s_unique_name',
                violation_error_message=_("Maintainer name must be unique.")
            ),
            models.UniqueConstraint(
                fields=('slug',),
                name='%(app_label)s_%(class)s_unique_slug',
                violation_error_message=_("Maintainer slug must be unique.")
            )
        )

    def fail(self, message, field=None):
        if field is not None:
            raise ValidationError({field: message})
        raise ValidationError(message)

    def clean(self):
        super().clean()
        if self.physical_address:
            PhoneMaintainerValidator.check_address(self.physical_address, 'physical_address')
        if self.shipping_address:
            PhoneMaintainerValidator.check_address(self.shipping_address, 'shipping_address')
 

class PhoneInfo(NetBoxModel):
    site = models.OneToOneField(
        Site,
        on_delete=models.CASCADE,
        verbose_name=_('Site'),
    )
    maintainer = models.ForeignKey(
        PhoneMaintainer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_('Maintainer'),
    )

    def __str__(self) -> str:
        return f'{self.site} phone maintainer'

    def get_absolute_url(self) -> str:
        return reverse('plugins:sop_phone:phoneinfo_detail', args=[self.pk])

    class Meta(NetBoxModel.Meta):
        verbose_name = _('Information')
        verbose_name_plural = _('Informations')
        constraints = [
            models.UniqueConstraint(
                fields=['site',],
                name='%(app_label)s_%(class)s_unique_site',
                violation_error_message=_("Site must be unique.")
            )
        ]


class PhoneDelivery(NetBoxModel):
    delivery = models.CharField(
        verbose_name=_('Delivery'),
        null=True,
        blank=True,
    )
    provider = models.ForeignKey(
        Provider,
        on_delete=models.RESTRICT,
        verbose_name=_('Provider'),
        null=True,
        blank=True,
    )
    site = models.ForeignKey(
        Site,
        on_delete=models.RESTRICT,
        verbose_name=_('Site'),
    )
    channel_count = models.PositiveBigIntegerField(
        verbose_name=_('Channel Count'),
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=30,
        choices=PhoneDeliveryStatusChoices,
        verbose_name=_('Status'),
    )
    ndi = models.PositiveBigIntegerField(
        verbose_name=_('NDI'),
        null=True,
        blank=True,
    )
    dto = models.PositiveBigIntegerField(
        verbose_name=_('DTO'),
        null=True,
        blank=True,
    )
    description = models.CharField(
        verbose_name=_('description'),
        max_length=200,
        blank=True
    )
    comments = models.TextField(
        verbose_name=_('comments'),
        blank=True
    )

    def get_absolute_url(self) -> str:
        return reverse('plugins:sop_phone:phonedelivery_detail', args=[self.pk])

    def get_status_color(self) -> str:
        return PhoneDeliveryStatusChoices.colors.get(self.status)

    def __str__(self) -> str:
        delivery:str = self.delivery if hasattr(self, 'delivery') else 'Unknown delivery'
        provider:str = self.provider if hasattr(self, 'provider') else 'Unknown provider'
        return f'{delivery} / {provider}'

    def clean(self):
        super().clean()
        if hasattr(self, 'delivery') and self.delivery and self.site:
            if PhoneDelivery.objects.exclude(pk=self.pk).filter(site=self.site, delivery=self.delivery).exists():
                raise ValidationError({
                    'delivery': _(f'{self.site}: A "{self.delivery}" delivery method already exists for this site.')
                })
        if self.ndi:
            PhoneValidator.check_number('ndi', self.ndi)
            if PhoneDelivery.objects.exclude(pk=self.pk).filter(ndi=self.ndi).exists():
                raise ValidationError({
                    'ndi': _(f'{self.site}: The MBN/NDI {format_number_error(self.ndi)} already exists on another\
 delivery on site {PhoneDelivery.objects.get(ndi=self.ndi)}')
                })
            if PhoneDelivery.objects.filter(pk=self.pk, dto=self.ndi):
                raise ValidationError({
                    'ndi': _(f'{self.site}: The MBN/NDI {format_number_error(self.ndi)} cannot be the DTO of its own delivery.')
                    })
            lndi = len(str(self.ndi))
            for rng in PhoneDID.objects.exclude(site=self.site):
                if len(str(rng.start)) == lndi:
                    if self.ndi <= rng.end and rng.start <= self.ndi:
                        raise ValidationError({
                            'ndi': _(f'{self.site}: The MBN/NDI {self.ndi} overlap DID range {format_number_error(rng.start)}\
 -> {format_number_error(rng.end)}')
                        })
        if self.dto:
            PhoneValidator.check_number('dto', self.dto)
            if self.ndi == self.dto:
                raise ValidationError({
                    'dto': _(f'{self.site}: The DTO {format_number_error(self.dto)} cannot be the MBN/NDI of its own delivery.')
                    })
            current = PhoneDelivery.objects.filter(pk=self.pk)
            if current.exists and PhoneDID.objects.filter(delivery=current.first()):
                ldto = len(str(self.dto))
                for rng in PhoneDID.objects.filter(delivery=current.first()):
                    if len(str(rng.start)) == ldto:
                        if self.dto <= rng.end and rng.start <= self.dto:
                            raise ValidationError({
                                'dto': _(f'The DTO {format_number_error(self.dto)} overlaps DID range\
 {format_number_error(rng.start)} -> {format_number_error(rng.end)}')
                                })

    class Meta(NetBoxModel.Meta):
        verbose_name = _('Phone Delivery')
        verbose_name_plural = _('Phone Deliveries')
        constraints = (
            models.UniqueConstraint(
                fields=('ndi',),
                name='%(app_label)s_%(class)s_unique_ndi',
                violation_error_message=_("NDI must be unique.")
            ),
            models.UniqueConstraint(
                fields=('delivery', 'site'),
                name='%(app_label)s_%(class)s_unique_delivery_method_site',
                violation_error_message=_("Delivery method must be unique in a site.")
            )
        )


class PhoneDID(NetBoxModel):
    delivery = models.ForeignKey(
        PhoneDelivery,
        on_delete=models.SET_NULL,
        verbose_name=_('Delivery'),
        null=True,
        blank=True,
    )
    site = models.ForeignKey(
        Site,
        on_delete=models.CASCADE,
        verbose_name=_('Site'),
        null=False,
        blank=True,
    )
    start = models.PositiveBigIntegerField(
        unique=False,
        verbose_name=_('Start number'),
        null=False,
        blank=True,
    )
    end = models.PositiveBigIntegerField(
        unique=False,
        verbose_name=_('End number'),
        null=False,
        blank=True,
    )

    def __str__(self) -> str:
        if not self.start and not self.end:
            return f'No DID'
        # \u00A0 is unicode for ' '
        return f'{format_number(number=self.start)}\u00A0\u00A0\u00A0\u00A0>>\u00A0\u00A0\u00A0\u00A0{format_number(number=self.end)}'

    def get_absolute_url(self) -> str:
        return reverse('plugins:sop_phone:phonedid_detail', args=[self.pk])

    def clean(self):
        super().clean()

        PhoneValidator.check_delivery_site(self.delivery, self.site)

        PhoneValidator.check_number('start', self.start)
        if self.end is None:
            self.end=self.start
        else :
            PhoneValidator.check_number('end', self.end)
            PhoneValidator.check_start_end(self.start, self.end)  

        if PhoneDelivery.objects.exclude(site=self.site).filter(ndi=self.start).exists():
            raise ValidationError({
                'start': _(f'{self.site}: Start {format_number_error(self.start)} overlaps {format_number_error(PhoneDelivery.objects.get(ndi=self.start))} delivery MBN/NDI.')
                })
        if PhoneDelivery.objects.exclude(site=self.site).filter(ndi=self.end).exists():
            raise ValidationError({
                'end': _(f'{self.site}: End {format_number_error(self.end)} overlaps {format_number_error(PhoneDelivery.objects.get(ndi=self.end))} delivery MBN/NDI.')
                })

        # check if the current range overlaps its own DTO
        PhoneValidator.check_delivery_overlaps(self.delivery, self.start, self.end)
        # check if self.end or self.start overlaps an existing DID range
        lnum=len(str(self.start))
        for deli in PhoneDelivery.objects.exclude(site=self.site):
            #only compare if numbers are comaprable (have the same length)
            if len(str(deli.ndi)) == lnum:
                # check if number overlap
                if self.start <= deli.ndi and self.end >= deli.ndi:
                    raise ValidationError({
                        'start': _(f'{self.site}: This range {format_number_error(self.start)} -> {format_number_error(self.end)}\
 overlaps {deli.site} delivery MBN/NDI.')
                    })

        for rng in PhoneDID.objects.exclude(pk=self.pk):
            #only compare if numbers are comaprable (have the same length)
            if len(str(rng.start))==lnum:
                # check if number overlap
                if self.start <= rng.end and rng.start <= self.end:
                    raise ValidationError({
                        'start': _(f'{self.site}: This range {format_number_error(self.start)} -> {format_number_error(self.end)}\
 overlaps range {format_number_error(rng.start)} -> {format_number_error(rng.end)} on site {rng.site}.')
                        })

    def save(self, *args, **kwargs):
        if not self.end or self.end == 0:
            self.end = self.start
        super().save(*args, **kwargs)

    class Meta(NetBoxModel.Meta):
        ordering = ('start',)
        verbose_name = _('DID Range')
        verbose_name_plural = _('DIDs')

        constraints = (
            models.UniqueConstraint(
                fields=('start',),
                name='%(app_label)s_%(class)s_unique_start_number',
                violation_error_message=_("Start number must be unique.")
            ),
            models.UniqueConstraint(
                fields=('end',),
                name='%(app_label)s_%(class)s_unique_end_number',
                violation_error_message=_("End number must be unique.")
            ),
            models.CheckConstraint(
                check=models.Q(end__gte=models.F('start')) & \
                    models.Q(start__biabs__bilog__bifloor=models.F("end")),
                name='%(app_label)s_%(class)s_end_greater_than_start',
                violation_error_message=_("End number must be greater than or equal to start number.")
            )
        )
