import django_filters
from heritagesites.models import CountryArea, HeritageSite, HeritageSiteCategory, \
	IntermediateRegion, SubRegion, Region


class HeritageSiteFilter(django_filters.FilterSet):
	site_name = django_filters.CharFilter(
		field_name='site_name',
		label='Heritage Site Name',
		lookup_expr='icontains'
	)

	# Add description, heritage_site_category, region, sub_region and intermediate_region filters here

	description = django_filters.CharFilter(
		field_name='description',
		label='Heritage Site Description',
		lookup_expr='icontains'
	)

	heritage_site_category = django_filters.ModelChoiceFilter(
		field_name='heritage_site_category',
		label='Heritage Site Category',
		queryset=HeritageSiteCategory.objects.all().order_by('category_name'),
		lookup_expr='exact'
	)

	region = django_filters.ModelChoiceFilter(
		field_name='heritagesitejurisdiction__location__region_region_name',
		label='Region',
		queryset=HeritageSite.objects.all().order_by('heritagesitejurisdiction__location__region_region_name'),
		lookup_expr='exact'
	)

	sub_region = django_filters.ModelChoiceFilter(
		field_name='location__sub_region',
		label='Sub Region',
		queryset=CountryArea.objects.order_by('heritagesitejurisdiction__location__sub_region_sub_region_name'),
		lookup_expr='exact'
	)

	intermediate_region = django_filters.ModelChoiceFilter(
		field_name='heritagesitejurisdiction__location__intermediate_region_intermediate_region_name',
		label='Intermediate Region',
		queryset=HeritageSite.objects.all().select_related('heritage_site_category').order_by('heritagesitejurisdiction__location__intermediate_region_intermediate_region_name'),
		lookup_expr='exact'
	)


	country_area = django_filters.ModelChoiceFilter(
		field_name='country_area',
		label='Country/Area',
		queryset=CountryArea.objects.all().order_by('country_area_name'),
		lookup_expr='exact'
	)

	# Add date_inscribed filter here
	date_inscribed = django_filters.NumberFilter(
		field_name='date_inscribed',
		label='Date Inscribed',
		lookup_expr='exact'
	)

	class Meta:
		model = HeritageSite
		# form = SearchForm
		# fields [] is required, even if empty.
		fields = []