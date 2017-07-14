select scanner_name, scanner_notes, full_date, result
from (((((((mrqqa_database.scanner_details 
join mrqqa_database.date_details
on mrqqa_database.scanner_details.scanner_id=mrqqa_database.date_details.scanner_id)
join mrqqa_database.version_details 
on mrqqa_database.date_details.version_id = mrqqa_database.version_details.version_id)
join mrqqa_database.gradsys_details 
on mrqqa_database.date_details.gradsys_id = mrqqa_database.gradsys_details.gradsys_id)
join  mrqqa_database.coil_details
on mrqqa_database.date_details.coil_id = mrqqa_database.coil_details.coil_id) 
join  mrqqa_database.phantom_details
on mrqqa_database.date_details.phantom_id = mrqqa_database.phantom_details.phantom_id)
join mrqqa_database.results
on mrqqa_database.date_details.date_id = mrqqa_database.results.date_id)
join mrqqa_database.series_details
on mrqqa_database.results.series_id = mrqqa_database.series_details.series_id)
where scanner_name = 'Scanner 1a';