import matplotlib.pylab as plt
import matplotlib.colors as pltcol

#Creating dictionaries for the IoD. 
iod_indices = [
                'a_index_of_multiple_deprivation_imd',
                'b_income_deprivation_domain', 
                'c_employment_deprivation_domain',
                'd_education_skills_and_training_domain',
                'e_health_deprivation_and_disability_domain', 
                'f_crime_domain',
                'g_barriers_to_housing_and_services_domain',
                'h_living_environment_deprivation_domain',
                'i_income_deprivation_affecting_children_index_idaci',
                'j_income_deprivation_affecting_older_people_index_idaopi'
                ]
iod_names = [
                'Index of Multiple Deprivation (IMD)',
                'Income Deprivation',
                'Employment Deprivation',
                'Education, Skills and Training',
                'Health Deprivation and Disability',
                'Crime', 
                'Barriers to Housing and Services',
                'Living Environment Deprivation',
                'Income Deprivation Affecting Children Index (IDACI)',
                'Income Deprivation Affecting Older People Index (IDAOPI)',
            ]

#Creating Dictionaries to link the two indices, 
iod_dict = dict(zip(iod_names,iod_indices))
iod_dict_inv = dict(zip(iod_indices,iod_names))

#Colour Pallette for the Choropleth maps
# As we are looking at the Deciles, we will have 10 points. 
domain = [i+1 for i in range(10)]
# Change plasma_r to try out different pallettes.  
cmap = plt.cm.get_cmap('plasma_r',10)
range_ = [pltcol.rgb2hex(cmap(domain)[i]) for i in range(10)]