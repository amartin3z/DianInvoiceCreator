select package_id, uuid,emission_date from download_package p right join (select uuid, emission_date, package_xml_id, package_metadata_id from providers_invoice where xml ='' order by package_xml_id) as t on t.package_xml_id=p.id order by package_id;



select package_id, uuid,emission_date from download_package p right join (select uuid, emission_date, package_xml_id, package_metadata_id from stamping_invoice where xml ='' order by package_xml_id) as t on t.package_xml_id=p.id order by package_id;