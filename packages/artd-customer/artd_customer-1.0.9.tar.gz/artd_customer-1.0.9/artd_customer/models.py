"""
 * Copyright (C) ArtD SAS - All Rights Reserved
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary and confidential
 * Written by Jonathan Favian Urzola Maldonado <jonathan@artd.com.co>, 2023
"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from artd_location.models import City, Country
from artd_partner.models import Partner

FIELD_TYPES = [
    ("number", _("Number")),
    ("date", _("Date")),
    ("email", _("Email")),
    ("password", _("Password")),
    ("text", _("Text")),
    ("list", _("List")),
]

CUSTOMER_TYPES = [
    ("customer", _("Customer")),
    ("supplier", _("Supplier")),
    ("other", _("Other")),
]

CUSTOMER_PERSON_TYPES = [
    ("person", _("Person")),
    ("company", _("Company")),
]

DOCUMENT_TYPES = [
    ("dni", _("DNI")),
    ("nit", _("NIT")),
    ("passport", _("Passport")),
    ("passport", _("Passport")),
    ("Foreigners_id:_card", _("Foreigner's ID card")),
    ("license", _("License")),
    ("other", _("Other")),
]


class CustomerBaseModel(models.Model):
    created_at = models.DateTimeField(
        _("Created at"),
        help_text=_("Date time on which the object was created."),
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        _("Updated at"),
        help_text=_("Date time on which the object was last updated."),
        auto_now=True,
        editable=False,
    )
    status = models.BooleanField(
        _("Status"),
        help_text=_("Status of the object."),
        default=True,
    )
    source = models.JSONField(
        _("Source"),
        help_text=_("Source of the object."),
        blank=True,
        null=True,
    )
    external_id = models.CharField(
        _("External ID"),
        help_text=_("External ID of the object."),
        max_length=100,
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True


class CustomerGroup(CustomerBaseModel):
    """Model definition for Customer Group."""

    partner = models.ForeignKey(
        Partner,
        on_delete=models.CASCADE,
        related_name="+",
        null=True,
        blank=True,
    )
    group_code = models.SlugField(
        _("Customer code"),
        max_length=50,
        help_text=_("Customer code"),
        unique=True,
    )
    group_name = models.CharField(
        _("Customer group name"),
        max_length=100,
        help_text=_("Customer group name"),
    )
    group_description = models.TextField(
        _("Customer group description"),
        help_text=_("Customer group description"),
        blank=True,
        null=True,
    )

    class Meta:
        """Meta definition for Customer Group."""

        verbose_name = _("Customer Group")
        verbose_name_plural = _("Customer Groups")

    def __str__(self):
        """Unicode representation of Customer Group."""
        return self.group_name


class MacroTaxSegment(CustomerBaseModel):
    """Model definition for MacroTaxSegment."""

    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="+",
        null=True,
        blank=True,
    )
    name = models.CharField(
        _("Name"),
        max_length=250,
        help_text=_("Name of the macroTaxSegment."),
    )
    code = models.CharField(
        _("Code"),
        max_length=250,
        help_text=_("Code of the macrosegment."),
    )

    class Meta:
        """Meta definition for MacroTaxSegment."""

        verbose_name = _("MacroTaxSegment")
        verbose_name_plural = _("Macrosegments")

    def __str__(self):
        """Unicode representation of MacroTaxSegment."""
        return f"{self.name} - {self.country}"


class TaxSegment(CustomerBaseModel):
    """Model definition for TaxSegment."""

    macrosegment = models.ForeignKey(
        MacroTaxSegment,
        on_delete=models.CASCADE,
        related_name="+",
        null=True,
        blank=True,
    )
    name = models.CharField(
        _("Name"),
        max_length=250,
        help_text=_("Name of the taxSegment."),
    )
    code = models.CharField(
        _("Code"),
        max_length=250,
        help_text=_("Code of the taxSegment."),
    )

    class Meta:
        """Meta definition for TaxSegment."""

        verbose_name = _("TaxSegment")
        verbose_name_plural = _("TaxSegments")

    def __str__(self):
        """Unicode representation of TaxSegment."""
        return f"{self.name} - {self.macrosegment}"


class Customer(CustomerBaseModel):
    partner = models.ForeignKey(
        Partner,
        on_delete=models.CASCADE,
        related_name="+",
        null=True,
        blank=True,
    )
    name = models.CharField(
        _("Name"),
        help_text=_("Name of the customer."),
        max_length=100,
        blank=True,
    )
    last_name = models.CharField(
        _("Last name"),
        help_text=_("Last name of the customer."),
        max_length=100,
        blank=True,
        null=True,
    )
    birth_date = models.DateField(
        _("Birth date"),
        help_text=_("Birth date of the customer."),
        blank=True,
        null=True,
    )
    document = models.CharField(
        _("Customer document"),
        max_length=50,
        help_text=_("Customer document"),
        blank=True,
        null=True,
    )
    email = models.EmailField(
        _("Email"),
        help_text=_("Email of the customer."),
        max_length=100,
        blank=True,
        null=True,
    )
    phone = models.CharField(
        _("Phone"),
        help_text=_("Phone of the customer."),
        max_length=100,
        blank=True,
        null=True,
    )
    city = models.ForeignKey(
        City,
        verbose_name=_("City"),
        help_text=_("City of the customer."),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    customer_group = models.ForeignKey(
        CustomerGroup,
        verbose_name=_("Customer group"),
        help_text=_("Customer group."),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    other_data = models.JSONField(
        _("Other data"),
        help_text=_("Other customer data"),
        blank=True,
        null=True,
    )
    tax_segment = models.ForeignKey(
        TaxSegment,
        verbose_name=_("Tax segment"),
        help_text=_("Tax segment."),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    customer_type = models.CharField(
        _("Customer type"),
        max_length=50,
        help_text=_("Customer type"),
        choices=CUSTOMER_TYPES,
        default="customer",
    )
    customer_person_type = models.CharField(
        _("Customer person type"),
        max_length=50,
        help_text=_("Customer person type"),
        choices=CUSTOMER_PERSON_TYPES,
        default="person",
    )
    document_type = models.CharField(
        _("Document type"),
        max_length=50,
        help_text=_("Document type"),
        choices=DOCUMENT_TYPES,
        default="dni",
    )

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self):
        return f"{self.name} {self.last_name}"

    def save(self, *args, **kwargs):
        if not self._state.adding:  # Verificar si se está actualizando
            # Obtener el valor anterior del campo antes de guardar
            old_model = Customer.objects.get(pk=self.pk)

        else:
            old_model = None  # Es un nuevo registro

        super(Customer, self).save(*args, **kwargs)

        if old_model is None:
            news_group = CustomerGroup.objects.get(group_code="new")
            CustomerGroupChangeLog.objects.create(
                customer=self,
                old_group=news_group,
                new_group=news_group,
            )
        else:
            if old_model.customer_group != self.customer_group:
                customer_group_change_log = CustomerGroupChangeLog.objects.create(
                    customer=self,
                    new_group=self.customer_group,
                )
                if old_model.customer_group is not None:
                    customer_group_change_log.old_group = old_model.customer_group
                    customer_group_change_log.save()


class Tag(CustomerBaseModel):
    partner = models.ForeignKey(
        Partner,
        verbose_name=_("Partner"),
        help_text=_("Partner of the tag."),
        on_delete=models.CASCADE,
    )

    description = models.CharField(
        _("Tag description"),
        max_length=250,
        help_text=_("Tag description"),
    )

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.description


class CustomerTag(CustomerBaseModel):
    customer = models.ForeignKey(
        Customer,
        verbose_name=_("Customer"),
        help_text=_("Customer"),
        on_delete=models.CASCADE,
    )
    tag = models.ForeignKey(
        Tag,
        verbose_name=_("Customer tag"),
        help_text=_("Tag."),
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _("Customer Tag")
        verbose_name_plural = _("Customer Tags")

    def __str__(self):
        return f"{self.customer} ({self.tag.description})"


class CustomerAddress(CustomerBaseModel):
    customer = models.ForeignKey(
        Customer,
        verbose_name=_("Customer"),
        help_text=_("Customer"),
        on_delete=models.CASCADE,
    )
    city = models.ForeignKey(
        City,
        verbose_name=_("City"),
        help_text=_("City of the customer."),
        on_delete=models.CASCADE,
    )
    phone = models.CharField(
        _("Phone"),
        max_length=50,
        help_text=_("Customer phone"),
        blank=True,
        null=True,
    )
    address = models.TextField(
        _("Customer address"),
        help_text=_("Customer address"),
        blank=True,
        null=True,
    )
    other_data = models.JSONField(
        _("Other data"),
        help_text=_("Other customer address data"),
        blank=True,
        null=True,
    )

    class Meta:
        """Meta definition for CustomerAddress."""

        verbose_name = _("Customer Address")
        verbose_name_plural = _("Customer Addresss")

    def __str__(self):
        """Unicode representation of CustomerAddress."""
        return f"{self.customer} ({self.address})"


class CustomerAdditionalFields(CustomerBaseModel):
    partner = models.ForeignKey(
        Partner,
        verbose_name=_("Partner"),
        help_text=_("Partner of the field."),
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        _("Field name"),
        help_text=_("Field name"),
        max_length=250,
    )
    field_type = models.CharField(
        _("Field type"),
        help_text=_("Field type"),
        max_length=10,
        choices=FIELD_TYPES,
    )
    label = models.CharField(
        _("Field label"),
        max_length=50,
        help_text=_("Field label"),
    )
    required = models.BooleanField(
        _("Is required?"),
        help_text=_("Is required?"),
        default=False,
    )
    field_values = models.JSONField(
        _("Field values"),
        help_text=_(
            'If the field is of type list, you must place the values ​​separated by commas inside the container [] and each value inside quotes, for example ["Dog","Cat"]'  # noqa
        ),
        blank=True,
        null=True,
        default=list,
    )

    class Meta:
        """Meta definition for CustomerAdditionalFields."""

        verbose_name = _("Customer Additional Field")
        verbose_name_plural = _("Customer Additional Fields")

    def __str__(self):
        """Unicode representation of CustomerAdditionalFields."""
        return f"{self.name}"


class CustomerGroupChangeLog(CustomerBaseModel):
    """Model definition for Customer Group Change Log."""

    customer = models.ForeignKey(
        Customer,
        verbose_name=_("Customer"),
        help_text=_("Customer"),
        on_delete=models.CASCADE,
    )

    old_group = models.ForeignKey(
        CustomerGroup,
        verbose_name=_("Old group"),
        help_text=_("Old group"),
        on_delete=models.CASCADE,
        related_name="old_group",
        null=True,
        blank=True,
    )

    new_group = models.ForeignKey(
        CustomerGroup,
        verbose_name=_("New group"),
        help_text=_("New group"),
        on_delete=models.CASCADE,
        related_name="new_group",
    )

    class Meta:
        """Meta definition for Customer Group Change Log."""

        verbose_name = _("Customer Group Change Log")
        verbose_name_plural = _("Customer Group Change Logs")

    def __str__(self):
        """Unicode representation of Customer Group Change Log."""
        return f"Log #{self.id}"
