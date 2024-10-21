def get_table_name(bulk_search_id):
	bulk_search_id_string = str(bulk_search_id).replace('-', '')
	return f'bulk_lane_pricing_results_{bulk_search_id_string}'
