from resume.models import Resume
from candidate.DataTable import DataTable


def get_resume_list(request):
    """
    Would be used to get available resume for data table.
    """
    
    #initial querySet
    query_set = Resume.objects.all()
    #columnIndexNameMap is required for correct sorting behavior
    column_index_name_map = {
        0: 'name',
        1: 'gender',
        2: 'experience',
        3: 'university',
        4: 'graduation_year',
        5: 'skills'
    }

    #call to generic function for Data table
    data_table = DataTable(request, query_set, column_index_name_map)
    #prepared data set to be displayed in data table
    data_set = prepare_resume_data(data_table.query_set)

    return data_table.get_datatables_records(data_set)


def prepare_resume_data(query_set):
    """
    Would prepared the data set to displayed in the datatable
    using the query set as argument.
    """

    data_set = []

    #Using query set preparing the data set.
    for qs in query_set:
        data_set.append([
        	qs.name, qs.gender, qs.experience, 
        	qs.university, qs.graduation_year, qs.skills
        ])
    
    return data_set