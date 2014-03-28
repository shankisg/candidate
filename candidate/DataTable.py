from django.db.models import Q
from django.http import HttpResponse
from django.utils import simplejson
from django.utils.cache import add_never_cache_headers


class DataTable(object):
    """
    Would used to prepare the data to used for displaying in the datatables.
    """

    def __init__(
            self, request, query_set,
            column_index_name_map,
            json_path_template=None, *args):
        """
        Would setting the inital data to be sent for displaying in datatable.
        """

        cols = int(request.GET.get('iColumns', 0))  # Get the number of columns
        i_display_length = min(int(request.GET.get('iDisplayLength', 10)), 100)  # Safety measure.
        start_record = int(request.GET.get('iDisplayStart', 0))  # Where the data starts from (page)
        end_record = start_record + i_display_length  # where the data ends (end of page)

        # Pass sColumns
        keys = column_index_name_map.keys()
        keys.sort()
        col_items = [column_index_name_map[key] for key in keys]
        s_columns = ",".join(map(str, col_items))

        # Ordering data
        i_sorting_cols = int(request.GET.get('iSortingCols', 0))
        asorting_cols = []

        if i_sorting_cols:

            for sorted_index_cols in range(0, i_sorting_cols):
                sorted_col_id = int(request.GET.get(
                    'iSortCol_'+str(sorted_index_cols), 0)
                )

                # make sure the column is sortable first
                if (request.GET.get('bSortable_{0}'.format(sorted_col_id), 'false') == 'true'):
                    sorted_col_name = column_index_name_map[sorted_col_id]
                    sorting_direction = request.GET.get(
                        'sSortDir_'+str(sorted_index_cols), 'asc'
                    )

                    if sorting_direction == 'desc':
                        sorted_col_name = '-' + sorted_col_name
                    asorting_cols.append(sorted_col_name)
            query_set = query_set.order_by(*asorting_cols)

        # Determine which columns are searchable
        searchable_columns = []

        for col in range(0, cols):
            if request.GET.get('bSearchable_{0}'.format(col), False) == 'true':
                searchable_columns.append(column_index_name_map[col])

        # Apply filtering by value sent by user
        custom_search = request.GET.get('sSearch', '').encode('utf-8')

        if custom_search != '':
            output_q = None
            
            for searchable_column in searchable_columns:

                kwargz = {searchable_column+"__icontains": custom_search}
                output_q = output_q | Q(**kwargz) if output_q else Q(**kwargz)
            query_set = query_set.filter(output_q)

        # Individual column search
        output_q = None

        for col in range(0, cols):
            kwargz = {}
            
            if (request.GET.get('sSearch_{0}'.format(col), False) > ''
                    and request.GET.get('bSearchable_{0}'.format(col), False) == 'true'):

                search_data = request.GET['sSearch_{0}'.format(col)]
                search_data = search_data.split(",")

                if col == 2:

                    for sd in search_data:
                        query_dict = {
                            column_index_name_map[col]: int(sd)
                        }

                        kwargz = kwargz | Q(**query_dict) if kwargz else Q(**query_dict)
                else:
                    
                    for sd in search_data:   
                        query_dict = {
                            column_index_name_map[col]+"__icontains": sd
                        }

                        kwargz = kwargz | Q(**query_dict) if kwargz else Q(**query_dict)
                output_q = output_q & kwargz if output_q else kwargz

        if output_q:
            query_set = query_set.filter(output_q)

        #count how many records match the final criteria
        self.i_total_records = self.i_total_display_records = query_set.count()
        self.query_set = query_set[start_record:end_record]  # get the slice
        self.s_echo = int(request.GET.get('sEcho', 0))  # required echo response

    def get_datatables_records(self, table_data):
        """
        Would return the prepared data to difplayed in data table.
        """

        response_dict = {}

        #preparing the response dict.
        response_dict.update({
            'sEcho': self.s_echo,
            'iTotalRecords': self.i_total_records,
            'iTotalDisplayRecords': self.i_total_display_records,
            'aaData': table_data
        })
        response = HttpResponse(
            simplejson.dumps(response_dict),
            mimetype='application/javascript'
        )

        #prevent from caching datatables result
        add_never_cache_headers(response)
        return response
